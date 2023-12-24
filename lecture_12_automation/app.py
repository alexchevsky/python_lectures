import os
import requests
import pandas as pd
import gspread
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()


FORM_WORKSHEET = 'Сборщик лидов (Responses)'
REPORT_WORKSHEET = 'Leads Report'
GOOGLE_CREDS = '/Users/ak/Code/courses/python_lectures/lecture_12_automation/credentials.json'

telegram_token = os.getenv('telegram_token')
telegram_chat_id = os.getenv('telegram_chat_id')



def get_form_leads(worksheet):
    gc = gspread.service_account(GOOGLE_CREDS)
    ws = gc.open(worksheet).sheet1
    return pd.DataFrame(ws.get_all_records())

def process_form_leads(form_leads):
    form_leads.columns = ['timestamp', 'email', 'company_size', 'city']
    form_leads['timestamp'] = pd.to_datetime(form_leads['timestamp'])
    form_leads['dt'] = form_leads['timestamp'].dt.date
    form_leads['year_month'] = form_leads['timestamp'].dt.to_period('M')
    return form_leads

def get_and_process_leads(worksheet):
    form_leads = get_form_leads(worksheet)
    return process_form_leads(form_leads)

def get_report_leads(worksheet):
    gc = gspread.service_account(GOOGLE_CREDS)
    ws = gc.open(REPORT_WORKSHEET).worksheet('Leads')
    return pd.DataFrame(ws.get_all_records())
    
def find_new_leads(form_leads, report_leads):
    merged_leads = form_leads.merge(
        report_leads, 
        how='left', 
        on='email', 
        suffixes=('', '_drop'),
        indicator=True)
    new_leads = merged_leads[merged_leads['_merge'] == 'left_only'][form_leads.columns]
    return new_leads

def not_empty(new_leads):
    return new_leads.shape[0] > 0

def leads_to_text(df):
    output = []
    for df_line in df.iterrows():
        row = df_line[1]
        output.append(f"{row['email']} - {row['company_size']} - {row['city']}")
    return '\n'.join(output)

def send_message(new_leads):
    message = 'New Leads:\n' + leads_to_text(new_leads)
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    payload = {
        'chat_id': telegram_chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response

def refresh_report_leads(form_leads, worksheet):
    gc = gspread.service_account(GOOGLE_CREDS)
    ws = gc.open(REPORT_WORKSHEET).worksheet('Leads')
    ws.update([form_leads.astype('str').columns.values.tolist()] + form_leads.astype('str').values.tolist())

def main():
    print(f'{datetime.now()} - START')
    form_leads = get_and_process_leads(FORM_WORKSHEET)
    report_leads = get_report_leads(REPORT_WORKSHEET)
    new_leads = find_new_leads(form_leads, report_leads)
    if not_empty(new_leads):
        send_message(new_leads)
    refresh_report_leads(form_leads, REPORT_WORKSHEET)
    print(f'{datetime.now()} - DONE')

if __name__ == '__main__':
    main()
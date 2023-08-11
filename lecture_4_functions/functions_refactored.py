from src import roas_functions

# Calculate the ROAS for five different marketing campaigns


exchange_rate = 1/50

campaigns = [
    {'clicks': 100, 'cpc': 0.50, 'revenue': 120},
    {'clicks': 150, 'cpc': 0.60, 'revenue': 200},
    {'clicks': 90, 'cpc': 0.55, 'revenue': 100},
    {'clicks': 200, 'cpc': 0.65, 'revenue': 280},
    {'clicks': 80, 'cpc': 0.52, 'revenue': 95},
]

if __name__ == '__main__':
    print()
    print()
    for i, campaign in enumerate(campaigns):
        cost = roas_functions.get_cost(campaign['clicks'],
                                       campaign['cpc'])
        cost_new_cur = roas_functions.exchange(cost, exchange_rate)

        roas = roas_functions.get_roas(cost_new_cur, campaign['revenue'])
        print(f"ROAS for campaign {i}: {round(roas,2)}")
    print()
    print()

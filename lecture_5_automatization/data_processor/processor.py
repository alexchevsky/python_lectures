import os
import json
import sys
from datetime import datetime

WD = os.path.dirname(sys.argv[0])
PATH_INBOX = os.path.join(WD, 'inbox')
PATH_PROCESSED = os.path.join(WD, 'processed')
PATH_ARCHIVE = os.path.join(WD, 'archive')


def get_files(path):
    files = os.listdir(path)
    return [os.path.join(path, x) for x in files]


def process_files(files):
    full_data = {}
    for file in files:
        processed_data = process_file(file)
        for k, v in processed_data.items():
            if k in full_data.keys():
                full_data[k] += v
            else:
                full_data[k] = v
        archive(file)
    return full_data


def archive(file, to_dir=PATH_ARCHIVE):
    filename = os.path.basename(file)
    os.replace(
        file,
        os.path.join(to_dir, filename)
    )


def process_file(file, ):
    # {
    #   'The Great Gatsby': 3,
    #   '1984': 5
    # }
    output = {}
    with open(file, 'r') as f:
        for line in f:
            data = json.loads(line)
            item = data['item']
            quantity = data['quantity']
            if item in output.keys():
                output[item] += quantity
            else:
                output[item] = quantity
    return output


def save_data(data, dir=PATH_PROCESSED):
    now = str(datetime.now())
    path = os.path.join(dir, now + '_processed.json')
    with open(path, 'w') as f:
        json.dump(data, f)


def main():
    files = get_files(PATH_INBOX)
    if len(files) > 0:
        processed_data = process_files(files)
        save_data(processed_data)
    print(f'{datetime.now()} - {len(files)} processed')


if __name__ == '__main__':
    main()

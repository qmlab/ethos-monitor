from argparse import ArgumentParser
import base64
import json

def get_args():
    parser = ArgumentParser()
    parser.add_argument('-f', '--file', dest='filename', help='config file name')
    parser.add_argument('-n', '--name', dest='name', help='property name')
    parser.add_argument('-v', '--value', dest='value', help='input value')
    return parser.parse_args()

def update_one(data, n, v):
    encoded = base64.b64encode(v.encode('utf-8')).decode('utf-8')
    data[n] = encoded
    return data

if __name__ == '__main__':
    args = get_args()
    with open(args.filename, "r+") as jsonFile:
        data = json.load(jsonFile)
        data = update_one(data, args.name, args.value)
        jsonFile.seek(0)
        json.dump(data, jsonFile)
        jsonFile.truncate()
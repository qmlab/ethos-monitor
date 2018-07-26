import base64
import json

def load_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)

config = load_config('config.json')
def get_config(name):
    v = config.get(name, '')
    if len(v) == 0:
        return v
    return base64.b64decode(v.encode('utf-8')).decode('utf-8')
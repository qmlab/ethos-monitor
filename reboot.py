import requests
import urllib.parse
from util import get_config

hash = get_config('PanelHash')
get_url = get_config('PanelPublicLink')
post_url = 'https://configmaker.com/?hash=' + hash

def reboot(rig):
    r = requests.get(url=get_url)
    data = r.text.split('\r\n')
    in_section = False
    id = ''
    new_data = []
    for line in data:
        if rig in line and line.startswith('loc'):
            in_section = True
            id = get_id(line)
        elif in_section and line.startswith('loc'):
            new_data.append(generate_reb(id, 1))
            in_section = False
        elif in_section and line.startswith('reb'):
            current_reb = get_reb(line)
            new_data.append(generate_reb(id, current_reb+1))
            in_section = False
            continue
        new_data.append(line)
    if in_section:
        new_data.append(generate_reb(id, 1))
            
    payload = generate_post_payload(hash, '\r\n'.join(new_data))
    r = requests.post(url=post_url, data=payload)
    if r.status_code != 200:
        print('Error in rebooting %s: %s' % (rig, r.text))

def get_id(line):
    return line.split()[1]

def get_reb(line):
    return int(line.split()[2])

def generate_reb(id, reb):
    return "reb %s %d" % (id, reb)

def generate_post_payload(hash, data):
    return {
        'Submit': 'Save Changes',
        'hash': hash,
        'update': data
    }
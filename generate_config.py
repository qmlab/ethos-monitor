from generate import update_one
import json

if __name__ == '__main__':
    data = {}
    useEmail = input('Use Email (True/False)?')
    update_one(data, 'UseEmail', useEmail)
    if bool(useEmail):
        update_one(data, 'EmailServer', input('EmailServer (example: smtp.gmail.com:587):'))
        update_one(data, 'EmailUser', input('Email account address:'))
        update_one(data, 'EmailPassword', input('Email account password:'))
        update_one(data, 'EmailTo', input('Email TO recipient:'))
        update_one(data, 'EmailCC', input('Email CC recipient:(optional)'))

    useFB = input('Use Facebook chat (True/False)?')
    update_one(data, 'UseFB', useFB)
    if bool(useFB):
        update_one(data, 'FBUser', input('Facebook user:'))
        update_one(data, 'FBPassword', input('Facebook account password:'))

    update_one(data, 'Panel', input('Ethos Panel:'))
    update_one(data, 'PanelHash', input('Ethos Panel hash:'))
    update_one(data, 'PanelPublicLink', input('Ethos Panel public link:'))
    update_one(data, 'AutoReboot', input('AutoReboot(True/False)?'))
    update_one(data, 'Logfile', input('Log file name:'))
    update_one(data, 'ExcludeList', input('Rig name list to skip the hash check (separated by ,)(optional):'))
    with open('config.json', 'w') as jsonFile:
        json.dump(data, jsonFile)
        jsonFile.truncate()


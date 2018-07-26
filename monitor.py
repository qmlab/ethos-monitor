import fbchat
import json
import logging
import pyEthOS.pyEthOS as ethos
from reboot import reboot
import smtplib
from util import get_config

def check_hash(driver, gpus, hash):
    if driver == 'nvidia':  # gtx 1070
        return hash >= 30 * gpus
    elif driver == 'amdgpu':    # rx 480
        return hash >= 24 * gpus
    return False

def check_watts(driver, watts):
    for watt in watts:
        if driver == 'nvidia' and int(watt) < 110:  # gtx 1070
            return False
        elif driver == 'amdgpu' and int(watt) < 80:    # rx 480
            return False
    return True

def send_email(errors):
    fromaddr = get_config('EmailUser')
    toaddr  = get_config('EmailTo')
    ccaddrs = get_config('EmailCC')
    username = fromaddr
    password = get_config('EmailPassword')
    server = smtplib.SMTP(get_config('EmailServer'))
    server.ehlo()
    server.starttls()
    server.login(username,password)
    arr = [
        "From: %s" % fromaddr,
        "To: %s" % toaddr,
        "CC: %s" % ccaddrs,
        "Subject: Mining Rigs Alert (%d): %s" % (len(errors), ','.join(errors.keys())),
        "",
        "Details: " + json.dumps(errors),
    ]
    msg = "\r\n".join(arr)
    errs = server.sendmail(fromaddr, [toaddr] + ccaddrs.split(), msg)
    server.quit()
    return len(errs) == 0

def send_fbchat(errors):
    user = get_config('FBUser')
    passwd = get_config('FBPassword')
    client = fbchat.Client(user, passwd)
    return client.send(fbchat.Message(text="EthosOS Alert: %d issues - Details: %s" % (len(errors), json.dumps(errors))), thread_id=client.uid)

if __name__ == "__main__":
    PANEL = get_config('Panel')
    SEND_FB = bool(get_config('UseFB'))
    SEND_EMAIL = bool(get_config('UseEmail'))
    AUTOREBOOT = bool(get_config('AutoReboot'))
    logging.basicConfig(filename=get_config('Logfile'), filemode='a', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    ethos_api = ethos.EthOS_API(PANEL, False)

    rigs = ethos_api.get_summary()['payload']['rigs']
    errors = {}
    exclude_list = []
    exclude_str = get_config('ExcludeList')
    if len(exclude_str) > 0:
        exclude_list = exclude_str.split(',')

    for id, rig in rigs.items():
        driver = rig['driver']
        gpus = int(rig['gpus'])
        hash = rig['hash']
        watts = rig['watts']
        name = rig['rack_loc']
        if name not in exclude_list:
            if not check_hash(driver, gpus, hash):
                errors[name] = 'Abnormal hash value: %d' % hash
        elif not check_watts(driver, watts.split()):
            errors[name] = 'Abnormal power consumption: %s' % watts

    if len(errors) > 0:
        logging.error('errors:' + str(errors))
        if AUTOREBOOT:
            for r, _ in errors.items():
                reboot(r)
                logging.info("Rebooting %s" % r)
        if SEND_EMAIL and not send_email(errors):
            logging.warning("Failed to send email alert")
        if SEND_FB and not send_fbchat(errors):
            logging.warning("Failed to send Facebook message alert")
    
    logging.info('Successfully completed.')
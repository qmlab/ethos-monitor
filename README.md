# Ethos-monitor

## Overview

This is a python program used to monitor the ethos rigs status. You need to schedule it using task scheduler in Windows or crontab in Linux. Only the **monitor** step needs to be scheduled.

## What does it do?

* It checks either of the two:
    1. Hash
    2. Power consumption

* For simplicity, all nvidia gpus are assumed to be *gtx 1070* and all amd gpus are assumed to be *rx 480*.

* To avoid false positive alerts for any wrong reported hash, an exclusion list can be used to skip the hash check for certain rigs. If a rig is in the exclusion list, the power consumption will be checked. Otherwise, the total hash value will be checked.

* The user can send alert to
    1. Email - Set UseEmail to True in **config.json**
    2. Facebook Messenger - Set UseFB to True in **config.json** 

* If AutoReboot in **config.json** is set to True, it will automatically try to reboot the faulty rig on each check.

## How to use it with key files
1. Generate the following key files with **python generate_config.py**. It will propmt a series of questions to generate the config.json from scratch.
2. Run **python monitor.py**
3. (optional) To update any individual entry of config.json, run **python generate.py -f config.json -n [property_name] -v [value]**

## Logging

Logs will be saved in the local file **ethos-monitor.log**

## If any question, please contact me

qmmailbox@gmail.com
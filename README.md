# Ethos-monitor

## Overview

This is a python program used to monitor the ethos rigs status. You need to schedule it using task scheduler in Windows or crontab in Linux. Only the **monitor** step needs to be scheduled.

## What does it do?

* It checks either of the two:
    1. Hash
    2. Power consumption
* For simplicity, all nvidia gpus are assumed to be *gtx 1070* and all amd gpus are assumed to be *rx 480*.
* To avoid false positive alerts for any wrong reported hash, an exclusion list can be used to skip the hash check for certain rigs. If a rig is in the exclusion list, the power consumption will be checked. Otherwise, the total hash value will be checked.
* The configurations are saved in a json file in encoded values.

## How to install?

git clone https://github.com/qmlab/ethos-monitor

## How to use it?
1. Generate the following key files with **python generate_config.py**. It will propmt a series of questions to generate the config.json from scratch.
2. Run **python monitor.py**
3. (optional) To update any individual entry of config.json, run **python generate.py -f config.json -n [property_name] -v [value]**

## Key Configurations
* UseEmail - Send email alerts
* UseFB - Send Facebook chat alerts
* AutoReboot - Whether automatically reboot the faulty rig using EthOS (cannot reboot if the OS crashes)
* Logfile - File path to save local logs
* Panel* - EthOS panel information

## Logging

Logs will be saved in the local file **ethos-monitor.log**

## Contact Me

qmmailbox@gmail.com

## License

The MIT License

Copyright (c) 2010-2018 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.MIT
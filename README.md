# Zabbix  Onboard script

## Simplify onboarding process by creating Users, Templates and Host groups and it gives appropriate permissions to user groups. 

## Requirements: 
 Python 3.9 or never ( I had no opportunity to test it with older version),
 Python modules: csv, json, requests, urlib3,
 Admin access to Zabbix instance,
 Zabbix API key,

### Files:

**zabbix_onboard_main.py** – main script file ,
**zabbix_onboard_def.py** – file with functions used by main script,
**onboard.conf** – script configuration file,
**onboard_template.csv** – template for read/write groups available for users assigned to account,
**templates_ro.csv** – template with read-only groups available for users assigned to account

### Usage:
1.	In onboard.conf the following variables must be set:
 •	url – link to Zabbix api for ex:
    url = zabbix.linux.rocks/api_jsonrpc.php
 •	key – user API key   for ex:
    key = b596cb8da1c91da7d6179b7f3ea3a40847f32c536641defa9703f3c76302ef61
 •	account code – onboarded Account TRI CODE for ex:
    account_code = ZZZ
### Please remember to save file.

 2.	Run main script for ex:
    python3.12 zabbix_onboard_main.py
### 3.	Check Zabbix GUI.

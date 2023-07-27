#!/usr/bin/env python

import sys
import time
import json
import os
import requests
from requests.auth import HTTPBasicAuth

debug_enabled = True

now = time.strftime("%a %b %d %H:%M:%S %Z %Y")
pwd = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# Set paths
log_file = '{0}/logs/integrations.log'.format(pwd)

def debug(msg):
    if debug_enabled:
        msg = "{0}: {1}\n".format(now, msg)
        print(msg)
        f = open(log_file,"a")
        f.write(msg)
        f.close()

CHAT_ID="-994280177"
#CHAT_ID=os.environ.get('TELEGRAM_CHAT_ID')
#debug(CHAT_ID)
# Read configuration parameters
alert_file = open(sys.argv[1])
hook_url = sys.argv[3]

# Read the alert file
alert_json = json.loads(alert_file.read())
debug("# TELEGRAM ALERT JSON")
#debug(alert_json)
alert_file.close()

# Extract data fields
alert_level = alert_json['rule']['level'] if 'level' in alert_json['rule'] else "N/A"
description = alert_json['rule']['description'] if 'description' in alert_json['rule'] else "N/A"
agent = alert_json['agent']['name'] if 'name' in alert_json['agent'] else "N/A"
username = alert_json['data']['dstuser'] if 'dstuser' in alert_json['data'] else "N/A"
# Generate request
msg_data = {}
msg_data['chat_id'] = CHAT_ID
msg_data['text'] = {}
msg_data['text']['description'] =  description
msg_data['text']['alert_level'] = str(alert_level)
msg_data['text']['agent'] =  agent
msg_data['text']['username'] = username
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}


# Send the request
requests.post(hook_url, headers=headers, data=json.dumps(msg_data))

sys.exit(0)

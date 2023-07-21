apt update && apt install -y wget
wget https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/alienvault_reputation.ipset -O /var/ossec/etc/lists/alienvault_reputation.ipset
wget https://wazuh.com/resources/iplist-to-cdblist.py -O /tmp/iplist-to-cdblist.py
/var/ossec/framework/python/bin/python3 /tmp/iplist-to-cdblist.py /var/ossec/etc/lists/alienvault_reputation.ipset /var/ossec/etc/lists/blacklist-alienvault
rm -rf /var/ossec/etc/lists/alienvault_reputation.ipset
rm -rf /tmp/iplist-to-cdblist.py
chown wazuh:wazuh /var/ossec/etc/lists/blacklist-alienvault
chmod 660 /var/ossec/etc/lists/blacklist-alienvault

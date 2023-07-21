#MariaDB
!290 ar.conf
restart-ossec0 - restart-ossec.sh - 0
restart-ossec0 - restart-ossec.cmd - 0
restart-wazuh0 - restart-ossec.sh - 0
restart-wazuh0 - restart-ossec.cmd - 0
restart-wazuh0 - restart-wazuh - 0
restart-wazuh0 - restart-wazuh.exe - 0
firewall-drop60 - firewall-drop - 60
netsh60 - netsh.exe - 60
!203 agent.conf
  <agent_config>
    <!-- Shared agent configuration here -->
    <localfile>
      <log_format>syslog</log_format>
      <location>/var/log/mysql/error.log</location>
    </localfile>
  </agent_config>

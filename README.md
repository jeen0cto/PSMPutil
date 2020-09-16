# PSMPUtil #
**version: 1.1**
**Last update : 2020-09-16**

Generate registry file for Putty session suitable for SSH connection through CyberArk PSM Proxy using a list of server name (no fqdn).  

Hostname registry key values will be in the format : 
```
username@cyberarkaccount#domain@fqdn_server@PSMP_ipaddress
```

All parameters can be customized in YAML configuration file 

```
psmp:
    host: 127.0.0.1
    domain: mydomain.foo
users:
    - username: albert
      account: adm-albert
    - username: john
      account: adm-john
input:
    serverlist_filename: servers.txt
    puttytemplate_filename: putty_template.txt
output:
    filename: putty_psmp.reg
```

Please report bug to: **jeen0cto@gmail.com**

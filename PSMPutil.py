# PSMPUtil 2020-09-16 - ver 1.1
# author: Jeen0cto
#
# Description
# Generate registry file for Putty session suitable for SSH connection through CyberArk PSM Proxy
# Hostname Key value will be in the format : 
#                       username@cyberarkaccount#domain@fqdn_server@PSMP_ipaddress
#
# All parameters are in PSMPutil.yaml configuration file
# Please report bug to: jeen0cto@gmail.com

import re
import yaml
from colorama import init, Fore, Back, Style
init()

print(Style.BRIGHT)
print(Fore.YELLOW + '*** PSMP Util - ver 1.0 ***')
print()

# Load configuration file (YAML) 
print(Fore.GREEN + 'Loading configuration file...')
file = open('PSMPutil2.yaml', 'r')
cfg = yaml.load(file, Loader=yaml.FullLoader)

# PSMP Section
section = cfg['psmp']
PSMPHost = section['host']
domain = section['domain']

# Users Section (it's a list!)
users = cfg['users']

# Input Section
section = cfg['input']
serverlist_filename = section['serverlist_filename']
puttytemplate_filename = section['puttytemplate_filename']

# Output Section
section = cfg['output']
print('Done.')
print()

# Open file server list
serversf = open(serverlist_filename,"r")

d = {}
for usr in users:
    username = usr['username']
    account = usr['account']

    # Create registry output file
    outfile = username + "_" + section['filename']
    outregf = open(outfile,'w')

    # connection string part one
    part1 = username + '@' + account + '#' + domain + '@'

    print(Fore.YELLOW  + 'Create Putty Session registry file: ' + Fore.WHITE + outfile)
    print(Fore.GREEN + 'Username : ' + Fore.WHITE + username)
    print(Fore.GREEN + 'Account : ' + Fore.WHITE + account)
    print(Fore.GREEN + 'Server list file : ' + Fore.WHITE + serverlist_filename)
    print(Fore.GREEN + 'PSM Proxy IP: ' + Fore.WHITE + PSMPHost)
    
    for srv in serversf:
        servername = srv.splitlines()[0]
        hostname = part1 + servername + '.' + domain + '@' + PSMPHost
        d['servername'] = srv.splitlines()[0] + '_PSMP'
        d['hostname'] = hostname
        
        templatef = open(puttytemplate_filename,'r')
        for line in templatef:
            if re.findall(r"<server>", line):
                line = line.replace('<server>', srv.splitlines()[0] + '_PSMP')
            if re.findall(r"<hostname>", line):
                line = line.replace('<hostname>', hostname)
            outregf.write(line)
        templatef.close()
    print(Fore.YELLOW  + 'Closing output file: ' + Fore.WHITE +  outfile)
    print(Fore.YELLOW + '')
    outregf.close()

serversf.close()
print(Fore.GREEN + 'Done.')

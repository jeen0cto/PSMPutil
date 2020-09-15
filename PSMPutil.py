# PSMPUtil 2020-06-28 - ver 1.0 
# author: Jeen0cto
#
# Description
# Generate registry file for Putty session suitable for SSH connection through CyberArk PSM Proxy
# Hostname Key value will be in the format : 
#                       username@cyberarkaccount#domain@fqdn_server@PSMP_ipaddress
#
# All parameters are in PSMPutil.yaml configuration file
#
# Please report bug to: jeen0cto@gmail.com

import re
import yaml
from colorama import init, Fore, Back, Style
init()

#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
print(Style.BRIGHT)
#print('back to normal now')

print(Fore.YELLOW + '*** PSMP Util - ver 1.0 ***')
print()


# Load configuration file (YAML) 
print(Fore.GREEN + 'Loading configuration file...')
file = open('PSMPutil.yaml', 'r')
cfg = yaml.load(file, Loader=yaml.FullLoader)

# PSMP Section
section = cfg['psmp']
PSMPHost = section['host']
# Users Section
section = cfg['users']
username = section['username']
account = section['account']
domain = section['domain']
# Input Section
section = cfg['input']
serverlist_filename = section['serverlist_filename']
puttytemplate_filename = section['puttytemplate_filename']
# Output Section
section = cfg['output']
outfile = username + "_" + section['filename']
print('Done.')
print()

print('Create Putty Session registry file: ' + Fore.WHITE + outfile)
print(Fore.GREEN + 'Username : ' + Fore.WHITE + username)
print(Fore.GREEN + 'Account : ' + Fore.WHITE + account)
print(Fore.GREEN + 'Server list file : ' + Fore.WHITE + serverlist_filename)
print(Fore.GREEN + 'PSM Proxy IP: ' + Fore.WHITE + PSMPHost)
print()

# Open file server list
serversf = open(serverlist_filename,"r")
# Create registry output file
outregf = open(outfile,'w')

# connection string part one
part1 = username + '@' + account + '#' + domain + '@'

d = {}
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

serversf.close()
outregf.close()
print(Fore.GREEN + 'Closing output file: ' + Fore.WHITE +  outfile)
print(Fore.GREEN + 'Done.')

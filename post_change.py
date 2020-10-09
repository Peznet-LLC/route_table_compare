#!/usr/bin/env python3


from netmiko import ConnectHandler
import sys, getopt
import argparse
import json
import subprocess

out_file = "pre_change.json"
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--routerip',
                        '-r',
                        help='IP of Router to Query',
                        required=True)
    parser.add_argument('--user',
                        '-u',
                        help='Username to login to router',
                        required=True)
    parser.add_argument('--password',
                        '-p',
                        help='password to login to router',
                        required=True)
    parser.add_argument('--vrf',
                        '-v',
                        help='VRF to look at (e.g inet.0 or customer1.inet.0',
                        required=True)
    args = parser.parse_args()

router_ip = args.routerip
user_name = args.user
pass_word = args.password
vrf = args.vrf

# Establish a connection to the router
virtual_srx = {
    'device_type': 'juniper',
    'host':   router_ip,
    'username': user_name,
    'password': pass_word,
    'port' : 22,
}
net_connect = ConnectHandler(**virtual_srx)

router_command = "show route table " + vrf + " | display json"

output = net_connect.send_command(router_command)

f = open("post_change.json", "w")
f.write(output)
f.close()
subprocess.call("./route_table_compare.py", shell=True)

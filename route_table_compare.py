#!/bin/env python3
import csv
import json
import argparse
import sys
import logging
import pandas as pd 
from deepdiff import DeepDiff, extract
from colorama import init
from colorama import Fore, Back, Style
from pprint import pprint

with open ('pre_change.json') as f:
  data = json.load(f)


with open ('post_change.json') as f2:
  data2 = json.load(f2)


modified_map = {
    'values_changed': 'CHANGED',
    'dictionary_item_added': 'ADDED',
    'dictionary_item_removed': 'REMOVED',
    'iterable_item_added': 'ADDED',
    'iterable_item_removed': 'REMOVED'
}
router_data = {}
nexthop = {}
router_data2 = {}



def parse_dict(_dict, _parsed):
  for k, v in _dict.items():
      if k == "route-table":
          for i2 in v[0]["rt"]:
                if "nh" in i2["rt-entry"][0]:
                  nexthop = i2["rt-entry"][0]["nh"][0]
                  _parsed[i2["rt-destination"][0]["data"]] = {"next-hop": nexthop}
          

           
      else:
        if type(v) is list:
            parse_list(v, _parsed)
        elif type(v) is dict:
            parse_dict(v, _parsed)



       

def parse_list(_list, _parsed):
  for i in _list:
    if type(i) is dict:
      parse_dict(i, _parsed)


parse_dict(data, router_data)
parse_dict(data2, router_data2)
results = {}
results = DeepDiff(router_data, router_data2)
routes_added = "Routes Added"
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


if "dictionary_item_added" in results:

    for route in results["dictionary_item_added"]:
        replace_prefix = (route.replace("root['", ""))
        route2 = replace_prefix.replace("']", "")
        print(route2 + " via next-hop " + router_data2[route2]["next-hop"]["to"][0]["data"] + " on interface " + router_data2[route2]["next-hop"]["via"][0]["data"])


print()
print()


if "dictionary_item_removed" in results:
    routes_removed = "Routes Removed"

    print(color.BLUE + routes_removed.center(40) + color.END)
    print()
    print()


    for key in results["dictionary_item_removed"]:
        key = key.replace("root['", "")
        key = key.replace("']['next-hop']['to'][0]['data']", "")
        key = key.replace("']", "")
        key = key.replace("']['next-hop']['via'][0]['data']", "")
        #print(router_data2)
        print(key + " via next-hop " + router_data[key]["next-hop"]["to"][0]["data"] + " on interface " + router_data[key]["next-hop"]["via"][0]["data"])

    print()
    print()
    print()


if "values_changed" in results:
    routes_changed = "Routes Changed"

    print(color.BLUE + routes_changed.center(40) + color.END)
    print()
    print()
    for key, value in results["values_changed"].items():
        key = key.replace("root['", "")
        key = key.replace("']['next-hop']['to'][0]['data']", "")
        key = key.replace("']['next-hop']['via'][0]['data']", "")
        print(key + " next hop changed from " + value["old_value"] + " to " + value["new_value"])
        
    
    

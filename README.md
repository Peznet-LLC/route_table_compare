# route_table_compare
Networks are becoming increasingly complex and changes done to devices have unintended consequences.  Theses simply python scripts capture the routing table of Juniper devices before and after the change is made.  

# To install and run

Requies Python 3.8:

pip3 install deepdiff
pip3 install argparse
pip3 install pandas
pip3 install colorama


# To run compare:


Run this to take snapshot of Junos routing table before a change:


python3 pre_change.py -r routerip -u username -p password -v vrf


Run this to take a snapshot of Junos routing table after a change:


python3 post_change.py -r 192.168.10.2 -u username -p password -v vrf

example:

python3 pre_change.py -r 192.168.1.1 -u netconf -p LetmeIn123! -v customer1.inet.0

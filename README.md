# route_table_compare
Networks are becoming increasingly complex and changes done to devices have unintended consequences.  Theses simply python scripts capture the routing table of Juniper devices before and after the change is made.  

# To install and run

Requies Python 3.8:

(If needed)

sudo apt install python3-pip

pip3 install deepdiff argparse pandas colorama

chmox +x pre_change.py post_change.py route_table_compare.py


# To run compare:


Run this to take snapshot of Junos routing table before a change:


pre_change.py -r routerip -u username -p password -v vrf


Run this to take a snapshot of Junos routing table after a change:


post_change.py -r 192.168.10.2 -u username -p password -v vrf

example:

pre_change.py -r 192.168.1.1 -u netconf -p LetmeIn123! -v customer1.inet.0

Note the VRF must be specificed.  If global VRF is desired or VRF's are not used specific "inet.0" as VRF for option "-v".

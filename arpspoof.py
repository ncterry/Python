"""
Machines on a network can identify each other.
Machine M asks for the MAC addressm of a certain IP address the N-machine
It may happen that any other machine, that happens to know which MAC address is at the target IP address, may respond.
Then M will update its own tables that the response MAC address is now tied to the IP
If this is hijacked, and faked, then the attacker can then impersonate the target, and get packets from M
The attacker can still forward the packets from M to N, so it does not look like anything is wrong.

M = victim
N = router
+ attacker

M Send a request packet  ----->    [man in middle]   <--------- N send back a response packet

    # arp -a        (see full arp tables of the machine. list of IP/MAC addresses that are connected.
    Internet Address            Physical Address
    192.168.1.1                 a4:c0:6f:25:96:85
    224.0.0.2                   ff:ff:ff:ff:ff:ff

scapy - a library for python, but is ALSO a internal machine on Linux also.

Details seen on:    OneNote --> Python Pentest --> arpspoof
"""


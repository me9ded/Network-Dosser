from scapy.all import *
#capture the frame in your network topology you need to know at least one know mac address in order to create the packet
packet=sniff(filter="ether dst 3a:96:2a:cf:ef:3c",count=1)
# to examine the captured frame
packet[0]
# to show the packet nicely
packet[0][0].show()
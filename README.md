These two scripts demonstrate potential vulnerabilities in network security by manipulating Ethernet frames and network protocols. By using these scripts, network traffic can be manipulated in a way that forces frames to be transferred solely to your machine, which you can then inspect with tools like Wireshark. 
This project illustrates how common security protocols can be exploited for educational purposes.

Script 1: Sniffing Ethernet Frames
The first script captures Ethernet frames by sniffing the network. This requires knowing at least one MAC address in the network to filter the traffic and capture only relevant frames.
Using a tool like Wireshark, you can inspect the captured frames for further analysis.

Script 2: Manipulating Spanning Tree Protocol (STP)
The second script targets the Spanning Tree Protocol (STP), which is used to prevent network loops and ensure a robust switching network.
The script tricks the network into believing that your machine is the root switch. By forcing this condition, the STP process is disrupted, causing network traffic to be rerouted through your device, effectively "ruining" the STP.
Steps to Obtain a MAC Address:
Scan the Network with Zenmap

Since you're connected to the network, you can use Zenmap (the graphical interface for Nmap) to scan the entire network. This will help you identify the IP addresses of devices on the network.
Note: You need to scan the network IP address (e.g., 192.168.1.0/24) instead of a specific user’s IP. Zenmap also provides additional information, like the operating system of the devices.
Example Zenmap Usage:
<img width="1422" alt="Screenshot 2024-10-08 at 8 39 05 PM" src="https://github.com/user-attachments/assets/8d039a26-89de-40c9-9b78-4b69becad111">

For more information on Zenmap, refer to the Nmap documentation.



Obtain the MAC Address with Hydra

Once you've identified a device on the network, you can use Hydra to brute-force credentials and gain access to the system.
After accessing a Windows machine, you can use the getmac command to retrieve the MAC address. For other operating systems, the appropriate command will depend on the OS (which can be identified using Zenmap).
Example Hydra Usage:
<img width="827" alt="Screenshot 2024-10-08 at 8 36 24 PM" src="https://github.com/user-attachments/assets/2b631156-7644-4dbc-983b-43da91c32368">

For more documentation, refer to the Hydra documentation.



Disclaimer:
These scripts are intended for learning purposes only and are not meant for malicious activities. Misusing these techniques to disrupt networks or unauthorized systems is illegal and unethical.

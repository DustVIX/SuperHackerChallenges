# Create a simple packet sniffer that captures network traffic.

from scapy.all import *

def analyzer(pkt):
    if pkt.haslayer(TCP):
        print("==========TCP==========")
        print("SRC-IP: " + pkt[IP].src)
        print("DST-IP: "+ pkt[IP].dst)
        print("SRC-port: " + str(pkt.sport))
        print("DST-port: "+ str(pkt.dport))

        print("=======================\n")

    if pkt.haslayer(UDP):
        print("==========UDP==========")
        print("SRC-IP: " + pkt[IP].src)
        print("DST-IP: "+ pkt[IP].dst)
        print("SRC-port: " + str(pkt.sport))
        print("DST-port: "+ str(pkt.dport))
        print("=======================\n")
    


print("*************** STARTED ***************")

iface = IFACES.dev_from_name("Intel(R) Wi-Fi 6E AX211 160MHz") 
sniff(iface=iface,prn=analyzer)
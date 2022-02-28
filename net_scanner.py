import scapy.all as scapy
import optparse
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ip", dest = "ip_address", help = "Enter IP Address.")
    (user_input, arguments) = parse_object.parse_args()

    if not user_input.ip_address:
        print("Enter IP Address!")
    return user_input

def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst = ip) #arp paketi olusturuyoruz hangi ip araliginda tarama yapacaksak onu yaziyoruz
    #scapy.ls(scapy.ARP()) # linux man komutu gibi fonksiyon konusunda yardim eder
    broadcast_packet = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") # belirtilen mac adresinde tarama yapar dst yazmasakta olur default olarak ayni cunku
    #scapy.ls(scapy.Ether())
    combined_packet = broadcast_packet / arp_request_packet # scapy dilinde iki paketi al tek paket haline donustur demek
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout = 1) #timeout arp isteginde cevap verilmeyen paketlerde bekleme devam et anlamina geliyor
    answered_list.summary() #aldigimiz ciktilari duzgun bir sekilde ozete dokme

user_ip_address = get_user_input()
scan_my_network(user_ip_address.ip_address)
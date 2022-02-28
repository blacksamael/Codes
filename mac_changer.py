import subprocess
import optparse
import re

def get_user_input():
    parse_object = optparse.OptionParser() # terminalde kullanicidan veri almak icin bir obje olusturuyoruz 
    parse_object.add_option("-i", "--interface", dest = "interface", help = "Interface to change!") #terminalden kullanicinin girdigi interface i almak icin
    parse_object.add_option("-m", "--mac", dest = "mac_address", help = "New mac address = ?") #terminalden kullanicinin girdigi mac addressi almak icin
    return parse_object.parse_args() # argumanlari geri dondurmek

def change_mac_address(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"]) #belirtilen arayuzu kapatiyoruz
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address]) #belirtilen arayuzun mac adresini kullanicinin belirttigi mac adresi ile degistiriyoruz
    subprocess.call(["ifconfig", user_interface, "up"]) # belirtilen arayuzu tekrar aciyoruz

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface]) #ifconfig degiskenine linuxtaki ifconfig sonucunu esitliyoruz 
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig)) #regex101 ile esitledigimiz sonucta mac adresini ariyoruz
    if new_mac: #eger belirttigimiz regex'i(mac adresi) alabilirse
        return new_mac.group(0) #esitledimiz maci donduruyor
    else:
        return None #mac adresini alamazsa hicbir sey dondurmuyor

print("Mac changer started.")
(user_input, arguments) = get_user_input() #user input fonksiyonundaki kullanici verilerini degiskene atiyoruz
change_mac_address(user_input.interface, user_input.mac_address) #mac adresini degistirme islemini yapiyoruz
finalized_mac = control_new_mac(str(user_input.interface)) # son olarak kullanicinin yazdigi mac adresi ile bilgisayarinki ayni mi diye kontrol edip bilgisayarin amc adresini geri donduruyoruz

if finalized_mac == user_input.mac_address: #eger bilgisayarin mac'i kullanicinin verdigi mac adresi ile ayni ise 
    print("Success!") 
else:
    print("Error!")
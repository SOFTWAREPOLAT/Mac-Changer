import subprocess
import optparse
import re


def kullanici_girdisi():

    kullanim_sekli = optparse.OptionParser()
    kullanim_sekli.add_option("-i","--interface",dest="interface",help="interface to change!")
    kullanim_sekli.add_option("-m","--mac",dest="mac_adresi",help="new mac adresi")

    return kullanim_sekli.parse_args()

def mac_degistirici(kullanici_interface,kullanici_mac_adresi):
    subprocess.call(["ifconfig",kullanici_interface,"down"])
    subprocess.call(["ifconfig", kullanici_interface,"hw","ether",kullanici_mac_adresi])
    subprocess.call(["ifconfig",kullanici_interface,"up"])

def yeni_mac_kontrol(interface):

    ifconfig = subprocess.check_output(["ifconfig",interface])
    yeni_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if yeni_mac:
        return yeni_mac.group(0)
    else:
        return None

print("Mac Değiştirici Başladı")
(kullanici_girdisi,arguments) = kullanici_girdisi()
mac_degistirici(kullanici_girdisi.interface,kullanici_girdisi.mac_adresi)
mac_final = yeni_mac_kontrol(str(kullanici_girdisi.interface))

if mac_final == kullanici_girdisi.mac_adresi:
    print("Mac Adresi Değiştirildi!")
else:
    print("Hata!!")
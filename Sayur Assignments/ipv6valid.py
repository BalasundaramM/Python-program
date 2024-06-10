def ipaddress(ipv6):
    ipv6 = ipv6.lower()
    hexa = ipv6.split(':')
    char_valid = set('abcdef0123456789')  
      
    if len(hexa) != 8 and '::' not in ipv6 or ipv6.count('::') >1:
        print("Enter a valid IPv6 address with 8 segments or use '::' for an omitted group")
        return False

    for hexadeci in hexa:

        if len(hexadeci) > 4 :
            print("Maximum 4 characters should be in each segment")
            return False

        for hexachar in hexadeci:
            if hexachar not in char_valid:
                print("IPv6 should contain only hexadecimal characters")
                return False

    return True            

with open("C:\\Users\\MIRUDULAA\\Downloads\\ipv6addresses.txt", "r") as file:
    ipv6_addresses = file.readlines()

for address in ipv6_addresses:
    ipv6 = address.strip()
    if ipaddress(ipv6):
        print(f"{ipv6} is a valid IPv6 Address")
    else:
        print(f"{ipv6} is an invalid IPv6 address ")        

import nmap

scanner = nmap.PortScanner()

print("welcome")
print("<---------------->")

ip_addr = input("please enter the ip address: ")
print("The ip address is: " + ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
             1) SYN ACK SCAN
             2)UDP SCAN
             3)COMPREHENSIVE SCAN""")
print("you have selected option: " + resp)

if resp == "1":
    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr.state]())
    print(scanner[ip_addr].all_protocols())
    print("open Ports: ", scanner[ip_addr]['tcp'].keys())


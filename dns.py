import socket

def dns_lookup(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        print(f"IP Address for {domain_name}: {ip_address}")
    except socket.gaierror:
        print(f"Could not resolve {domain_name}")

if __name__ == "__main__":
    domain_name = input("Enter a domain name to perform a DNS lookup: ")
    dns_lookup(domain_name)

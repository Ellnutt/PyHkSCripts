import nmap
begin = 75
end = 80
target = '******'
scanners = nmap.PortScanner()
for port in range(begin, end+1):
    res = scanners.scan(target, str(i))
    res = res['scan'][target]['tcp'][i]['state']
    print(f'port [i] is {res}.')
    

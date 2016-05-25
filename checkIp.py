def checkIp(str):
    result = True
    ip = str.split('.')
    print(ip)
    if len(ip) != 4:
        result = False
    else:
        for i in ip:
            if result and i.isdigit() and (-1 < int(i) < 256):
                continue
            else:
                result = False
                break
    return result

print(checkIp('10.35.160.133'))
print(checkIp('300.250.3.2'))
print(checkIp('yogev rabl'))
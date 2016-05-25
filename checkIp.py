def checkIp(str):
    result = True

    if len(str.split('.')) != 4:
        result = False
    else:
        for i in str.split('.'):
            if result and i.isdigit() and (-1 < int(i) < 256):
                continue
            else:
                result = False
                break
    return result

print(checkIp('10.35.160.133'))
print(checkIp('100.250.3.8'))
print(checkIp('yogev rabl'))
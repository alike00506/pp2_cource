def counter(txt):
    uppr = 0
    lowr = 0
    for char in txt :
        if char.isupper():
            uppr += 1
        elif char.islower():
            lowr += 1
    return uppr,lowr 
stringg = input()
result = counter(stringg)
print(result)           
r1=int(input('start range: '))
r2=int(input('end range: '))
line=[z for z in range(r1, r2+1) if z % 7 ==0 and z % 5 != 0]
print(line)
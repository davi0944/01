fir = 1
de = 0
a = input()
for letter in a:
    if(fir == letter):
        de = 1
    fir = letter

if(de == 1):
    print('yes')
else:
    print('no')




grngan=['bakwan','risoles','tahu']
buah=['apel','semangka','nenas']
sayur=['bayam','kangkung','kol']

#menggabungkan list
belanja=[grngan,buah,sayur]
print(belanja)
print('='*20)
#for didalam for
for subdatarblnja in belanja:
    print(subdatarblnja)
    for komponen in subdatarblnja:
        print(komponen)


anka=10

for i in range(0,20):
    print(i)
    if i is anka:
        print('angka ditemukan',i)
        break
else:
    print('angka tdak dtmukan')

 

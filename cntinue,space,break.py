print('='*5,'break')
for i in range(10,20):
    
    if i is 15:
        print('angka cantik=',15)
        break#berfungsi menhentikan program
    print('angka aye',i)
else:
    print('nilai yang terakir=',i)

print('='*5,'continue')

for i in range(10,20):
    
    if i is 15:
        print('angka cantik=',15)
        continue#melanjutkan ke step berikutnya
    print('angka aye',i)
else:
    print('nilai yang terakir=',i)

print('='*5,'pass')
    
for i in range(10,20):
    
    if i is 15:
        print('angka cantik=',15)
        pass #melewatkan/melanjutkan p
    print('angka aye',i)
else:
    print('nilai yang terakir=',i)
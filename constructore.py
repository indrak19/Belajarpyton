#membuat Kunstruktor

class user:
    total=0
    def __init__(self,name,email,status) :
        self.name=name #atribut
        self.email=email #atribut
        self.status=status #atribut
        user.total+=1

    def info(self):
        return f'{self.name}-{self.email}-{self.status}'

    def updatestatus(self,status):
        self.status=status



#instance variable VS class variable
indra=user('indra','indrareynaldo@gmail.com','admin')

print(indra.info())#memanggil class
indra.updatestatus('moderator')
print(indra.info())# mengubah status

print(user.total)
kaya=user('kaya','kaya@gmail.com','admin')
print(user.total)
print(indra.name)
print(indra.email)
print(indra.status)

print(kaya.name)
print(kaya.email)
print(kaya.status)
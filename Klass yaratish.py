# TASK1
class User():
    def __init__(self,ism,familya,email):
        self.ism = ism
        self.familya = familya
        self.email = email
user1 = User('Olim','Hasanov','<EMAIL>')
print(user1.ism)
print(user1.familya)
print(user1.email)

# TASK2
class User():
    def __init__(self,username,ism,familya,email):
        self.username = username
        self.ism = ism
        self.familya = familya
        self.email = email

    def get_username(self):
        return self.username
    def get_ism(self):
        return self.ism

    def get_familya(self):
        return self.familya

    def get_email(self):
        return self.email

user1 = User('Olim2000','Olim','Hasanov','<EMAIL>')
print(f"Foydalanuvchi: {user1.get_username()}")
print(f"Ismi: {user1.get_ism()} {user1.get_familya()}")
print(f"Email: {user1.get_email()}")

# TASK3
class Avtolar():
    def __init__(self,nomi,yili,narxi,rang):
        self.nomi = nomi
        self.yili = yili
        self.narxi = narxi
        self.rang = rang

    def avto_info(self):
        print(f"Nom : {self.nomi}\n"
              f"Yili : {self.yili}\n"
              f"Narxi : {self.narxi}\n"
              f"Kompania : {self.rang}")
avto1 = Avtolar('Nexia',2010,8000, 'qora')
avto2 = Avtolar('Spark',2016,9000, 'ko\'k')
avto3 = Avtolar('Damas',2019,10000, 'oq')
avto1.avto_info()
avto2.avto_info()
avto3.avto_info()
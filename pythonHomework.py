# it_park = ['python','css','javascript','html','c++']
# print(it_park)
# del it_park[1]
# print(it_park)
# it_park.append('js')
# it_park.append('css')
# it_park.insert(0,'c++')
# print(it_park)


# VariableType = []
# element = input("1-tilni kiriting:")
# VariableType.append(element.title())
# element = input("2-tilni kiriting:")
# VariableType.append(element.title())
# element = input("3-tilni kiriting:")
# VariableType.append(element.title())
# element = input("4-tilni kiriting:")
# VariableType.append(element.title())
# element = input("5-tilni kiriting:")
# VariableType.append(element.title())
# print(VariableType)

#
# Ozbekiston = ['xorazm','buxoro','toshkent','termiz','navoiy']
# print(Ozbekiston)
# print(len(Ozbekiston))
# print(sorted(Ozbekiston))
# print(sorted(Ozbekiston, reverse=True))
# print(Ozbekiston)
#
#
# sonlar = list(range(180,1800,2))
# print(sonlar)
# sonlar1 = sum(sonlar)
# print(sonlar1)
# sonlar2 = min(sonlar)
# sonlar3 = max(sonlar)
# sonlar4 = sonlar3 - sonlar2
# print(sonlar4)
# sonlar5 = sonlar2 + sonlar3
# print(sonlar5)
# print(len(sonlar))
# sonlar0 = sonlar[:10]
# print(sonlar0)
# sonlar_1 = sonlar[100:110]
# print(sonlar_1)
# sonlar_2 = sonlar[200:210]
# print(sonlar_2)

# If

# login = input("Login kiriting :")
# if login == "root":
#     print("Xush kelibsiz Rootjon! Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz {login}!")


# son1 = int(input("Birinchi son:"))
# son2 = int(input("Ikinchi son:"))
# if son1 == son2:
#     print("Sonlar teng")
# else:
#     print("Sonlar teng emas")

# son = float(input("Xohlagan sonni kiriting:"))
# if son < 0:
#     print("Manfiy son")
# else:
#     print("Musbat son")


# son = float(input("Son kiriting:"))
# if son > 0:
#     print(f"{son**(1/2)}")
# else:
#     print("Msubat son kiriting")


# son = []
# son1 = int(input("Son kiriting:"))
# son.append(son1)
# son1 = int(input("Son kiriting:"))
# son.append(son1)
# son1 = int(input("Son kiriting:"))
# son.append(son1)
# son1 = int(input("Son kiriting:"))
# son.append(son1)
# son1 = int(input("Son kiriting:"))
# son.append(son1)


# yosh = int(input("Yoshingizni nechida:"))
# if yosh < 5 or yosh > 65:
#     print("Kirish bepul")
# elif yosh < 18:
#     print("Kirish 15000 so'm")
# elif yosh > 18:
#     print("Kirish 20000 so'm")


# son1 = int(input("Birinchi son:"))
# son2 =  int(input("Ikkinchi son:"))
# if son1 == son2:
#     print("Sonlar teng")
# elif son1 > son2:
#     print("Birinchi son ikkinchi sondan katta")
# elif son1 < son2:
#     print("Birinchi son ikkinchi sondan kichik")


# son = int(input("Son kiriting:"))
# numbers = []
# for i in range(3,16):
#     if son % i == 0:
#         numbers.append(i)
# print(numbers)


# users = ['shdjf','hgjd','gdf','jshdg','jghsadf']
# login = str(input("Login kiriting:"))
# if login in users:
#     print("Bu login band")
# else:
#     print("xush kelibsiz!")

#
# kompyuter = {
#     'narx':1000,
#     'nomi':'Asus',
# }
# # print(kompyuter['narx'])
# # kompyuter['yili']= 2023
# # print(kompyuter)
#
# comp = kompyuter.get('narx')
# print(comp)


davlatlar = {'uzbekiston':'Toshkent','Rossiya':'MOscow'}
print(sorted(davlatlar.keys()))

print(sorted(davlatlar.values()))

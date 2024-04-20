# Tub sonni aniqlash
def tubsonni_topish(n):
    i = 1
    k = 0
    while i<=n:
        if n%i == 0:
            k+=1
        i+=1
        if k>2:
            break
    if k == 2:
        print(f"{n} tub son")
    else:
        print(f"{n} tub son emas")
tubsonni_topish(17)

# EKUB
def ekubni_topish(a,b):
    while a != b:
        if a>b:
            a-=b
        else:
            b-=a
    print(f"EKUB {a}")
ekubni_topish(18,42)
ekubni_topish(25,425)
ekubni_topish(486,84)

# DEF Funksiyasi qo'shimcha mashqlar'
# 1.
# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan
# yilini hisoblaydigan funksiya yozing.

def t_yilni_hisoblash(joriy_yil=2024):
    ism = input("Ismingizni kiriting:")
    yosh = int(input("Yoshingizni kiriting:"))
    print(f"{ism} {joriy_yil-yosh} -yil da tugilgan")
t_yilni_hisoblash()
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# 2.
# Foydalanuvchidan son olib, uning kvadrati va kubini
# konsolga chiqaruvchi funksiya yozing.

def kv_kubni_hisobla(son):
    print(f"{son} sonining kvadrati = {son**2} ga teng.")
    print(f"{son} sonining kubi = {son ** 3} ga teng.")
kv_kubni_hisobla(4)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# 3.
# Foydalanuvchidan son olib, son juft yoki
# toqligini konsolga chiqaruvchi funksiya yozing.
def toq_juft(son):
    if son%2 == 0:
        print(f"{son} juft son.")
    else:
        print(f"{son} toq son.")
toq_juft(5)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# 4.
# Foydalanuvchidan ikkita son olib, ulardan
# kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

def sonlarni_taqqosla(n,m):
    if n>m:
        print(f"{n} > {m}")
    elif n<m:
        print(f"{n} < {m}")
    else:
        print(f"{n} va {m} sonlari teng")
sonlarni_taqqosla(23,56)
sonlarni_taqqosla(54,54)
sonlarni_taqqosla(28,13)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# 5.
# Foydalanuvchidan x va y sonlarini olib, x ning y darajasini
 # konsolga chiqaruvchi funksiya yozing.

def daraja(x,y):
     print(f"{x} sonining {y} darajasi = {x ** y} ga teng")
daraja(12,14)
daraja(78,5)
daraja(5,3)
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# 6.
# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo('lgan sonlarga qoldiqsiz '
# bo')linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.

def bolinish(x):
    n = range(2,11)
    for i in n:
        if x%i == 0:
            print(f"{x} soni {i} soniga qoldiqsiz bo'linadi")
bolinish(90)
# ///////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
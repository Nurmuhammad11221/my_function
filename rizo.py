# def hello(name):
#     """ Foydalanuvchi ismni sorab unga salom beruvchi dastur """
#     print(f"HI {name}!")

# hello('John')
# hello('Doe')
# print(hello.__doc__)

# foydalanuvchidan otrtiq ism va familyasini sorovchi dastur

# def full_name(fname, lname):
#     print(f"Foydalanuvchi ismi: {fname.title()}\n"
#     f"Foydalanuvchi familasi: {lname.title()}")

# full_name('john', 'doe')


# def qoshish(num1, num2):
#     a = num1 + num2
#     print(f"{num1} + {num2} = {a}")

# qoshish(7, 8)

# def ayrish(num1, num2):
#     a = num1 - num2
#     print(f"{num1} - {num2} = {b}")

# ayrish(7, 8)


# def kopaytish(num1, num2):
#     a = num1 * num2
#     print(f"{num1} * {num2} = {d}")

# kopaytish(7, 8)


# def bolish(num1, num2):
#     a = num1 / num2
#     print(f"{num1} / {num2} = {q}")

# bolish(7, 8)

# def yosh_hisoblash(ism="John", yil=2000, hozirgi_yil=2024):
#     print(f"{ism} {hozirgi_yil - yil} da")
# yosh_hisoblash(yil=2000, hozirgi_yil=2024, ism="John")

# def yosh_hisoblash(ism="John", yosh=100000000000000000000000000000000000000000000000000000000000000000000000, hozirgi_yil=2024):
#     prin)t(f"{ism} {hozirgi_yil - yosh} tugilgan da")
# yosh_hisoblash(yosh=100000000000000000000000000000000000000000000000000000000000000000000000, hozirgi_yil=2024, ism="John")

# def hello(fname, lname):
#     print(f"Hello {fname} {lname}")
# hello('John', 'Doe')

# def calc(num1, num2):
#     a = num1 ** num2
#     print(f"{num1} ** {num2} = {a}")

# calc(7, 8)

# def kub(num1, num2):
#     a = {num1 ** 3} {num2 ** 3}
#     print(f"{num1} **    {num2} = {a}")

# kub(7, 8)

# def hisoblash(num1):
#     if num1 % 2 == 0:
#         print(f"{num1} juft son")
#     else:
#         print(f"{num1} toq son")
# hisoblash(8)


# 1

# def kattason(num1, num2):
#     if num1 > num2:
#         print(f"{num1}")
#     elif num2 > num1:
#         print(f"{num2}")
#     else:
#         print("teng")

# kattason(7, 10)

# # 2

# def daraja(x, y=2):
#     a = x ** y
#     print(f"{x} ning {y} darajasi: {a}")

# x = int(input("x ni kiriting: "))
# y = int(input("y ni kiriting: "))

# daraja(x)

# def bolinish_alomatlari(num):
#     for bolinish in range(2, 11):
#         if num % bolinish == 0:
#             print(f"{num} soni {bolinish} ga qoldiqsiz bolinadi")
# num = int(input("istalgan soni kriting: "))
# bolinish_alomatlari(num)



    

# def toliq_ism_yasa(ism, familasi):
#     """ toliq ism qaytaruvchi dastur """
    
#     toliq_ism = f"{ism} {familasi}"
#     return toliq_ism


# talaba1 = toliq_ism_yasa("Jonh", "Doe")
# talaba2 = toliq_ism_yasa("Abzal", "Abzal")
# talaba3 = toliq_ism_yasa("Jora", "Jora")


# print(toliq_ism_yasa.__doc__)
# print(f"Darsga kelmagan talaba {talaba1}, {talaba2}, {talaba3}")     


# def avto_info(kompaniya, model, rangi, karobka, yili, narxi=None):
#     avto = {
#         'kompaniya': kompaniya,
#         'model': model,
#         'rangli': rangi,
#         'karobka': karobka,
#         'yili': yili,
#         'narx': narxi,
#     }
#     return avto

# car = avto_info("GM", "Genetra", "Qora", "Avtomat", 2023, 17_000)
# print(car)

# def about(ismi, familasi, tugilgan_yili, tugilgan_joy, email_manzili, tel_raqam):
#     yosh = 2024 - tugilgan_yili
#     malumot = {
#         'ismi': ismi,
#         'familasi': familasi,
#         'tugilgan_yili': tugilgan_yili,
#         'yosh': yosh,
#         'tugilgan_joy':  tugilgan_joy,
#         'email_manzili': email_manzili,
#         'tel_raqam': tel_raqam,
#     }
#     return malumot

# odam = about(f"John", "Doe", 2010, "Toshkent", "emailemail@gmail.com", 917987700)
# print(odam) 



# 2



# 3

def kata(a, b, c):
    return max(a, b, c)

num1 = input("Birinchi sonni kiriting: ")
num2 = input("Ikkinchi sonni kiriting: ")
num3 = input("Uchinchi sonni kiriting: ")

orasida_kotasi = kata(num1, num2, num3)

print(f"{orasida_kotasi}")





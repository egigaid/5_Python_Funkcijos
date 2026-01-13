import random
# pamoka apie funkcijas

import time


def say_hi(): # nieko nepriima ir nieko negrazina
    print("hi")

say_hi()
say_hi()
say_hi()


def say_hi_to(name):#priima kintamaji, nieko negrazina
    print(f'hi {name}')


say_hi_to('Jonas')
say_hi_to('Naglis')
vardas = "Viktoras"
say_hi_to(vardas)


def sim_pi():# nieko nepriima, grazina reiksme
    return 3.1415

var = sim_pi()
print(var)

print(sim_pi())


def sumavimas(a, b):#priima du kintamuosius, grazina reiksme
    return a + b

print(sumavimas(4,48))
print( sum([4,48]) )


print(time.time())


def make_initials(name,surname):
    return (name[0] + surname[0]).upper()

initials = make_initials('Jonas', 'Jablonskis')
print(initials)


def make_initials_v2(text):
    pts = text.split()
    init = ""
    for pt in pts:
        init += pt[0]
    return init.upper()

res = make_initials_v2("Anzelmas Aluizas Mikalojus Konstantinas")
print(res)





def calc_age(birth_year = 2026):
    return 2026 - birth_year


print(calc_age(2002))
print(calc_age(1994))
print(calc_age())


def print_info(name = "", surname = "", birth_year = 0):
    print("mano vardas",name,"pavarde",surname,"gimimo metai",birth_year)

print_info('Naglis', 'Mockevicius',1998)
print_info('Naglis', 'Mockevicius')
print_info('Naglis', 1998)
print_info('Naglis', birth_year=1998)
print_info(name='Naglis', surname='Mockevicius',birth_year=1998)





print(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, sep=" :) ", end=" ?")
print()


weirdo = "Anzelmas Aluizas Mikalojus Konstantinas"
print(weirdo.split())
print(weirdo.split("a"))
print(weirdo.split(sep="a"))
print(weirdo.split(sep="a", maxsplit=3))


# 1. Sukurkite Funkciją kuri priima du kintamuosius, skaičius. Juos susumuoja ir atspausdina.
print("---- 1. Uzdavinys ----------------")

def sumavimas(a, b):            #priima du kintamuosius, grazina reiksme
    print(a + b)

sumavimas(4,5)
sumavimas(10, 20)

# 2. Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.
print("---- 2. Uzdavinys ----------------")

def PISq():
    return 9.8596

print(PISq())

# 3.Sukurkite Funkciją kuri priima du kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.
print("---- 3. Uzdavinys ----------------")

def sandauga(a, b):            #priima du kintamuosius, grazina reiksme
    return a * b
print(sandauga(4,5))
print(sandauga(10,10))

# 4.Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.
print("---- 4. Uzdavinys ----------------")

def print_masyvas(masyvas):
    for i in masyvas:
        print(i, end=" ")
    print()

numbers = [1, 2, 3, 5, 6, 7, 8, 9, 10]
print_masyvas(numbers)

numbers = [5, 10, 15, 25]
print_masyvas(numbers)

# 5.Sukurkite Funkciją kuri sugeneruotų random skaičių masyvą ir jį gražintų.
# Funkcija priima tris kintamuosius, min, max ir length reikšmėms nustatyti.
print("---- 5. Uzdavinys ----------------")

def random_masyvas(min, max,length):
    masyvas = []
    for i in range(length):
         masyvas.append(random.randint(min, max))
    return masyvas

sugeneruotas_masyvas = random_masyvas(1, 10, 5)
print(f'Sugeneruotas masyvas: {sugeneruotas_masyvas}')

# 6. Sukurkite Funkciją kuri panaudotų 5toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį),
# susumuotų ir gražintų reikšmę.
print("---- 6. Uzdavinys ----------------")

def random_masyvas(min, max,length):
    masyvas = []
    for i in range(length):
         masyvas.append(random.randint(min, max))
    return masyvas

sugeneruotas_masyvas = random_masyvas(1, 10, 5)
print(f'Sugeneruotas masyvas: {sugeneruotas_masyvas}')



def masyvo_suma(masyvas1):
    Isviso = sum(masyvas1)
    return Isviso

rezultatas = masyvo_suma(sugeneruotas_masyvas)
print(f'masyvo skaiciu suma: {rezultatas}')

# 7. Sukurkite Funkciją kuri priimtų 5toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį.
print("---- 7. Uzdavinys ----------------")

def masyvo_vidurkis(masyvas1):
    vidurkis = sum(masyvas1) / len(masyvas1)
    return vidurkis

rezultatas_vid = masyvo_vidurkis(sugeneruotas_masyvas)
print(f'masyvo skaiciu vidurkis: {rezultatas_vid}')


# 8. Sukurkite Funkciją kuri priimtų du skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis. Pirmas skaičius- išoriniam ciklui, antras vidiniam.
print("---- 8. Uzdavinys ----------------")


def staciakampis(aukstis, plotis):
    for x in range(aukstis):
        for y in range(plotis):
            print("* ", end="")
        print()
    print()

staciakampis1 = staciakampis(3,4)
staciakampis2 = staciakampis(5,8)

# 9. Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų.
# Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį) (simboliu yra 23, tarpu yra 3)
print("---- 9. Uzdavinys ----------------")


def tekstas(sakinys):
    simboliu_kiekis = len(sakinys)
    tarpai = 0
    for i in sakinys:
        if i == " ":
            tarpai += 1
    simboliu = len(sakinys) - tarpai
    print(sakinys)
    print(f'Tekste yra simboliu: {simboliu}. Tarpu: {tarpai}')


sakinys = "Šiandien labai graži diena"
tekstas(sakinys)

sakinys = "Labas, mama"
tekstas(sakinys)

# 10. Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų. Kodavimas - sakinį apsukame iš kitos pusės.
# Pvz “Naglis” turi gautis “silgaN”.
print("---- 10. Uzdavinys ----------------")


def koduotas(sakinys):
    for i in sakinys:
        kodas = sakinys[::-1]
    print(kodas)

sakinys = "Naglis"
koduotas(sakinys)

sakinys = "azuolas ir klevas"
koduotas(sakinys)

# 11. Sukurti funkciją, kuri apsuka tik žodžius. “Labas rytas” -> “sabaL satyr” ir atspausdina rezultatą
print("---- 11. Uzdavinys ----------------")

def apsukti_zodziai(sakinys):
    zodziai = sakinys.split()
    apsukti = []
    for zodis in zodziai:
        apverstas_zodis = zodis[::-1]
        apsukti.append(apverstas_zodis)
    return " ".join(apsukti)


sakinys = "Labas rytas"
print(sakinys)
rezultatas = apsukti_zodziai(sakinys)
print(rezultatas)

print('------- 2variantas')
def apsukti_zodziai(sakinys):
    zodziai = sakinys.split()
    apsukti = [zodis[::-1] for zodis in zodziai]
    return " ".join(apsukti)

sakinys = "Labas rytas"
print(sakinys)
rezultatas = apsukti_zodziai(sakinys)
print(rezultatas)

# 12. Sukurkite funkciją, kuri priimtų masyvą ir atspausdintų tik tuos elementus kurie yra skaičiai.
print("---- 12. Uzdavinys ----------------")

def tikskaiciai(masyvas):
    skaiciai = ""
    for i in masyvas:
        if i.isdigit():
            skaiciai += i
    return skaiciai

masyvas = "kaina 99 centai"
print(f'Pradinis masyvas: {masyvas}')
masyvo_skaiciai = tikskaiciai(masyvas)
print(masyvo_skaiciai)


masyvas = ("kaina", "99", "centai")
print(f'Pradinis masyvas: {masyvas}')
masyvo_skaiciai = tikskaiciai(masyvas)
print(masyvo_skaiciai)

# 13. Sukurkite funkciją, kuri priima masyvą ir atspausdina tik sveikuosius skaičius.
# (jei pavyks, patobulinkite, kad funkcija priimtų antrą parametrą True/False kuris nuspręstų ar
# spausdins tik sveikuosius skaičius ar skaičius su kableliu.
print("---- 13. Uzdavinys ----------------")

# 13. Sukurkite funkciją, kuri priima masyvą ir atspausdina tik sveikuosius skaičius.

def sveikiejisk(masyvas):
    kieksk = 0
    for i in masyvas:
        if type(i) is int:
            kieksk += 1
    return kieksk


masyvas = [1, 2.5, 3.5, 10, 5]
print(masyvas)
print(f"Sveikųjų skaičių yra: {sveikiejisk(masyvas)}")


def sveikiejisk2(masyvas):
    for i in masyvas:
        if type(i) is int:
            print(i, end=" ")
    print()

masyvas = [1, 2.5, 3.5, 10, 5]
sveikiejisk2(masyvas)

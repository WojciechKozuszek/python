# 1
""""
nazwa = input("Podaj slownie cyfre: ")

list = {"jeden":1, "dwa":2, "trzy":3, "cztery":4, "piec":5}

print(list[nazwa])
"""
# 2
""""
print("Podaj slownie cyfry do dodania")
liczba1 = input("Podaj pierwsza cyfre: ")
liczba2 = input("Podaj druga cyfre: ")

lista = {"jeden":1, "dwa":2, "trzy":3, "cztery":4, "piec":5}

suma = lista[liczba1] + lista[liczba2]
print(suma)
"""
# 3
""""
cyfra = int(input("Podaj cyfre: "))

list1 = {1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery", 5:"piec"}

print(list1[cyfra])
"""

# 4
""""
podaj = input("Podaj liczba 3-cyfrowa: ")

list2 = {1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery", 5:"piec", 6:"szesc", 7:"siedem", 8:"osiem", 9:"dziewiec"}

x1 = int(podaj[0])
x2 = int(podaj[1])
x3 = int(podaj[2])

print(list2[x1])
print(list2[x2])
print(list2[x3])
print(f"{list2[x1]} {list2[x2]} {list2[x3]}")

"""

# 5
# zbiory - set()

zbior = set()
zbior.add(5)
zbior.add(8)
zbior.add(5)
zbior.discard(5)
print(zbior)
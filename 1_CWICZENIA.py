# i="K"
# n="Olszewski"
# def foo(i, n):
# return i+"."+n
# print(foo(i, n))
#2 ZAD
#
# a="konrad"
# b="olszewski"
# def bruh(a, b): aa=a[0].capitalize() return aa+"."+b.capitalize()

# print(foo(a, b))
#3 ZAD
#
# def foo(r1,r2,l):
# rok=str(r1)+str(r2)
# data_ur=int(rok)-l
# return data_ur
# print(foo(20,22,21))
#4 ZAD
#
# def foo(imie,nazwisko,bruh):
# bruh(imie,nazwisko)
# print(foo("Konrad", "Olszewski"))
#5 ZAD
#
# def foo(a,b):
# if(b>0 and a>=0):
# return a/b
# print(foo(5,2))
#6 ZAD

# x=0
# while(x<100):
# a=int(input("podaj liczbe "))
# x= x + a
# print(x)
#7 ZAD

cars = ['Maluch', 'Garbus', 'Audi', 'Garbus']

# def foo(x):
#     w=tuple(x)
#     return w
#
# print(foo(cars))

#8 ZAD

# a=int(input("Ile pozycji chcesz dodać do krotki? "))
# cars=[]
# for i in range(a):
#     h=input(f"Podaj {i+1} pozycje")
#     cars.append(h)
#
# def foo(x):
#     w=tuple(x)
#     return w
#
# print(foo(cars))

#9 ZAD

# x=int(input("POdaj liczbe sobie"))
# x=x-1
# dni=["Poniedziałęk","Wtorek","Środa","Czwartek","Piątek","Sobota","Niedziela"]
#
# print(dni[x])


#10 ZAD

a=input("Wpisz sobie słowo  ")
l=len(a)

r = a[::-1]

print(a)

t="palindorm"

if a==r:
    print(t)
else:
    print("nie palindrom")

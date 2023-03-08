a = 'napis\ndrugi napis'
print(a)
b = 4
c = 4.5
print(b, c)
#liczby zespolone
d=3+4j
print(d)
e=b+c
print(e)
# dzielenie całkowite
f=b // c
print(f)
# modulo
g = c % b
print(g)
# potęgowanie
i=c**2
print(i)
#potegowanie
j = pow(5,2)
print(j)
# k=5**1/2
# n=pow(5,1/2)
print('b=b+2')
b+=2
print(b)
lista=['aB',2,4,5,[7,6,5],5.5]
print(lista[4])
lista.append(6.5) # takie push_back()
print(lista)
#dodawanie elementu na pozycje
lista.insert(4, 5.5)
print("dodawanie elementu na pozycje\n", lista)
#dodawanie kilku elementow na koniec listy
lista.extend([8,9,10])
print("dodawanie kilku elementow na koniec listy\n",lista)
#usuwanie elementu po indeksu
del lista[2]
print("usuwanie elementu po indeksu\n", lista)
#usuwanie elementu po wartosci elementu
lista.remove(5)
print("usuwanie elementu po wartosci elementu\n", lista)
#odwrocenie listy
lista.reverse()
print("odwrocenie listy\n", lista)
#sortowanie
listy=[1,4,6,8,2,3]
listy.sort()
print("sortowanie listy\n",listy)
print("slownik")
slownik = {'a': 1, 3: 1, 5:'b'}
print(slownik)
print(slownik['a'])

slownik['klucz'] = "wartosc"
print(slownik)
# usuwanie wierszy
slownik.pop('a')
print(slownik)
print(slownik.keys())
print(slownik.values())
# formatowanie
print('x=%(zm)d' % {'zm': 12})
print('a = {}, b={}'.format(12, 14))

#if warunek1
#   instrukcja1
#   instrukcja2
#elif warunek2
#   instrukcja1
#   instrukcja2
#else:
    #instrukcja1

a = input('Podaj a:')
b = input('Podaj b:')
print(a)
print(b)
# print(type(a))
# print(type(b))
a = int(a)
b = int(b)
# print(type(a))
# print(type(b))
if a>b:
    print('a = ' + str(a))
elif a<b:
    print('b = ' + str(b))
else:
    print('a rowne b')

c = input('Podaj c:')
d = input('Podaj d:')
print(c)
print(d)
c = int(c)
d = int(d)
if c==d:
    print('Liczby sa rowne')
else:
    print('Liczby nie sa rowne')

if (a>b) & (c>d):
    print('a większe od b i c większe od d')
else:
    print('Nie')

#for element in sekwencja:
    #instrukcja1
    #instrukcja2
#else:
    #instrukcja1
    #instrukcja2

for x in range(1,6,1):
    print(x)
else:
    print('Koniec pętli')
print('Wypisywanie')
for x in listy:
    print(x)
print('Wypisywanie')
for x in range(len(listy)): #to samo co u gory
    print(listy[x])
print('Wypisywanie od danego elementu')
for x in range(4,len(listy)):
    print(listy[x])

#while warunek:
#   instrukcja1
#   instrukcja2
#else:
#   instrukcja1
print('while')
licznik=0
while licznik !=len(listy):
    print(listy[licznik])
    licznik += 1

liczby = [3, 4, 5, 1, 7, 8, 5]
licznik = 0
a = int(input('Podaj a: '))
while licznik !=len(liczby):
    if a - liczby[licznik] ==0:
        print('{} - {} = 0'.format(a, liczby[licznik]))
        break
    licznik +=1
print('Usuwanie dwujek')
liczby1 = [ 1, 2, 2, 2, 2, 3]
licznik1=0
while licznik1 != len(liczby1):
    if liczby1[licznik1] == 2:
        liczby1.pop(licznik1)
    else:
        licznik1 += 1
for x in liczby1:
    print(x)
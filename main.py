# a="napis \n drugi napis"
# print(a)
# b=5
# c=5.5
# print(b,c)
# d=5+3j
# print(d)
# e=c+d
# print(e)
# f=c//b
# print(f)
# g=c%b
# print(g)
# h=b**b
# print(h)
# i=b**1/2
# j=pow(b,1/2)
# print(j)
# print(str(b)+'= b + 2')
# print(b)
# b+=2
# print(b)
# listy=[4,5,6,5.6]
# print(listy)
# listy.append(4)
# print(listy)
# hemoglobina=[3,24,6,8,69,69,241]
# #dodac element na wybrane miejsce
# listy.insert(3,4)
# #dodac kilka elementow
# listy.extend(hemoglobina)
# print(listy)
# #usunac element o danej pozycji
# listy.pop(1)
# print(listy)
# #usunac element o danej wartosci
# listy.remove(69)
# print(listy)
# #sortowanie
# listy.sort()
# print(listy)
# #odwracanie
# listy.reverse()
# print(listy)
# slownik={'a':2,1:2,4:'ab',1:3}
# print(slownik)
# print(slownik[4])
# slownik['klucz']='wartosc'
# print(slownik)
# slownik.pop('klucz')
# print(slownik)
# print(slownik.keys())
# print(slownik.values())
# print('a=%(zm)d'%{'zm':12})
# print('a={},b={}')
# #if warunek1 wcięcie
#     #instrukcja
#     #instrukcja2
# #elif warunek2:
#     #instrukcja1
#     #instrukcja2
# #else
#     #instrukcja1
# a=input('podaj a   ')
# b=input('podaj b   ')
# print(a)
# print(b)
# print(type(a))
# print(type(b))
# if a>b:
#     print(a)
# elif a<b:
#     print(b)
# else:
#     print('a równe b xd')
# c=input('c= ')
# d=input('d= ')
# if c==d:
#     print('są równe')
# if (a>b)&(c>d):
#     print('a większe od b i c większe od d')
#for element in sekwencja:
    #instrukcja 1
    #instrukcja 2
#else:
    #instrukcja 1
    #instrukcja 2
# for x in listy:
#     print(x)
# else:
#     print('koniec')
# for i in range(0,len(listy)):
#     a = listy[i]
#     print(a)
# licznik=0
# while licznik!=len(listy):
#     print(listy[licznik])
#     licznik+=1
liczby=[3,4,5,6,7,2,2,2,8,1,2]
# a=int(input('podaj a pajacu: '))
liczebnik=0
# while liczebnik!=len(liczby):
#     if(a-liczby[liczebnik]==0):
#         print('{}-{}=0'.format(a,liczby[liczebnik]))
#         break
#     liczebnik+=1
while liczebnik!=len(liczby):
    if liczby[liczebnik]==2:
        del liczby[liczebnik]
        liczebnik-=1
    liczebnik+=1
print(liczby)



a=[4,3,5,6,5,1,2] ## saraksts
a.append(8) ## добавление 8
a.append('ku') ## добавление ку
a.remove(5) ## удаление 5
print (a) ## вывод а
a[2]=10 ## вставляем 10 во второй элемент
del a[7] ##удаляет 7 элемент
print (a) ##
a.sort() ##
a.reverse() ## в порядке убывания
print (a) ##

b='computer' ##
print(b)


c=list(map(lambda x: x**2,a)) ##square kvadrat
print(c)

d=[3,5,3,5,8,8,8,3,8,7,3,5,]
print (d.count(5)) ##выводит кол-во пятерок

f=list(map(lambda x: x**0.5,c)) ##sqrt
print(f)

c.extend(f)
print(c)

a.extend(c)
print(a)
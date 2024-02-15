lst = [i for i in range(10)]

lst.append(44)

lst.sort(reverse=True)
print (lst)
lst.reverse()
print (lst)
print (lst.index(1))

m = lst.copy()
print (m)

m.insert(3, 333)
print (m)

n = [900, 1000, 1100]
lst.extend(n)
print (lst)
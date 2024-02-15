marks = [1,2,3,4,5,6,7,8,9,10,11,12]

print (marks)
print (len(marks))
print (marks[0:3])
print (marks[:3])
print (marks[1:-4])
print (marks[1:-2:3])

lst = [i*i for i in range(100)]
print (lst)

lst = [i*i for i in range(100) if i%2==0]
print (lst)

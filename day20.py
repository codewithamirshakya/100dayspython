def calculateGmean(a,b):
    print ((a*b)/(a+b))

def calculateGreater(a,b):
    if (a < b):
        print(b, "is greater")
    elif (a > b):
        print(a, "is greater")
    elif (a == b):
        print(a, "is eq")        

a = 9
b = 8

calculateGmean(a,b) # calculate
calculateGreater(a,b)
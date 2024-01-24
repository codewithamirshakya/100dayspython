def average (*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print("Average :: ", sum / len(numbers))    

average(1,2,23,3,66)    
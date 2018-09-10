# I want to figure out a way to detect straights

spam = [1,3,4,5,6,7,8]
counter = 0
for e in range(0,6):
    print(spam[e+1])
    print(e+1)
    if spam[e+1] == e + 1:
        counter +=1


print(counter)

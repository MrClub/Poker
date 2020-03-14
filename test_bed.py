def test_function(number_of_the_beast):
    if number_of_the_beast > 10:
        return [], "yes"
    else:
        return [666], "no"

spam, ham = test_function(11)
#print(spam,ham)

if not test_function(11):
    print("It works for the first variable")
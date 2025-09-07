
def Palindrome():
    number = 12321
    temp = number
    newnumber = 0
    while(temp > 0):
        rem = temp%10
        newnumber = newnumber * 10 + rem
        temp = temp//10

    print(newnumber)
    print(number)

    if (newnumber == number):
        print (f"The {number} is a Palindrome.")

Palindrome()

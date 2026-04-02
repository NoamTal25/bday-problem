
def bday(n):
    
    number_of_people = 0
    
    for i in range(n):
        num = 365
        for b in range(i):
            num = num * (365 - (b + 1))    
        number_of_people = number_of_people + 1
        chance_two_bdays = 1 - (num / (365 ** (i + 1)))
        print(number_of_people, "people:", chance_two_bdays)


bday(100)
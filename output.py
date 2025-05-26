from bank.manager import*
from bank.customer import*
while True:
    print("1.Manager login")
    print("2.Customer login")
    try:
        o=int(input("Enter your operation:"))
   
        if o==1:
            manager()
        elif o==2 :
            custo()
        else:
            print("Choose correct option.....!")
    except ValueError:
        print("Enter valid input......!")
        print("***************")
                      

#cname=input("Enter your username:")
#accno=int(input("Enter your accno:"))
def customer(accno,cname):
    try:
        with open("detail.txt","r") as file:
            f=file.read().split("\n")
            for i in f:
                t=i.split("\t")
                if str(accno)==t[0] and cname==(t[1]):
                    print("your login successfully")
    except FileNotFoundError:
        print("File Can't be find")
                 

def deposit(accno):
    try:
         eamt=int(input("Enter amount:"))
         with open("detail.txt","r") as file:
                f=file.read().strip().split("\n")
                with open("detail.txt","w") as file:
                    for i in f:
                      t=i.split("\t")
                      if int(t[0])==accno:
                          if eamt>=1:
                              amt=int(t[2])+eamt
                              t[2]=str(amt)
                              print("deposited successfully")
                              file.write("\t".join(t)+"\n")
                          else:
                               print("Minimum you can deposit 1 Rupee....!")
                                 
                      else:
                           file.write("\t".join(t)+"\n")
    except:
        print("Enter correct amount")
                          
               
def  withdraw(accno):
     try:
         eamt=int(input("Enter amount:"))
         with open("detail.txt","r") as file:
                f=file.read().strip().split("\n")
                with open("detail.txt","w") as file:
                    for i in f:
                      t=i.split("\t")
                      if int(t[0])==accno:
                          if eamt>=1:
                              amt=int(t[2])-eamt
                              t[2]=str(amt)
                              print("Withdraw successfully")
                              file.write("\t".join(t)+"\n")
                          else:
                               print("Minimum you can withdraw 1 Rupee....!")
                                
                      else:
                           file.write("\t".join(t)+"\n")
     except ValueError:
        print("Enter correct amount")

def balance(accno):
    try:
        with open("detail.txt","r") as file:
                f=file.read().strip().split("\n")
                for i in f:
                      t=i.split("\t")
                      if int(t[0])==accno:
                          print("Your balance is,")
                          print(int(t[2]))
    except FileNotFoundError:
        print("File can not be found....!")


                      
def custo():
    cname=input("Enter your username:")
    accno=int(input("Enter your accno:"))
    customer(accno,cname)
    print("1.deposit")
    print("2.withdraw")
    print("3.balance Enquery")
    try:
        n=int(input("Choose you operation"))
        if n==1:
             deposit(accno)
        elif n==2:
            withdraw(accno)
        elif n==3:
            balance(accno)
        else:
            print("Choose correct option")
    except ValueError:
        print("Enter valid input....!")

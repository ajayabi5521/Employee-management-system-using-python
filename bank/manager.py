def newcustomer():
    try:
        name=input("Enter customer name:")
        accno=int(input("Enter customer account no:"))
        amt=int(input("Enter customer inidial deposit amount:"))
        with open("detail.txt","a") as file:
                file.write(str(accno)+"\t"+name+"\t"+str(amt)+"\n")
                print("Customer added successfully")
    except ValueError:
        print("Enter correct values:")
def viewcustomerdetails():
    try:
        a="detail.txt"
        assert a=="detail.txt"
        with open("detail.txt","r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File can not be found")
def  editcustomerdetailsparticular():
     try:
         cid=int(input("Enter customer id:"))
         eamt=int(input("Enter amount:"))
         with open("detail.txt","r") as file:
                f=file.read().strip().split("\n")
                with open("detail.txt","w") as file:
                    for i in f:
                      t=i.split("\t")
                      if int(t[0])==cid:
                          amt=int(t[2])+eamt
                          t[2]=str(amt)
                          print("updated successfully")
                          file.write("\t".join(t)+"\n")
                      else:
                             file.write("\t".join(t)+"\n")
     except ValueError:
         print("Enter correct values")
               
def manager():
    uname=input("ENTER USERNAME:")
    password=input("ENTER PASSWORD:")
    if uname=="admin" and password=="admin":
        i=1
        while i==1:
            print("-----------------------Welcome to manager login----------------------")
            print("1.Add new customer")
            print("2.View customer details")
            print("3.Edit customer details ")
            n=int(input("Enter your operation  Mr.Admin:"))
            if n==1:
                newcustomer()
            elif n==2:
                viewcustomerdetails()
            elif n==3:
                editcustomerdetailsparticular()
            else:
                print("choose correct opeeration ....1")

            i=int(input("Are you continue press 1.Otherwire press any key"))    
            
    else:
        print("username or password incorrect")


      

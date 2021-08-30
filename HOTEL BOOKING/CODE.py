import csv
class hot:
    def f1():
        a=[];
        a.append(input("ENTER THE NAME : "))
        a.append(input("ENTER THE CONTACT NUM : "))
        a.append(input("ENTER THE ADDRESS : "))
        a.append(input("ENTER THE CHECK IN DATE : "))
        a.append(input("ENTER THE CHECK OUT DATE : "))
        a.append(input("ENTER THE PRICE OF THE ROOM /day : "))
        with open('FILE.csv', mode='a') as csv_file:   
            csvwriter = csv.writer(csv_file)
            csvwriter.writerow(a);
    def f2():
        x=input("ENTER THE CONTACT NO : ")
        csv_file = csv.reader(open('FILE.csv', "r"), delimiter=",")
        a=[];
        c=1;
        for row in csv_file:
            if x == row[1]:
                a.append(row[0]);
                a.append(row[1])
                a.append(row[2])
                a.append(input("ENTER THE CHECK IN DATE : "))
                a.append(input("ENTER THE CHECK OUT DATE : "))
                a.append(input("ENTER THE PRICE OF THE ROOM /day : "))
                c=0;
                break;
            else:
                c=1
        if c==1:
            print("NO DETAILS FOUND PLZ ENTER CORRECT CONTACT NUM")
        with open('FILE.csv', mode='a') as csv_file: 
            csvwriter = csv.writer(csv_file)
            csvwriter.writerow(a);
    def f3():
        x=input("ENTER THE CONTACT NO : ")
        csv_file = csv.reader(open('FILE.csv', "r"), delimiter=",")
        z=[];
        c=1;
        y=0;
        cf=list(csv_file)
        for row in reversed(cf):
            if x == row[1]:  
                z=row
                from datetime import datetime
                date_format = "%m/%d/%Y"
                a = datetime.strptime(row[3], date_format)
                b = datetime.strptime(row[4], date_format)
                y= (b - a).days
                c=0;
                break
            else:
                c=1
        if c==1:
            print("NO DETAILS FOUND PLZ ENTER CORRECT CONTACT NUM")
        else:
            print("BILL :-")
            print("----------------------------------------")
            print("NAME           : ",z[0])  
            print("PH_NO          : ",z[1])
            print("ADDRESS        : ",z[2])
            print("CHECK IN DATE  : ",z[3])
            print("CHECK OUT DATE : ",z[4])
            print("TOTAL AMOUNT   : ",(int(z[5])*y))
            print("----------------------------------------")

if __name__ == "__main__":
    opt=True;
    while opt:
        print("OPTIONS :-\n\t1)BOOKING\n\t2)BILLING\nPRESS ENTER TO EXIT");
        opt=input("ENTER UR CHOICE : ");
        if opt=="1":
            opt1=True;
            while opt1:
                print("OPTIONS :-\n\t1)NEW CUSTOMER\n\t2)OLD CUSTOMER\nPRESS ENTER TO GO BACK TO THE MAIN MENU")
                opt1=input("ENTER UR CHOICE : ");
                if opt1=="1":
                    hot.f1();
                elif opt1=="2":
                    hot.f2();
                elif opt1=="":
                    print();
        elif opt=="2":
            hot.f3();
        elif opt=="":
            print();
        
        
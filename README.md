opt=True;
ar=[];
while opt:
    print("1)ARIHMETIC CALCULATOR\n2)BITWISE CALCULATOR\n3)HISTORY\nPRESS ENTER TO EXIT");
    opt=input("ENTER YOUR CHOICE : ");
    if opt=="1":
        opt1=True;
        while opt1:
            print("1)SUM\n2)SUBTRACT\n3)MUNTIPLY\n4)DIVIDE\nPRESS ENTER FOR GOING BACK TO MAIN MENU");
            opt1=input("ENTER YOUR CHOICE :");
            if opt1=="1":
                x=int(input("ENTER THE 1ST NUM :"));
                y=int(input("ENTER THE 2ST NUM :"));
                k=x+y;
                print("SUM = ",k);
                ar.append((str(x)+" + "+str(y)+" = "+str(k)));
            elif opt1=="2":
                x=int(input("ENTER THE 1ST NUM :"));
                y=int(input("ENTER THE 2ST NUM :"));
                k=x-y;
                print("DIFFECENCE = ",k);
                ar.append((str(x)+" - "+str(y)+" = "+str(k)));
            elif opt1=="3":
                x=int(input("ENTER THE 1ST NUM :"));
                y=int(input("ENTER THE 2ST NUM :"));
                k=x*y;
                print("PRODUCT = ",k);
                ar.append((str(x)+" X "+str(y)+" = "+str(k)));
            elif opt1=="4":
                x=int(input("ENTER THE 1ST NUM :"));
                y=int(input("ENTER THE 2ST NUM :"));
                k=x/y;
                print("QUCIENT = ",k);
                ar.append((str(x)+" / "+str(y)+" = "+str(k)));
            elif opt!="":
                print("");
    elif opt=="2":
        opt1=True;
        while opt1:
            print("1)BITWISE AND\n2)BITWISE OR \n3)BITWISE XOR\n4)BITWISE LEFT SHIFT\n5)BITWISE RIGHT SHIFT\nPRESS ENTER FOR GOING BACK TO MAIN MENU");
            opt1=input("ENTER YOUR CHOICE :");
            if opt1=="1":
                x=int(input("ENTER THE 1ST NUM :"));
                y=int(input("ENTER THE 2ST NUM :"));
                k=x&y;
                print("AND = ",k);
                ar.append((str(x)+" & "+str(y)+" = "+str(k)));
            elif opt1=="2":
                x=int(input("ENTER THE 1ST NUM :"));
                y=int(input("ENTER THE 2ST NUM :"));
                k=x|y;
                print("OR = ",k);
                ar.append((str(x)+" | "+str(y)+" = "+str(k)));
            elif opt1=="3":
                x=int(input("ENTER THE 1ST NUM :"));
                y=int(input("ENTER THE 2ST NUM :"));
                k=x^y;
                print("XOR = ",k);
                ar.append((str(x)+" ^ "+str(y)+" = "+str(k)));
            elif opt1=="4":
                x=int(input("ENTER THE 1ST NUM :"));
                y=int(input("ENTER LEFT SHIFT POSITION :"));
                k=x<<y;
                print("LEFT SHIFT = ",k);
                ar.append((str(x)+" << "+str(y)+" = "+str(k)));
            elif opt1=="5":
                x=int(input("ENTER THE 1ST NUM :"));
                y=int(input("ENTER RIGHT SHIFT POSITION :"));
                k=x>>y;
                print("RIGHT SHIFT = ",k);
                ar.append((str(x)+" >> "+str(y)+" = "+str(k)));
            elif opt!="":
                print("INVALID CHOICE");
    elif opt=="3":
        print("HISTORY");
        for i in ar:
            print(i);
    elif opt!="":
        print("");

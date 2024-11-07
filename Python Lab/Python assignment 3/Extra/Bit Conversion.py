def DecToBin(d):
    b = 0
    m = 1
    while d>0:
        b = b + ((d%2)*m)
        m = m*10
        d = int(d/2)
    return b

def DecToOct(d):
    b = 0
    m = 1
    while d>0:
        b = b + ((d%8)*m)
        m = m*10
        d = int(d/8)
    return b

def DecToHex(dnum):
    i = 0
    hnumlist = []
    while dnum!=0:
        rem = dnum % 16
        if rem<10:
            rem = rem+48
        else:
            rem = rem+55
        hnumlist.insert(i, chr(rem))
        i = i+1
        dnum = int(dnum / 16)
    return hnumlist

def BinToDec(bnum):
    dnum = 0
    i = 1
    while bnum!=0:
        rem = bnum%10
        dnum = dnum + (rem*i)
        i = i*2
        bnum = int(bnum/10)
    return dnum

def BinToOct(bnum):
    octaldigit = 0
    octalnum = []
    i = 0
    mul = 1
    chk = 1
    while bnum!=0:
        rem = bnum % 10
        octaldigit = octaldigit + (rem * mul)
        if chk%3==0:
            octalnum.insert(i, octaldigit)
            mul = 1
            octaldigit = 0
            chk = 1
            i = i+1
        else:
            mul = mul*2
            chk = chk+1
        bnum = int(bnum / 10)
    if chk!=1:
        octalnum.insert(i, octaldigit)
    
    return octalnum

def BinToHex(bnum):
    hex = 0
    mul = 1
    chk = 1
    i = 0
    hnumlist = []
    while bnum!=0:
        rem = bnum%10
        hex = hex + (rem*mul)
        if chk%4==0:
            if hex<10:
                hex = hex+48
                val = chr(hex)
                hnumlist.insert(i, val)
            else:
                hex = hex+55
                val = chr(hex)
                hnumlist.insert(i, val)
            mul = 1
            hex = 0
            chk = 1
            i = i+1
        else:
            mul = mul*2
            chk = chk+1
        bnum = int(bnum/10)

    if chk!=1:
        hex = hex+48
        val = chr(hex)
        hnumlist.insert(i, val)
    if chk==1:
        i = i-1
    return hnumlist

print("\nWelcome to Menu Driven Program for conversion\n")
print("What Operation do you like to perform :-")

while(True):
    print("\nPress 1 for Decimal to Binary conversion.")
    print("Press 2 for Decimal to Octal conversion.")
    print("Press 3 for Decimal to Hexadecimal conversion.")
    print("Press 4 for Binary to Decimal conversion.")
    print("Press 5 for Binary to Octal conversion.")
    print("Press 6 for Binary to Hexadecimal conversion.")
    print("Press 7 to exit.\n")

    try:
        choice = int(input("\nEnter your choice : "))
    except:
        print("\nWARNING :- Please enter a valid numeric value. Thank you.")
    else: 
        if choice == 1:
            print("\nProgram for Decimal to Binary conversion.\n")
            dnum = int(input("Enter a Decimal Number : "))

            bnum = DecToBin(dnum)
            print("\nEquivalent Binary Value = ", bnum)

        elif choice == 2:
            print("\nProgram for Decimal to Octal conversion..\n")
            dnum = int(input("Enter a Decimal Number : "))

            onum = DecToOct(dnum)
            print("\nEquivalent Octal Value = ", onum)

        elif choice == 3:
            print("\nProgram for Decimal to Hexadecimal conversion.\n")
            dnum = int(input("Enter a Decimal Number : "))

            hnum = DecToHex(dnum)
            print("\nEquivalent Hexadecimal Value = ", end="")
            i=len(hnum)
            i=i-1
            while i>=0:
                print(end=hnum[i])
                i = i-1
            print()

        elif choice == 4:
            print("\nProgram for Binary to Decimal conversion.\n")
            bnum = int(input("Enter a Binary Number : "))
            
            dnum = BinToDec(bnum)
            print("\nEquivalent Decimal Value = ", dnum)

        elif choice == 5:
            print("\nProgram for Binary to Octal conversion.\n")
            bnum = int(input("Enter a Binary Number : "))

            onumlist = BinToOct(bnum)
            print("\nEquivalent Octal Value = ", end="")
            i=len(onumlist)
            i=i-1
            while i>=0:
                print(onumlist[i],end="")
                i = i-1
            print()

        elif choice == 6:
            print("\nProgram for Binary to Hexadecimal conversion.\n")
            bnum = int(input("Enter a Binary Number : "))

            hnumlist = BinToHex(bnum)
            print("\nEquivalent Hexadecimal Value = ", end="")
            i=len(hnumlist)
            i=i-1
            while i>=0:
                print(hnumlist[i],end="")
                i = i-1
            print()

        elif choice == 7:
            print("\nThanks for using this program.\nPlease Come back soon......\n")
            break

        else:
            print("\nERROR :- Invalid User Input.Please choose a Valid Option.")

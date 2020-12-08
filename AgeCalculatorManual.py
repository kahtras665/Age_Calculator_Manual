name= input("Enter your name: ")
print("Hello",name,"thank you for using our Time Calculator Python Program! This program tells you your age and the number of days you have lived.")
print("Let's start the process! Follow the instructions and the heads-up messages carefully for the best results! Good Luck!")
st= input("Press any key to start: ")
print()
print("Enter Birth Date.")
dateBirth= int(input("Enter Date: "))
monthBirth= int(input("Enter Month: "))
yearBirth= int(input("Enter Year: "))
if dateBirth>31:
    dateBirth= int(input("Wrong Input! Re-Enter date correctly: "))
if monthBirth>12:
    monthBirth= int(input("Wrong Input! Re-Enter month correctly: "))
if yearBirth>2020:
    yearBirth= int(input("Wrong Input! Re-Enter year correctly: "))
if yearBirth%4!=0:  #not a leap year
    if dateBirth>28 and monthBirth==2:
        dateBirth= int(input("Wrong Input! Re-Enter date correctly: "))
if yearBirth%4==0:  #leap year
    if dateBirth>29 and monthBirth==2:
        dateBirth= int(input("Wrong Input! Re-Enter date correctly: "))
if monthBirth==4 or monthBirth==6 or monthBirth==9 or monthBirth==11:
    if dateBirth>30:
        dateBirth= int(input("Wrong Input! Re-Enter date correctly: "))
print()
print("Enter Today's Date.")
dateCurrent= int(input("Enter Date: "))
monthCurrent= int(input("Enter Month: "))
yearCurrent= int(input("Enter Year: "))
if dateCurrent>31:
    dateCurrent= int(input("Wrong Input! Re-Enter date correctly: "))
if monthCurrent>12:
    monthCurrent= int(input("Wrong Input! Re-Enter month correctly: "))
if yearCurrent>2020:
    yearCurrent= int(input("Wrong Input! Re-Enter year correctly: "))
if yearCurrent%4!=0:  #not a leap year
    if dateCurrent>28 and monthCurrent==2:
        dateCurrent= int(input("Wrong Input! Re-Enter date correctly: "))
if yearCurrent%4==0:  #leap year
    if dateCurrent>29 and monthCurrent==2:
        dateCurrent= int(input("Wrong Input! Re-Enter date correctly: "))
if monthCurrent==4 or monthCurrent==6 or monthCurrent==9 or monthCurrent==11:
    if dateCurrent>30:
        dateCurrent= int(input("Wrong Input! Re-Enter date correctly: "))
# line numbers 48 to 57 were added later on
if yearBirth>yearCurrent:
    print("Wrong Input! year of birth cannot be greater than this year.")
    yearBirth= int(input("Re-Enter Year of Birth: "))
if yearBirth==yearCurrent and monthBirth==monthCurrent:
    if dateBirth>dateCurrent:
        print("Wrong Input! Birth Date cannot be greater than Today's Date.")
        print("Re-Enter information regarding Birth Date.")
        dateBirth= int(input("Enter Date: "))
        monthBirth= int(input("Enter Month: "))
        yearBirth= int(input("Enter Year: "))
print()
print("Your Birthday is: ",dateBirth,"/",monthBirth,"/",yearBirth)
print("Today's date is: ",dateCurrent,"/",monthCurrent,"/",yearCurrent)
chan= input("Do you want to make any changes to the any of the dates mentioned above? Y/N: ")
if chan!="Y" and chan!="y" and chan!="N" and chan!="n":
    chan= input("Follow the instructions carefully (Re-enter either Y or N): ")
if chan=="Y" or chan=="y":
    print()
    print("You chose to make changes to the date.")
    chang= input("Enter 'B' to make changes to the Birthdate or Enter 'T' to make changes to Today's date or Enter 'A' to make changes to both Birthdate and Today's date: ")
    if chang=="B" or chang=="b":
        print()
        print("Re-Enter Birth Date.")
        dateBirth= int(input("Enter Date: "))
        monthBirth= int(input("Enter Month: "))
        yearBirth= int(input("Enter Year: "))
        if dateBirth>31:
            dateBirth= int(input("Wrong Input! Re-Enter date correctly: "))
        if monthBirth>12:
            monthBirth= int(input("Wrong Input! Re-Enter month correctly: "))
        if yearBirth>2020:
            yearBirth= int(input("Wrong Input! Re-Enter year correctly: "))
        if yearBirth%4!=0:  #not a leap year
            if dateBirth>28 and monthBirth==2:
                dateBirth= int(input("Wrong Input! Re-Enter date correctly: "))
        if yearBirth%4==0:  #leap year
            if dateBirth>29 and monthBirth==2:
                dateBirth= int(input("Wrong Input! Re-Enter date correctly: "))
        if monthBirth==4 or monthBirth==6 or monthBirth==9 or monthBirth==11:
            if dateBirth>30:
                dateBirth= int(input("Wrong Input! Re-Enter date correctly: "))
    if chang=="T" or chang=="t":
        print()
        print("Re-Enter Today's Date.")
        dateCurrent= int(input("Enter Date: "))
        monthCurrent= int(input("Enter Month: "))
        yearCurrent= int(input("Enter Year: "))
        if dateCurrent>31:
            dateCurrent= int(input("Wrong Input! Re-Enter date correctly: "))
        if monthCurrent>12:
            monthCurrent= int(input("Wrong Input! Re-Enter month correctly: "))
        if yearCurrent>2020:
            yearCurrent= int(input("Wrong Input! Re-Enter year correctly: "))
        if yearCurrent%4!=0:  #not a leap year
            if dateCurrent>28 and monthCurrent==2:
                dateCurrent= int(input("Wrong Input! Re-Enter date correctly: "))
        if yearCurrent%4==0:  #leap year
            if dateCurrent>29 and monthCurrent==2:
                dateCurrent= int(input("Wrong Input! Re-Enter date correctly: "))
        if monthCurrent==4 or monthCurrent==6 or monthCurrent==9 or monthCurrent==11:
            if dateCurrent>30:
                dateCurrent= int(input("Wrong Input! Re-Enter date correctly: "))
    if chang=="A" or chang=="a":
        print()
        print("Re-Enter Birth Date.")
        dateBirth= int(input("Enter Date: "))
        monthBirth= int(input("Enter Month: "))
        yearBirth= int(input("Enter Year: "))
        if dateBirth>31:
            dateBirth= int(input("Wrong Input! Re-Enter date correctly: "))
        if monthBirth>12:
            monthBirth= int(input("Wrong Input! Re-Enter month correctly: "))
        if yearBirth>2020:
            yearBirth= int(input("Wrong Input! Re-Enter year correctly: "))
        if yearBirth%4!=0:  #not a leap year
            if dateBirth>28 and monthBirth==2:
                dateBirth= int(input("Wrong Input! Re-Enter date correctly: "))
        if yearBirth%4==0:  #leap year
            if dateBirth>29 and monthBirth==2:
                dateBirth= int(input("Wrong Input! Re-Enter date correctly: "))
        if monthBirth==4 or monthBirth==6 or monthBirth==9 or monthBirth==11:
            if dateBirth>30:
                dateBirth= int(input("Wrong Input! Re-Enter date correctly: "))
        print()
        print("Re-Enter Today's Date.")
        dateCurrent= int(input("Enter Date: "))
        monthCurrent= int(input("Enter Month: "))
        yearCurrent= int(input("Enter Year: "))
        if dateCurrent>31:
            dateCurrent= int(input("Wrong Input! Re-Enter date correctly: "))
        if monthCurrent>12:
            monthCurrent= int(input("Wrong Input! Re-Enter month correctly: "))
        if yearCurrent>2020:
            yearCurrent= int(input("Wrong Input! Re-Enter year correctly: "))
        if yearCurrent%4!=0:  #not a leap year
            if dateCurrent>28 and monthCurrent==2:
                dateCurrent= int(input("Wrong Input! Re-Enter date correctly: "))
        if yearCurrent%4==0:  #leap year
            if dateCurrent>29 and monthCurrent==2:
                dateCurrent= int(input("Wrong Input! Re-Enter date correctly: "))
        if monthCurrent==4 or monthCurrent==6 or monthCurrent==9 or monthCurrent==11:
            if dateCurrent>30:
                dateCurrent= int(input("Wrong Input! Re-Enter date correctly: "))
tnod=0
for i in range(yearBirth,yearCurrent+1):
    nod=0
    if i==yearBirth and yearBirth%4!=0:
        if monthBirth==1:
            nod= (31-dateBirth) + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        if monthBirth==2:
            nod= (28-dateBirth) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        if monthBirth==3:
            nod= (31-dateBirth) + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        if monthBirth==4:
            nod= (30-dateBirth) + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        if monthBirth==5:
            nod= (31-dateBirth) + 30 + 31 + 31 + 30 + 31 + 30 + 31
        if monthBirth==6:
            nod= (30-dateBirth) + 31 + 31 + 30 + 31 + 30 + 31
        if monthBirth==7:
            nod= (31-dateBirth) + 31 + 30 + 31 + 30 + 31
        if monthBirth==8:
            nod= (31-dateBirth) + 30 + 31 + 30 + 31
        if monthBirth==9:
            nod= (30-dateBirth) + 31 + 30 + 31
        if monthBirth==10:
            nod= (31-dateBirth) + 30 + 31
        if monthBirth==11:
            nod= (30-dateBirth) + 31
        if monthBirth==12:
            nod= (31-dateBirth)
    if i==yearBirth and yearBirth==0:
        if monthBirth==1:
            nod= (31-dateBirth) + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        if monthBirth==2:
            nod= (29-dateBirth) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        if monthBirth==3:
            nod= (31-dateBirth) + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        if monthBirth==4:
            nod= (30-dateBirth) + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31
        if monthBirth==5:
            nod= (31-dateBirth) + 30 + 31 + 31 + 30 + 31 + 30 + 31
        if monthBirth==6:
            nod= (30-dateBirth) + 31 + 31 + 30 + 31 + 30 + 31
        if monthBirth==7:
            nod= (31-dateBirth) + 31 + 30 + 31 + 30 + 31
        if monthBirth==8:
            nod= (31-dateBirth) + 30 + 31 + 30 + 31
        if monthBirth==9:
            nod= (30-dateBirth) + 31 + 30 + 31
        if monthBirth==10:
            nod= (31-dateBirth) + 30 + 31
        if monthBirth==11:
            nod= (30-dateBirth) + 31
        if monthBirth==12:
            nod= (31-dateBirth)
    if i!=yearBirth and i!=yearCurrent:
        if i%4!=0:
            nod= 365
        if i%4==0:
            nod= 366
    if i==yearCurrent and yearCurrent%4!=0:
        if monthCurrent==1:
            nod= nod + dateCurrent
        if monthCurrent==2:
            nod= nod + 31 + dateCurrent
        if monthCurrent==3:
            nod= nod + 31 + 28 + dateCurrent
        if monthCurrent==4:
            nod= nod + 31 + 28 + 31 + dateCurrent
        if monthCurrent==5:
            nod= nod + 31 + 28 + 31 + 30 + dateCurrent
        if monthCurrent==6:
            nod= nod + 31 + 28 + 31 + 30 + 31 + dateCurrent
        if monthCurrent==7:
            nod= nod + 31 + 28 + 31 + 30 + 31 + 30 + dateCurrent
        if monthCurrent==8:
            nod= nod + 31 + 28 + 31 + 30 + 31 + 30 + 31 + dateCurrent
        if monthCurrent==9:
            nod= nod + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + dateCurrent
        if monthCurrent==10:
            nod= nod + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + dateCurrent
        if monthCurrent==11:
            nod= nod + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + dateCurrent
        if monthCurrent==12:
            nod= nod + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dateCurrent
    if i==yearCurrent and yearCurrent%4==0:
        if monthCurrent==1:
            nod= nod + dateCurrent
        if monthCurrent==2:
            nod= nod + 31 + dateCurrent
        if monthCurrent==3:
            nod= nod + 31 + 29 + dateCurrent
        if monthCurrent==4:
            nod= nod + 31 + 29 + 31 + dateCurrent
        if monthCurrent==5:
            nod= nod + 31 + 29 + 31 + 30 + dateCurrent
        if monthCurrent==6:
            nod= nod + 31 + 29 + 31 + 30 + 31 + dateCurrent
        if monthCurrent==7:
            nod= nod + 31 + 29 + 31 + 30 + 31 + 30 + dateCurrent
        if monthCurrent==8:
            nod= nod + 31 + 29 + 31 + 30 + 31 + 30 + 31 + dateCurrent
        if monthCurrent==9:
            nod= nod + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + dateCurrent
        if monthCurrent==10:
            nod= nod + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + dateCurrent
        if monthCurrent==11:
            nod= nod + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + dateCurrent
        if monthCurrent==12:
            nod= nod + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dateCurrent
    tnod= tnod + nod
print()
fin= input("Do you want to know the total number of days since you are living? Y/N: ")
if fin!="Y" and fin!="y" and fin!="N" and fin!="n":
    fin= input("Follow the instructions carefully (Re-enter either Y or N): ")
if fin=="Y" or fin=="y":
    print("So, you have been living since",tnod,"days",name)
if fin=="N" or fin=="N":
    print("Ok then :(  I thought you were excited to know!")
ye= tnod/365
year= int(ye)
m1= tnod/30.41
m2= int(m1)
month= m2-(year*12)
print()
fin1= input("Do you want to know your age? Y/N: ")
if fin!="Y" and fin1!="y" and fin1!="n" and fin1!="n":
    fin1= input("Follow the instructions carefully (Re-enter either Y or N): ")
if fin1=="Y" or fin1=="y":
    print("You are",year,"years and",month,"months old.")
if fin1=="N" or fin1=="n":
    print("Ok then :( ")
print()
nxtB= input("Do you want to know the number of days left for your next birthday: Y/N? ")
if nxtB!="Y" and nxtB!="y" and nxtB!="n" and nxtB!="n":
    nxtB= input("Follow the instructions carefully (Re-enter either Y or N): ")
if nxtB=="Y" or nxtB=="y":
    if monthCurrent<monthBirth:
        for k in range(monthCurrent, monthBirth+1):
            if k==monthCurrent:
                if monthCurrent==4 or monthCurrent==6 or monthCurrent==9 or monthCurrent==11:
                    res= 30-dateCurrent 
                if monthCurrent==1 or monthCurrent==3 or monthCurrent==5 or monthCurrent==7 or monthCurrent==8 or monthCurrent==10 or monthCurrent==12:
                    res= 31-dateCurrent 
                if monthCurrent==2:
                    res= 28-dateBirth 
            if k==monthBirth:
                res= dateBirth-1
            if k!=monthCurrent && k!=monthBirth:
                if k==4 or k==6 or k==9 or k==11:
                    res=30
                if k==1 or k==3 or k==5 or k==7 or k==8 or k==10 or k==12:
                    res=31
                if k==2:
                    res=28
            bd+=res
    if monthCurrent>monthBirth:
        for l in range(monthCurrent, 13):
            if l==monthCurrent:    
                if monthCurrent==4 or monthCurrent==6 or monthCurrent==9 or monthCurrent==11:
                    res= 30-dateCurrent
                if monthCurrent==1 or monthCurrent==3 or monthCurrent==5 or monthCurrent==7 or monthCurrent==8 or monthCurrent==10 or monthCurrent==12:
                    res= 31-dateCurrent
                if monthCurrent==2:
                    res= 28-dateBirth
            if l==monthBirth:
                res= dateBirth-1
            if l!=monthCurrent && l!=monthBirth:    
                if l==4 or l==6 or l==9 or l==11:
                    res=30
                if l==1 or l==3 or l==5 or l==7 or l==8 or l==10 or l==12:
                    res=31
                if l==2:
                    res=28
            bd+=res           
        for m in range(1,monthBirth+1):
            if m==monthCurrent:
                if monthCurrent==4 or monthCurrent==6 or monthCurrent==9 or monthCurrent==11:
                    res= 30-dateCurrent
                if monthCurrent==1 or monthCurrent==3 or monthCurrent==5 or monthCurrent==7 or monthCurrent==8 or monthCurrent==10 or monthCurrent==12:
                    res= 31-dateCurrent
                if monthCurrent==2:
                    res= 28-dateBirth
            if m==monthBirth:
                res= dateBirth-1
            if m!=monthCurrent && m!=monthBirth:
                if m==4 or m==6 or m==9 or m==11:
                    res=30
                if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
                    res=31
                if m==2:
                    res=28
            bd+=res
    bd+=1 #added 1 to the total because this 1 is added for counting today's date.
    print(bd," days are left for your next birthday!")
if nxtB=="N" or nxtB=="n":
    print("Ok then :(  I thought you were excited to know!")
print()
ans= input("Wanna know the developer's name? Y/N: ")
if ans!="Y" and ans!="y" and ans!="N" and ans!="n":
    ans= input("Follow the instructions carefully (Re-enter either Y or N): ")
if ans=="Y" or ans=="y":
    print("----Sarthak----")
if ans=="N" or ans=="n":
    print("I thought you were too keen to know who developed such a cool program :(")
print()
print("<Process Finished>")
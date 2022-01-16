#!/usr/bin/env python
# coding: utf-8

# In[42]:


#Proceed is used to verify if the program will run without error
proceed=True

#Function with half of the courses
def half():
    print("Enter grades on 12.0 GPA scale")
    print()
    chem=int(input("CHEM 1E03: "))*3
    math_a=int(input("MATH 1ZA3: "))*3
    physics_a=int(input("PHYSICS 1D03: "))*3
    elective_a=int(input("Elective 1: "))*3
    half.CGPA=(chem+math_a+physics_a+elective_a)/12
    
#Function with all of the courses
def full():
    print("Enter grades on a 12.0 GPA scale")
    print()
    chem=int(input("CHEM 1E03: "))*3
    math_a=int(input("MATH 1ZA3: "))*3
    physics_a=int(input("PHYSICS 1D03: "))*3
    elective_a=int(input("Elective 1: "))*3
    math_b=int(input("MATH 1ZB3: "))*3
    math_c=int(input("MATH 1ZC3: "))*3
    physics_b=int(input("PHYSICS 1E03: "))*3
    elective_b=int(input("Elective 2: "))*3
    engineering=int(input("ENGINEER 1P13: "))*13
    full.CGPA=(chem+math_a+physics_a+elective_a+math_b+math_c+physics_b+elective_b+engineering)/37

#Chose which model to use based on semesters completed
sem=int(input("How many semesters have you completed? "))
print()
if sem==1:
    predict=input("Would you like to predict semester 2 grades? (Y/N) ")
    print()
    if predict == ("N") or predict == ("n"):
        half()
        CGPA=half.CGPA
    elif predict == ("Y") or predict == ("y"):
        full()
        CGPA=full.CGPA
    else:
        print()
        print ("Enter Y or N")
        proceed=False 
        print ("Restart program")
elif sem==2:
    full()
    CGPA=full.CGPA
else:
    print()
    print ("Please enter 1 or 2")
    proceed=False
    print ("Restart program")

#Output CGPA
if proceed==True:
    if CGPA>12 or CGPA<0:
        print()
        print ("Invalid CGPA")
        proceed=False
        print ("Restart program")
    elif CGPA<=12 and CGPA>=0:
        print()
        print("Your CGPA is:",round(CGPA,2))

#Calculate mechatronics and software
if proceed==True:
    if CGPA>=11:
        tronsoft=95
    elif (11>CGPA>=9.5):
        tronsoft=((CGPA-9.5)/1.5)*45+50
    elif(9.5>CGPA>=9.3):
        tronsoft=((CGPA-9.3)/0.2)*20+30
    elif(9.3>CGPA>=8.0):
        tronsoft=((CGPA-8)/1.3)*25+5
    elif(8.0>CGPA>=4.0):
        tronsoft=((CGPA)/4)*5
    elif CGPA<=4.0:
        tronsoft=0
    
#Calculate computer
if proceed==True:
    if CGPA>=9.5:
        comp=95
    elif (9.5>CGPA>=9.3):
        comp=((CGPA-9.3)/0.2)*20+75
    elif(9.3>CGPA>=8):
        comp=((CGPA-8.0)/1.3)*55+20
    elif(8.0>CGPA>=6.8):
        comp=((CGPA-6.8)/1.2)*15+5
    elif(6.8>CGPA>=4.0):
        comp=((CGPA-4.0)/2.8)*5
    elif CGPA<=4.0:
        comp=0
    
#Calculate mechanical
if proceed==True:
    if CGPA>=8.0:
        mech=95
    elif(8.0>CGPA>=6.8):
        mech=((CGPA-6.8)/1.2)*15+80
    elif(6.8>CGPA>=6.0):
        mech=((CGPA-6.0)/0.8)*30+50
    elif(6.0>CGPA>=4.0):
        mech=((CGPA-4.0)/2)*40+10
    elif CGPA<=4.0:
        mech=0
        
#Calculate electrical
if proceed==True:
    if CGPA>=6.0:
        elec=95
    elif(6.0>CGPA>=4.0):
        elec=((CGPA-4.0)/2)*60+35
    elif CGPA<=4.0:
        elec=0

#Calculate chemical and civil
if proceed==True:
    if CGPA>=6.0:
        chemciv=95
    elif(6.0>CGPA>=4.0):
        chemciv=((CGPA-4.0)/2)*20+75
    elif CGPA<=4.0:
        chemciv=0
    
#Calculate engineering phyiscs and materials
if proceed==True:
    if CGPA>=4.0:
        physmat=95
    elif CGPA<=4.0:
        physmat=0

#Society and management eligibility
if proceed==True:
    if CGPA>=9.3:
        soc=("will")
        man=("will")
    elif(9.3>CGPA>=8):
        soc=("will")
        man=("might")
    elif(8>CGPA>=6.8):
        soc=("might")
        man=("won't")
    elif CGPA<6.8:
        soc=("won't")
        man=("won't")

#NSERC eligibility
if proceed==True:
    if CGPA>=10.0:
        nserc=("are")
    elif(10.0>CGPA>=7.0):
        nserc=("may be")
    elif CGPA<7.0:
        nserc=("aren't")

#Get deadline from url
import requests
link="https://research.mcmaster.ca/funding/nserc-undergraduate-student-research-award-usra/"
raw=requests.get(link)
rawtext=raw.text
first=rawtext.split("<b>")
second=split[2]
third=second.split("<")
deadline=third[0]

#Output
if proceed==True:
    print()
    print("Your odds of getting into each Eng II Program are:")
    print("--------------------")
    print("Software:",(round(tronsoft,2))-2.5,"%")
    print("Mechatronics:",round(tronsoft,2),"%")
    print("Computer:",round(comp,2),"%")
    print("Mechanical:",round(mech,2),"%")
    print("Electrical:",round(elec,2),"%")
    print("Chemical:",round(chemciv,2),"%")
    print("Civil:",round(chemciv,2),"%")
    print("Engineering Physics:",round(physmat,2),"%")
    print("Materials:",round(physmat,2),"%")
    print()
    print("You",man,"be admitted to the management program")
    print("You",soc,"be admitted to the society program")
    print()
    print("You",nserc,"eligble for the NSERC undergraduate student research award")
    print("For info about NSERC, go to:") 
    print("https://research.mcmaster.ca/funding/nserc-undergraduate-student-research-award-usra/")
    print("Deadline:", deadline)


# 

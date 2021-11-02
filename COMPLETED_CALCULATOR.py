import math
import time
import random

a = random.randint(3,7)

def add(x, y):
    """This function adds two numbers"""
    return x + y


def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y


def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y


def divide(x, y):
    """This function divides two numbers"""
    return x / y


def square_root(x):
    """This Function Gives The Square Root Of The Number"""
    #return math.sqrt(x)
    for i in range(1,x+1):
        if i*i == x:
            return i

def square_of_a_number(x):
    """This Function Gives The Square Of A number"""
    return x * x


def factorial(x):
    """This Function Gives The Factorial Of A Number"""
    product = 1
    for i in range(1,x+1):
        product *= i
    return product
    


def sum_of_the_numbers_before_the_number_you_entered(x):
    """This Function Gives The Sum Of All The Numbers Before The Number Which You Have Entered """
    return ((x/2)*(2*x + ((x-1)*-1)))-x


def logarithm(x, y):
    """This Function Helps In Performing Logarithm"""
    return math.log(x, y)


def MOD(x):
    """This Function Gives The Nearest Number OR It Rounds The Entered Number """
    if x > 0:
        return x
    elif x < 0:
        return -(x)


def HCF(x, y):
    """This Function Gives The HCF Of The Entered Two Numbers """
    return math.gcd(x, y)

def COPYsign(x,y):
    """math.copysign(x, y) function return a float with the magnitude (absolute value) of x but the sign of y."""
    return math.copysign(x,y)

def multiple_expressions():
    exp=input('\nEnter your expression: ')
    while True:
        try:   
            print("ANSWER of [",exp,"]:",eval(exp))
            print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
            print("press 'C' to use the calculator again or type anything to quit!")
            check=input()
            if check=='c' or check=='C':
                exp=input('Enter your expression: ')
            else:
                print("We will divert you back to the main part of the program......")
                time.sleep(a)
                break
        except Exception as e:
            print('your expression is invalid,TRY AGAIN!')
            print('type anything to "Exit" or press C to "Continue"')
            check=input()
            if check=='C' or check=='c':
                exp=input('Enter a valid expression: ')
            else:
                print("We will divert you back to the main part of the program...... (please wait for a moment)")
                time.sleep(a)
                break
    

def SI_units(val,unit_in,unit_out):
    return val * SI[unit_in] / SI[unit_out]    
    

while True:
    type_of_calculator = input('\nEnter(standard[st], converter[C], scientific[sc], programmer[prg] and date calcualtion(dc) or type q to quit from the program:- )')
    
    if type_of_calculator == 'q':
        exit()
    
    
    
    if type_of_calculator == 'st':

    # take input from the user
        while True:
                print("Select operation.")
                
                print("1.Add")
                print("2.Subtract")
                print("3.Multiply")
                print("4.Divide")
                print("5.Performing Logarithm")
                print("6.HCF")
                print("7.square root")
                print("8.square of a number")
                print("9.factorial")
                print("10.sum of the numbers before the number you entered")
                print("11.MOD")
                print("12.Copysign")
                print('13.For doing multiple operations(+,-,*,/) at single time using any number of numbers ')
                
                
                try:
                    choice = int(input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13) or press 0 to quit:"))
                    if choice == 13:
                        multiple_expressions()
                        
                            
                    if choice == 0:
                        print('\n\n we will divert you back to the main part of the program..... (please wait for a moment)')
                        time.sleep(8)
                        break
                    global num1, num2
                    if choice <= 6 and (choice != 5 and choice != 11 and choice != 12 and choice != 13):
                        num1 = int(input("Enter 1 first number: "))
                        num2 = int(input("Enter 2 second number: "))
                    elif choice == 5:
                        num1 = int(input("Enter the numeric number: "))
                        num2 = int(input("Enter the base: "))
                    elif choice == 11:
                        num1 = float(input("Enter the numeric number: "))
                    elif choice == 12:
                        num1 = float(input("Enter 3 first number: "))
                        num2 = float(input("Enter 4 second number: "))
                        
                    elif choice > 13:
                        print("Invalid input!!!! \n PLEASE ENTER THE CORRECT NUMBER OF THE CHOICE GIVEN.!!! \n PLEASE TRY AGAIN!!! \n THANKYOU....")
                        continue
                    
                    #elif choice < 11 or choice > 6 or choice == 8 and choice != 13:
                    elif choice < 11 or choice > 6 and choice == 8 and choice != 13:
                        num1 = int(input(" 5 Enter first number: "))
                    

                    if choice == 1:
                        print(num1, "+", num2, "=", add(num1, num2))
                        time.sleep(4)
                        continue
                    
                    elif choice == 2:
                        print(num1, "-", num2, "=", subtract(num1, num2))
                        time.sleep(4)
                        continue
                    
                    elif choice == 3:
                        print(num1, "*", num2, "=", multiply(num1, num2))
                        time.sleep(4)
                        continue
                    
                    elif choice == 4:
                        print(num1, "/", num2, "=", divide(num1, num2))
                        time.sleep(4)
                        continue
                    
                    elif choice == 5:
                        print("The Answer Is:- ", logarithm(num1, num2))
                        time.sleep(4)
                        continue
                    
                    elif choice == 6:
                        print("The HCF Of ", num1,"and", num2, "is :- ", HCF(num1, num2))
                        time.sleep(4)
                        continue
                    
                    elif choice == 7:
                        print("The Square Root Of", num1, "Is:- ", square_root(num1))
                        time.sleep(4)
                        continue
                    
                    elif choice == 8:
                        print("The Square Of", num1, "Is :- ", square_of_a_number(num1))
                        time.sleep(4)
                        continue
                    
                    elif choice == 9:
                        print("The Factorial Of", num1, "Is:- ", factorial(num1))
                        time.sleep(4)
                        continue
                    
                    elif choice == 10:
                        print("The Sum Of The Numbers Before", num1, "is:- ", sum_of_the_numbers_before_the_number_you_entered(num1))
                        time.sleep(4)
                        continue
                    
                    elif choice == 11:
                        print("The Answer Is:- ", MOD(num1))
                        time.sleep(4)
                        continue
                    
                    elif choice == 12:
                        print("The Copysign of",num1,"and",num2,"is :- ", COPYsign(num1,num2))
                        time.sleep(4)
                        continue
                    
                except ValueError as e:
                    print('\nyour expression is invalid,TRY AGAIN!')
                    print('WE WILL DIVERT YOU BACK TO MAIN PART OF THIS PROGRAM.....')
                    time.sleep(4)
                    continue
                      

    if type_of_calculator == 'C':
        while True:
            try:
                type_of_conversion=input("\nEnter The Type Of Conversion:-\nL: LENGTH\nV:VOLUME\nWM: WEIGHT AND MASS\nA: AREA\nT:TEMPERATURE\nE: ENERGY\nSP: SPEED\nTi: Time\nW:POWER\nP:PRESSURE\nDA:DATA\nAN:ANGLE or to quit type 'q':- ")
                
                if type_of_conversion == 'q':
                    print('\n\n we will divert you back to the main part of the program.....(please wait for a moment)')
                    time.sleep(8)
                    break
                if type_of_conversion=="V":
                    print("mililiter = ml")
                    print("gallons(UK) = G")
                    print("liters = l")
                    SI = {'ml': 0.001, 'l': 1, 'G':4.5}
                    b = input("Enter The unit From Which You Want To Convert:- ")
                    c = input("Enter The unit To Which You Want To Convert The Number To :- ")
                    a = int(input("Enter The Number Which You Want To Convert:- "))
                    a = SI_units(a, b, c)
                    print(b,"in", c,  "is", a)
                    continue


                elif type_of_conversion=="L":
                    print("millimeters:mm \n centimeters:cm \n meters:m \n kilometers:km \n nanometers:nm \n feet:f \n yards:y \n Miles:mi \n inches:i")

                    SI = {'mm': 0.001, 'cm': 0.01, 'm': 1.0, 'km': 1000.0, 'nm':0.000000001,'f':0.3048, 'y':0.9144, 'mi':1609.34, 'i':0.0254}

                    b = int(input("Enter The Number Which You Want To Convert:- "))
                    c = input("Unit from:- ")
                    d = input('Unit to:- ')
                    a = SI_units(float(b), c, d)
                    print(b,c,"in",d,"is",a)
                    continue
                
                elif type_of_conversion=="WM":
                    print("carats:C \n milligrams:mg \n centigrams:cg \n decigrams:dg \n grams:G \n decagrams:Dg \n hectograms:Hg \n killograms:Kg \n tonnes:T \n pounds:P")
                    SI = {'C': 0.2, 'mg': 0.001, 'cg': 0.01, 'dg': 0.1, 'G': 1.0, 'Dg': 10.0, 'Hg': 100, 'Kg': 1000, 'T': 1000000, 'P':453.592}
                    b = int(input("Enter The Number Which You Want To Convert:- "))
                    c = input("Unit from:- ")
                    d = input('Unit to:- ')
                    a = SI_units(float(b), c, d)
                    print(b,c,"in",d,"is",a)
                    continue
                
                elif type_of_conversion=="A":
                    print("square milimeters: sqmm \n square centimeters:sqcm \n square meters: sqm \n hectares: H \n square kilometers: sqkm \n square inches: sqi \n square feet: sqf \n square yards: sqy \n acres:A")
                    SI = {'sqmm': 0.000001, 'sqcm': 0.0001, 'sqm': 1, 'H': 10000.00, 'sqkm': 1000000.00, 'sqi': 0.000645, 'sqf': 0.092903, 'sqy': 0.836127,'A': 4046.856}
                    b = int(input("Enter The Number Which You Want To Convert:- "))
                    c = input("Unit from:- ")
                    d = input('Unit to:- ')
                    a = SI_units(float(b), c, d)
                    print(b,c,"in",d,"is",a)
                    continue
                
                elif type_of_conversion == "T":
                    print("celsius:C \n farenhite:F \n kelvin:K")
                    c = input("Unit from (Only WRITE in capital letters and only the units given ABOVE) :-")
                    d = input('Unit to (Only WRITE in capital letters and only the units given ABOVE):- ')
                    if c=="C" and d=="F":
                        celsius = float(input("Enter temperature in celsius: "))
                        fahrenheit = (celsius * 9 / 5) + 32
                        print('%.2f Celsius is: %0.2f Fahrenheit' % (celsius, fahrenheit))

                    elif c=="F" and d=="C":
                        fahrenheit = float(input("Enter temperature in fahrenheit: "))
                        celsius = (fahrenheit - 32) * 5 / 9
                        print('%.2f Fahrenheit is: %0.2f Celsius' % (fahrenheit, celsius))

                    elif c=="C" and d=="K":
                        celsius=float(input("Enter Temperature in celsius:- "))
                        print(celsius+273.15,"k")

                    elif c=="K" and d=="C":
                        kelvin=int(input("Enter The Temperature in Kelvin:- "))
                        print(kelvin-273.15,"C")

                    elif c=="F" and d=="K":
                        fahrenheit=float(input("Enter The Temperature In Farenhite:- "))
                        Kelvin = (fahrenheit-32) * 5 / 9 + 273.15
                        print(Kelvin)

                    elif c=="K" and d=="F":
                        Kelvin=float(input("Enter The Temperature In Kelvin:- "))
                        farenhite= (Kelvin - 273.15) * 9 / 5 + 32
                        print(farenhite)
                    else:
                        print("Enter The Correct unit\nOR\nUNDER DEVELOPMENT")
                    continue
                
                elif type_of_conversion == "E":
                    print("joules:J\nkilojoules:KJ\nthermal_calories:TC\nfood_calories:FC ")
                    SI = {'J': 1, 'KJ': 1000, 'TC': 4.184, 'FC': 4184}
                    c = input("Unit from:- (Only WRITE in capital letters and only the units given ABOVE)")
                    d = input('Unit to:- (Only WRITE in capital letters and only the units given ABOVE)')
                    b = int(input("Enter The Number Which You Want To Convert:- "))
                    a = SI_units(float(b), c, d)
                    print(b,c,"is",a,d)
                    continue
                
                elif type_of_conversion == 'SP':
                    print('centi meters per second: cms\nmeter per second:ms\nkilometer per hour:kmh\nfeet per second:fps\nmiles per hour:mph\nknots:kn\nmach:m')
                    SI = {'cms':0.036,'ms':3.6,'kmh':1,'fps':1.09728,'mph':1.6092,'kn':1.85184,'m':1225.08}
                    c = input("Unit from:- (Only in format as given above)")
                    d = input('Unit to:- (Only in format as given above)')
                    b = int(input("Enter The Number Which You Want To Convert:- "))
                    a = SI_units(float(b), c, d)
                    print(b,c,"is",a,d)
                    continue
                
                elif type_of_conversion == 'Ti':
                    print('microseconds:ms\nmilliseconds:mis\nseconds:s\nminutes:mins\nhours:hr\ndays:d\nweeks:w\nyears:ye')
                    SI = {'ms':0.00000001666667,'mis':0.000017,'s':0.016667,'mins':1,'hr':60,'d':1440,'w':10080,'ye':525960}
                    c = input("Unit from:- (Only in format as given above)")
                    d = input('Unit to:- (Only in format as given above)')
                    b = int(input("Enter The Number Which You Want To Convert:- "))
                    a = SI_units(float(b), c, d)
                    print(b,c,"is",a,d)
                    continue

                elif type_of_conversion == 'W':
                    print('watts:w\nkilowatts:kw\nhorse power:hp\nfoot-pounds/minute:fppm\nBTUs/minute:btupm')
                    SI = {'w':1,'kw':1000,'hp':745.6999,'fppm':0.022597,"btupm":17.58427}
                    c = input("Unit from:- (Only in format as given above)")
                    d = input('Unit to:- (Only in format as given above)')
                    b = int(input("Enter The Number Which You Want To Convert:- "))
                    a = SI_units(float(b), c, d)
                    print(b,c,"is",a,d)
                    continue
                
                elif type_of_conversion == 'P':
                    print('atmospheres:atm\nBars:B\nKilopascals:kp\nmilimeters of mercury:mmm\nPascals:P\npounds per square inch:ppsi')
                    SI = {"atm":1,"B":0.986923,"kp":0.009869,"mmm":0.001316,"P":0.00001,"ppsi":0.068046}
                    c = input("Unit from:- (Only in format as given above)")
                    d = input('Unit to:- (Only in format as given above)')
                    b = int(input("Enter The Number Which You Want To Convert:- "))
                    a = SI_units(float(b), c, d)
                    print(b,c,"is",a,d)
                    continue
                
                elif type_of_conversion == 'AN':
                    print('degrees:d\nradians:r\ngradians:g')
                    SI = {'d':1,"r":57.29578,"g":0.9}
                    c = input("Unit from:- (Only in format as given above)")
                    d = input('Unit to:- (Only in format as given above)')
                    b = int(input("Enter The Number Which You Want To Convert:- "))
                    a = SI_units(float(b), c, d)
                    print(b,c,"is",a,d)
                    continue
                
                elif type_of_conversion == 'DA':
                    print('UNDER DEVELOPMENT....')
                    print('we will divert you back to the main part of the program....(please wait for a moment)')
                    time.sleep(a)
                    break
                
                else:
                    print('write in correct format...')
                    print('\nWe will ask again in a moment please wait')
                    time.sleep(2)
                    continue
                
            except ValueError as e:
                    print('\nyour entered thing is integer or float,TRY AGAIN! with string type only','\nYour Error is:-',e)
                    print('WE WILL DIVERT YOU BACK TO MAIN PART OF THIS PROGRAM.....')
                    time.sleep(3)
                    continue
                      
            
    if type_of_calculator == 'sc':
        print('\n\nUNDER DEVELOPMENT....')
        print('\nwe will divert you back to the main part of the program....(please wait for a moment)')
        time.sleep(2)
        continue
    
    if type_of_calculator == 'prg':
        print('\n\nUNDER DEVELOPMENT....')
        print('\nwe will divert you back to the main part of the program....(please wait for a moment)')
        time.sleep(2)
        continue
    
    if type_of_calculator == 'dc':
        
        print('IMPORTANT NOTE:- \nThe answer would be not 100 % correct just it will not give correct answer for leap years and february month rule and sometimes the answer is printed 2 or three tims just look after it and chose your correct date appropriately after looking at all dates printed!!!\n We will try to make it 100 % in coming days think this as a beta version!!!\nTill then use it and sorry for inconvenience!! ')
        
        while True:
            
            date = int(input('enter the date:- '))
            month = int(input('enter the month:- '))
            year = int(input('enter the year:- '))
        
            months_1 = [1,3,5,7,8,10,12]
            months_2 = [4,6,9,11]
            
            for k in months_2:
                if month == k and date > 30:
                    print('\n\nwrite in correct format...')
                    print('\nWe will ask again in a moment please wait')
                    time.sleep(2)
                    continue
                
            for l in months_1:
                if month == l and date > 31:
                    print('\n\nwrite in correct format...')
                    print('\nWe will ask again in a moment please wait')
                    time.sleep(2)
                    continue
                
            type_of_date_calculation_1 = input('type (add) to add and type (substract) to substract the days or q to quit:- ')
            
            if type_of_date_calculation_1 == 'q':
                print('\nwe will divert you back to the main part of the program....(please wait for a moment)')
                time.sleep(3)
                break
            
            if type_of_date_calculation_1 == 'add':
                num = int(input('\nEnter number of days:- '))
                years = num//365
                months = (num-years*365)//30
                days = (num - years * 365 - months * 30)
                
                f_date,f_month,f_year = date + days, month + months, year+ years
                
                if f_month > 12:
                    
                    f_month = f_month - 12
                    f_year = f_year + 1
            
                    print('The date you wanted is:\nDate:',f_date,' month:',f_month,' year:',f_year)
                
                elif f_date > 31:
                    for i in months_1:
                        if f_month == i:
                            f_date = f_date - 31
                            f_month = f_month + 1
                            
                            print('The date you wanted is:\nDate:',f_date - 1,' month:',f_month,' year:',f_year)
                    for j in months_2:
                        if f_month == j:
                            f_date = f_date - 30
                            f_month = f_month + 1
                            
                            print('The date you wanted is:\nDate:',f_date - 1,' month:',f_month,' year:',f_year)
                            
                if f_month == 2 and (f_year % 4 == 0 or f_year % 100 == 0):
                    f_date = f_date - 29
                    f_month = f_month + 1
                        
                    print('The date you wanted is:\nDate:',f_date - 1,' month:',f_month,' year:',f_year)
                
                elif f_month == 2 and (f_year % 4 != 0 or f_year % 100 != 0):
                    f_date = f_date - 28
                    f_month = f_month + 1
                
                    print('The date you wanted is:\nDate:',f_date - 1,' month:',f_month,' year:',f_year)

                else:
                    print('The date you wanted is:\nDate:',f_date,' month:',f_month,' year:',f_year)
                    continue
            
            if type_of_date_calculation_1 == 'substract':
                print('UNDER DEVELOPMENT...')
                print('\nWe will ask again in a moment please wait')
                time.sleep(2)
                continue
            
            else:
                print('\n\nwrite in correct format...')
                print('\nWe will ask again in a moment please wait')
                time.sleep(2)
                continue
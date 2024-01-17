import datetime


#Set consents 
BASE_SALERY = 350.00
SALE_QOUTA = 5000

def calSpouseAge():
    age = int(input('Enter your age'))

    spouseAge = (age/2)+7
    return spouseAge

def calculateGrade (grade):
    if grade >=80 and grade <= 100:
        letterGrade = "A"
    elif grade >=70 and grade <= 79:
        letterGrade = "B"
    elif grade >=60 and grade <= 69:
        letterGrade = "C"
    elif grade >=50 and grade <= 59:
        letterGrade = "D"
    else:
        letterGrade = "F"
    return letterGrade
def grossPay(hours, payRate):

    if hours <= 40:
        GrossPay = hours*payRate
    else:
        RegPay = 40*payRate
        overTime = (hours - 40)*(payRate*1.5)
        GrossPay = RegPay+overTime
    return GrossPay

def calculateSales (sales):

    if sales <= 5000:
        bounes = sales * 0
    elif sales >= 5000:
        bounes = sales * 0.01
        if sales > 100000:
            bounes = bounes + 500
    return bounes
    
def calInvoiceDate (purDate):
    #calculate the payment date of the next month
    purYear = purDate.year
    purMont = purDate.month
    purDay = purDate.month

    if purDay >= 25:
        purMont += 1

    PayDate = datetime.datetime(purYear, purMont + 1)

    return PayDate

def CalGrossPay(saleQouta):

    if saleQouta < SALE_QOUTA:
        belowQouta = SALE_QOUTA - saleQouta
        drawAgianst = (belowQouta*0.1)
        grossPay = BASE_SALERY - drawAgianst

    elif saleQouta == SALE_QOUTA:
        grossPay = BASE_SALERY

    else:
        over = saleQouta*0.04
        grossPay = over + BASE_SALERY

        if saleQouta >15000:
            grossPay = grossPay + 250

        if saleQouta >25000:
            grossPay = grossPay + 500
    
    return grossPay


while True:

    #print(calSpouseAge())

    '''grade = int(input("Enter the grade:"))
    studentGrade = calculateGrade(grade)
    print(studentGrade)'''

    ''' hours = int(input("Enter the hours: "))
    payRate = float(input('Enter the pay rate: '))

    income = grossPay(hours, payRate)
    print(income)'''

    '''sales = float(input("Enter the sales number: "))

    bouns = calculateSales(sales)
    print(bouns)

    purchaseDate = "2023-10-04"

    purchaseDate = datetime.datetime.strptime(purchaseDate, "%Y-%b-%d")

    payDate = calInvoiceDate(purchaseDate)
    print(payDate)'''

    sales = float(input("Enter total Sales: "))

    pay = CalGrossPay(sales)
    print(pay)


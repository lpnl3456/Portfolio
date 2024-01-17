# A Program to keep track of sales at Honest Harry Car Sales
# Written on Oct 13, 2023
# Auther: Luke Peddle

# Import libraries

import random
import datetime

# Set Constants
HST_RATE = 0.15
LICENCE_FEE_RATE = 75.00
LICENCE_FEE_ABOVE_5000_RATE = 165.00
TRANSFER_FEE_RATE = 0.01
LUXURY_FEE_RATE = 0.016
FIN_FEE_RATE = 39.99

# Gather Inputs

allowed_province = set("NL"+"NS"+"PE"+"QB"+"ON"+"MT"+"SK"+"AB"+"BC"+"NT"+"NV"+"YK")
while True:
    while True:
        custFirstName =  input("Enter the customer's first name: ").title()
        if custFirstName == "":
            print("Input cannot be blank - Please er-enter")
            print()
        else:
            break
    if custFirstName == "End":
        break
    else:

        while True:
            custLastName = input("Enter the customer's last name: ").title()
            if custLastName == "":
                print("Input cannot be blank - Please er-enter")
                print()
            else:
                break

    
        while True:
            stAdd = input("Enter the street addressed: ").title()
            if stAdd == "":
                print("Input cannot be blank - Please er-enter")
                print()
            else:
                break
        while True:
            city = input("Enter the city: ").title()
            if city == "":
                print("Input cannot be blank - Please er-enter")
                print()
            else:
                break
        
        while True:
            province = input("Enter the Province(XX): ").upper()
            if province == "":
                print("Input cannot be blank - Please er-enter")
                print()
            elif len(province) != 2:
                print("Province must be 2 characters - Please re-enter")
                print()
            elif province != "NL" and province != "NS" and province != "PE" and province != "QB" and province != "ON" and province != "MT" and province != "SK" and province != "AB" and province != "BC" and province != "NT" and province != "NV" and province != "YK":
                print("Invalid Province- Please re-enter")
                print()
            else:
                break

        while True:
            postalCode = input("Enter the postal code(X#X#X#): ").upper()
            if postalCode == "":
                print("Input cannot be blank - Please er-enter")
                print()
            elif len(postalCode) != 6:
                print("Postal code must be 6 characters - Please re-enter")
                print()
            elif postalCode [0].isalpha() == False or postalCode [2].isalpha() == False or postalCode [4].isalpha() == False:
                print("The characters in the 1, 3, and 5 postion must be letters - Please re-enter")
                print()
            elif postalCode [1].isdigit() == False or postalCode [3].isdigit() == False or postalCode [5].isdigit() == False:
                print("The characters in the 2, 4, and 6 postion must be numbers - Please re-enter")
                print()
            else:
                break
            
        while True:
            phoneNum = input("Enter the phone number(##########): ")

            if phoneNum == "":
                print("Input cannot be blank -Please er-enter")
                print()
            elif phoneNum.isdigit() == False:
                print("The phone number mus be all numbers - Please re-enter")
            elif len(phoneNum) != 10:
                print("The input must be 10 digits long - Please re-enter")
            else:
                break
        
        while True:
            plateNum = input("Enter the plate number(XXX###): ").upper()
            if plateNum == "":
                    print("Input cannot be blank - Please er-enter")
                    print()
            elif len(plateNum) != 6:
                print("Plate number must be 6 characters - Please re-enter")
                print()
            elif plateNum[0:3].isalpha() == False:
                print("The first three characters must be letters - Please re-enter")
                print()
            elif plateNum[3:6].isdigit() == False:
                print("The last three chacaters must be numbers - Please re-enter")
                print()
            else:
                break

        while True:
            carMake = input("Enter the make of the car: ").title()
            if carMake == "":
                    print("Input cannot be blank - Please er-enter")
                    print()
            else:
                break
        
        while True:
            carModel = input("Enter the model of the car: ").title()
            if carModel == "":
                    print("Input cannot be blank - Please er-enter")
                    print()
            else:
                break
        
        while True:
            carYear = input("Enter the year of the car: ")
            if carYear == "":
                    print("Input cannot be blank - Please er-enter")
                    print()
            elif len(carYear) != 4:
                print("The year must be 4 characters long - Please re-enter")
                print()
            elif carYear.isdigit() == False:
                print("Year must be all numbers - Please re-enter")
                print()
            else:
                break

        while True:
            try:
                sellingPrice = float(input("Enter the selling price: "))
            except:
                print("Selling price must be a number - Please re-enter")
                print()
            else:
                if sellingPrice > 50000.00:
                    print("Selling price cannot exceed $50,000.00 - Please re-enter")
                    print()
                else:
                    break

        while True:
            try:
                tradeIn = float(input("Enter the amount of the trade in: "))
            except:
                print("trade in must be a number - Please re-enter")
                print()
            else:
                if tradeIn > sellingPrice:
                    print("Trade in cannot exceed the selling price - Please re-enter")
                    print()
                else:
                    break

        while True:
            salesName = input("Enter the sales person's name: ")
            if salesName == "":
                    print("Input cannot be blank - Please re-enter")
                    print()
            else:
                break

        # Do calculations

        priceAfterTrade = sellingPrice - tradeIn

        if sellingPrice <= 5000.00:
            licenseFee = LICENCE_FEE_RATE
        else:
            licenseFee = LICENCE_FEE_ABOVE_5000_RATE

        transferFee = sellingPrice *(TRANSFER_FEE_RATE)

        if sellingPrice >20000.00:
            transferFee = transferFee + (sellingPrice * LUXURY_FEE_RATE)

        subtotal = priceAfterTrade + licenseFee + transferFee
        hst = subtotal * HST_RATE

        totalSalesPrice = subtotal + hst

        # Display the receipt

        invoiceDate = datetime.datetime.now()
        invoiceDateDsp = invoiceDate.strftime("%B %d, %Y")
        print()
        print(f"Honest Harry Car Sales                       Invoice Date: {invoiceDateDsp}")
        recID = custFirstName[0] + custLastName[0] + "-" + plateNum[-3:-1] + plateNum[-1] + "-" + phoneNum[-4:-1] + phoneNum[-1]
        print(f"Used Car Sale ans Receipt                    Receipt No:        {recID}")
        print()
        sellingPriceDsp = "${:,.2f}".format(sellingPrice)
        print(f"                                        Sale price:              {sellingPriceDsp:>10s}")
        tradeInDsp = "${:,.2f}".format(tradeIn)
        print(f"Sold to:                                Trade allowance:         {tradeInDsp:>10s}")
        print(f"                                        -----------------------------------")
        fullName = custFirstName[0] + '. ' + custLastName
        priceAfterTradeDsp = "${:,.2f}".format(priceAfterTrade)
        print(f"    {fullName:<30}      Price after Trade:       {priceAfterTradeDsp:>10s}")
        licenseFeeDsp = "${:,.2f}".format(licenseFee)
        print(f"    {stAdd:<30}      License Fee:             {licenseFeeDsp:>10s}")
        fullAdd = city + ", " + province + " " + postalCode
        transferFeeDsp = "${:,.2f}".format(transferFee)
        print(f"    {fullAdd:<30s}      Transfer Fee:            {transferFeeDsp:>10s}")
        print(f"                                        -----------------------------------")
        subtotalDsp = "${:,.2f}".format(subtotal)
        print(f"Car Details:                            Subtotal:                {subtotalDsp:>10s}")
        hstDsp = "${:,.2f}".format(hst)
        print(f"                                        HST:                     {hstDsp:>10s}")
        print(f"    {carYear:<4s} {carMake:<12s} {carModel:<12s}      -----------------------------------")
        totalSalesPriceDsp = "${:,.2f}".format(totalSalesPrice)
        print(f"                                        Total sales price:       {totalSalesPriceDsp:>10s}")
        print()

        print(f"---------------------------------------------------------------------------")
        print()
        print(f"                                Finacing      Total         Monthly")
        print(f"      # Years   # Payments        Fee         Price         Payment")
        print(f"      -------------------------------------------------------------")

        # Calculate and display the monthly payments

        for year in range(1,5):
            payments = year * 12
            finFee = year * FIN_FEE_RATE
            totalPrice = totalSalesPrice + finFee
            monthlyPayment = totalPrice/12

            finFeeDsp = "${:,.2f}".format(finFee)
            totalSalesPriceDsp = "${:,.2f}".format(totalPrice)
            monthlyPaymentDsp = "${:,.2f}".format(monthlyPayment)
            print(f"         {year:<1d}          {payments:>2d}           {finFeeDsp:>7s}    {totalSalesPriceDsp:>10s}   {monthlyPaymentDsp:>10s}")
        
        print(f"      -------------------------------------------------------------")
        invoiceDateDsp = invoiceDate.strftime("%d-%b-%y")
        firstPaymentDate = invoiceDate + datetime.timedelta(days = 30)
        firstPaymentDateDsp = firstPaymentDate.strftime("%d-%b-%y")
        print(f"      Invoice date: {invoiceDateDsp}         First payment date: {firstPaymentDateDsp}")
        print(f"      Sales person's name: {salesName:<20}")
        print()
        print(f"---------------------------------------------------------------------------")
        print(f"                   Best used cars at the best prices!")
        print()

# End program

print()
print("Thank you for using the program. Have a nice day")
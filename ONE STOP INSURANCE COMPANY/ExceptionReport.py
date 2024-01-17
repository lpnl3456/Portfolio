# a Program to create a exception report for ONE STOP INSURANCE COMPANY
# Written on Dec 4, 2021
# Auther: Luke Peddle

# Import libraries
import FormatValues as FV
import datetime
import math

# Set constants 
f = open('OSICDef.dat', 'r')
POLICY_NUM = f.readline()
BASE_PREMUIM_RATE = float(f.readline())
ADD_CAR_DISCOUNT_RATE = float(f.readline())
EXTRA_LIABILITY_RATE = float(f.readline())
GLASS_COVERAGE_RATE = float(f.readline())
LOANER_CAR_RATE = float(f.readline())
HST_RATE = float(f.readline())
MONTHLY_PROC_FEE_RATE = float(f.readline())
f.close()
today = FV.FDateM(datetime.datetime.now())

# Main Program

# Print main headings and column headings
print()
print(f"ONE STOP INSURANCE COMPANY") 
print(f"POLICY LISTING AS OF {today:>9s}")
print()
print(f"POLICY CUSTOMER             TOTAL                TOTAL       DOWN         MONTHLY")
print(f"NUMBER NAME                PREMIUM     HST       COST       PAYMENT       PAYMENT")
print(f"=================================================================================")
    
# Initialize counters and accumulators for summary / analytics.
polCtr = 0
totPreAcc = 0
totHstAcc = 0
totCostAcc = 0
totDownPayAcc = 0
totMonthPayAcc = 0

# Open the file with the "r" mode for read.
f = open("Policies2.dat", "r")

for policyRec in f:  
    extraCosts = 0
    
    # Input - read the first record and split into a list.
    policyList = policyRec.split(",")
        
    #Assign variables to each item in the list that are required in the report.
    polNum = policyList[0].strip()
    custFirstName = policyList[2].strip()
    custLastName = policyList[3].strip()
    polNumCarIn = int(policyList[9].strip())
    polExtLia = policyList[10].strip()
    polGlassCov = policyList[11].strip()
    polLoanCar = policyList[12].strip()
    PolPayMeth = policyList[13].strip()
    polDownPay = float(policyList[14].strip())

    # Calculations
    if PolPayMeth != "Full":
        inPre = BASE_PREMUIM_RATE + ((polNumCarIn -1)*BASE_PREMUIM_RATE* (1 + ADD_CAR_DISCOUNT_RATE))

        if polExtLia == "Y":
            extraCosts = extraCosts + EXTRA_LIABILITY_RATE
        
        if polGlassCov == "Y":
            extraCosts = extraCosts +  GLASS_COVERAGE_RATE
        
        if polLoanCar == "Y":
            extraCosts = extraCosts +  LOANER_CAR_RATE
        
        totPre = inPre + extraCosts

        hst = totPre * HST_RATE

        totPay = totPre + hst

        monthPay = ((totPay + MONTHLY_PROC_FEE_RATE)-polDownPay)/12

        print(f"{polNum:>4} {FV.FName(custFirstName,custLastName):<18s} {FV.FDollar2(totPre):>10s}   {FV.FDollar2(hst):>7s}  {FV.FDollar2(totPay):>10s}  {FV.FDollar2(polDownPay):>10s}   {FV.FDollar2(monthPay):>10s}")

        polCtr = polCtr + 1
        totPreAcc = totPreAcc +totPre
        totHstAcc = totHstAcc + hst
        totCostAcc = totCostAcc + totPay
        totDownPayAcc = totDownPayAcc + polDownPay
        totMonthPayAcc = totMonthPayAcc + monthPay

f.close()
print(f"=================================================================================")
print(f"Total policies: {polCtr:>3d}     {FV.FDollar2(totPreAcc):>10s}  {FV.FDollar2(totHstAcc):>7s}  {FV.FDollar2(totCostAcc):>10s}   {FV.FDollar2(totDownPayAcc):>10s} {FV.FDollar2(totMonthPayAcc):>10s}")
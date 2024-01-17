# a Program to create a detailed report for ONE STOP INSURANCE COMPANY
# Written on Dec 1, 2021
# Auther: Luke Peddle

# Import libraries
import FormatValues as FV
import datetime

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
print(f"POLICY CUSTOMER               POLICY      INSURANCE      EXTRA      TOTAL")
print(f"NUMBER NAME                    DATE        PREMUIM       COSTS     PREMUIM")
print(f"==========================================================================")

# Initialize counters and accumulators for summary / analytics.
polCtr = 0
insurPreAcc= 0
extraCostsAcc = 0
totPreAcc = 0

# Open the file with the "r" mode for read.
f = open("Policies2.dat", "r")

for policyRec in f:  

    inPre = 0
    extraCosts = 0
    totPre = 0
    # Input - read the first record and split into a list.
    policyList = policyRec.split(",")
        
    #Assign variables to each item in the list that are required in the report.
    polNum = policyList[0].strip()
    custFirstName = policyList[2].strip()
    custLastName = policyList[3].strip()
    polDate = policyList[1].strip()
    polNumCarIn = int(policyList[9].strip())
    polExtLia = policyList[10].strip()
    polGlassCov = policyList[11].strip()
    polLoanCar = policyList[12].strip()

    # Calculations

    inPre = BASE_PREMUIM_RATE + ((polNumCarIn -1)*BASE_PREMUIM_RATE/(1 +ADD_CAR_DISCOUNT_RATE))

    if polExtLia == "Y":
        extraCosts = extraCosts + EXTRA_LIABILITY_RATE
    
    if polGlassCov == "Y":
        extraCosts = extraCosts +  GLASS_COVERAGE_RATE
    
    if polLoanCar == "Y":
        extraCosts = extraCosts +  LOANER_CAR_RATE
    
    totPre = inPre + extraCosts

    print(f"{polNum:>4}   {FV.FName(custFirstName,custLastName):<18s}    {polDate:<10s}  {FV.FDollar2(inPre):>10s}    {FV.FDollar2(extraCosts):>7s}  {FV.FDollar2(totPre):>10s}")

    polCtr = polCtr + 1
    insurPreAcc = insurPreAcc + inPre
    extraCostsAcc = extraCostsAcc + extraCosts
    totPreAcc = totPreAcc +totPre

f.close()
print(f"==========================================================================")
print(f"Total policies: {polCtr:>3d}                     {FV.FDollar2(insurPreAcc):>11s} {FV.FDollar2(extraCostsAcc):>10s} {FV.FDollar2(totPreAcc):>11s}")
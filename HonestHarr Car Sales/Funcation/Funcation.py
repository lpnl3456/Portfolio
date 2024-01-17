

#set program funcation.
def Celsuis(temp):
    #Funcation to convert celuis to ferhinhit
    return 9/5*temp+32

def TrainingHeartRate():
    age = float(input('Enter the age: '))
    restingRate = float(input("Enter the resting heart rate: "))

    trainingRate = ((220-age)- restingRate)*0.6+restingRate
    print(trainingRate)

while True:
    #temp = int(input("Enter the temperature"))
    #print(Celsuis(temp))
    TrainingHeartRate()
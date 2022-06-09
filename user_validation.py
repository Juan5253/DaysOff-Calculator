from datetime import datetime, date 
#defines the time of service from the date firstDay as string parameter
def calculateSeniority(firstDay):
    firstDateValue = datetime.strptime(firstDay, '%d/%m/%Y') #converts the string it receives as a parameter to a datatime object, also in the defined date format.
    todayDate = date.today() #Take actual date
    seniorityYears = todayDate.year - firstDateValue.year
    seniorityYears -= ((todayDate.month, todayDate.day) < (firstDateValue.month, firstDateValue.day)) #If the month and day of today are less than the month and day of start date, subtract 1
    return seniorityYears
#Defines the days off from the seniority and department key
def calculateDaysOff(seniorityYears, deparmentKey):
    daysOff = 0
    if deparmentKey == 1:
        if seniorityYears == 1:
            daysOff = 6
        elif seniorityYears >= 2 and seniorityYears<=6:
            daysOff = 14
        elif seniorityYears >= 7:
            daysOff = 20
        else:
            print("No tienes dias de descanso ")
    elif deparmentKey == 2:
        if seniorityYears == 1:
            daysOff = 7
        elif seniorityYears >= 2 and seniorityYears<=6:
            daysOff = 12
        elif seniorityYears >= 7:
            daysOff = 22
        else:
            print("No tienes dias de descanso ")
    elif deparmentKey == 3:
        if seniorityYears == 1:
            daysOff = 10
        elif seniorityYears >= 2 and seniorityYears<=6:
            daysOff = 20
        elif seniorityYears >= 7:
            daysOff = 30
        else:
            print("No tienes dias de descanso ")
    else :
        print ("Codigo de departamento invalido!! ")

    return(daysOff) 
#Convert the department key to a string as appropriate
def assingmentOfDepartment(departmentKey):
    department = ""
    if departmentKey == 1:
        department = "Atención al cliente"
    elif departmentKey == 2:
        department = "Logística"
    elif departmentKey == 3:
        department = "Gerencia"
    return department
#Menu print function
def viewdaysOff(name, department, daysOff):
    daysOffS = str(daysOff)
    print ("------------------------------ \n Trabajador " + name + "\n Su departamento es " + department + "\n Sus dias de vacaciones son : " + daysOffS + "\n------------------------------")


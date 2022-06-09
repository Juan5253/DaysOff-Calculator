#DAYS OFF CALCULATOR
import user_validation
from os import system

title = "BIENVENIDO"
print(title.center(20))
name = input("Digite su nombre: ")
departmentKey = int(input("Digite la clave de su departamento : "))
seniority=input("Digite la fecha de su primer dia en el trabajo (DD/MM/AAAA) :")
system("cls")

seniorityValue= user_validation.calculateSeniority(seniority)
departmentValue= user_validation.assingmentOfDepartment(departmentKey)
daysOffValue = user_validation.calculateDaysOff(seniorityValue,departmentKey)

user_validation.viewdaysOff(name, departmentValue, daysOffValue)

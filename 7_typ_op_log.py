IsWeekend = False
print("Is weekend=", IsWeekend)

Temperature = 5
print("Temperature =", Temperature)

ToDoList = "Shopping"
print("ToDoList =", ToDoList)

IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ""
print("IsHappy =", IsHappy)

IsHappy = not IsWeekend and Temperature < 20 and ToDoList != ""
print("IsHappy =", IsHappy)

IsHappy = IsWeekend and Temperature >= 20 and ToDoList == "" \
          or not IsWeekend and Temperature < 20 and ToDoList != ""
print("IsHappy =", IsHappy)


# zadania:
isAutomaticMode = False
is80PercentLight = True
isDirectLight = False
isRainy = True
turnLightsOn = isAutomaticMode == True and (is80PercentLight == False \
               or isDirectLight == True or isRainy == True)

print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

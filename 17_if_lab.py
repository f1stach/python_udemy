print("ZADANIE 1")
musclePain = True
fever = False
weakness = False
isMan = True

if musclePain and fever and weakness or (isMan and (musclePain or fever or weakness)):
    print("suspiction of influenza")
elif weakness and not fever or not musclePain:
    print("Just take a rest!")
else:
    print("you may be cold")

print("ZADANIE 2")

isCheckCompleted = True
print("Check is completed" if isCheckCompleted else "Check not done yet!")
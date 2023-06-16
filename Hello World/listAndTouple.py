numbersForMath = []
while True:
    value=input("Type number for mafs or press X to finish:")
    if value.isdigit():
        value=int(value)
        numbersForMath.append(value)
        print("numbers so far:",len(numbersForMath))
    elif value == "X" or value =="x":
        break
    else:
        print('Silly Boy... das not right. I only like happy numbers. no negative downers')
print(sum(numbersForMath))
print("Here is Number Spam Now")
for number in numbersForMath:
    print(number)
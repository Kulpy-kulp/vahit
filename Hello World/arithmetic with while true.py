# This is for math things
# To add, use +

# This is to add Number a to Number B. int checks to see if number is valid. As long as anything inside is "correct" it will loop forever until it reaches a break.
# So if a user doesn't type a number, then it will repeat the 1st step, "type a number"

#IsDigit only works with string... yes I could have done 'numberAint(input("type a number:"))' but if they add a "P" then it errors
while True:
    numberA=input("Type a number:")
    
    if numberA.isdigit(): #IsDigit only works with string... yes I could have done int(input) but if they add a "P" then it errors
        numberA=int(numberA)
        break
    else:
        print("IT SAYS NUMBER!")
while True:
    numberB=input("Type another number:")
    
    if numberB.isdigit():
        numberB=int(numberB)
        break
    else:
        print("IT SAYS NUMBER!")

 # Woo! All the numbers provided were indeed valid digits so that means the below will now kick in.         
addition=(numberA + numberB)
print("#########################")
print(numberA,"plus",numberB,"equals",addition)
print("#########################")
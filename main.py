print("<----------------Welcome To My Calculator!-------------------->")

done = False
while not done
  num1 = int(input("Give me a number:"))
  operator = input("Give me an operation") 
  num2 = int(input ("Give Me another Number:"))
  
  if operator == '+':
    print(num1 + num2)
  
  if operator == '-':
    print(num1 - num2)
  
  if operator == '*':
    print(num1 * num2)
  
  if operator == '/':
    print(num1 / num2)
  
  if operator == '^':
    print(num1 ** num2)
  
  if operator == '%':
    print(num1 % num2)

  userInput = input("Do you want to continue calculating?")
  if userInput == 'Yes'
    done = False
  else:
    done = True
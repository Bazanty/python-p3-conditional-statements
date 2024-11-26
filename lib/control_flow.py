#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

 
    

def hows_the_weather(temperature):
    if temperature == 33:
        return "It's brisk out there!"
    if temperature == 55:
        return "It's a little chilly out there!"
    if  temperature <= 75:
        return "It's perfect out there!"
    
    elif temperature >= 99:
        return "It's too dang hot out there!"
    
    
      
    # your code here
    
    pass

def fizzbuzz(num):
    if not num % 15:
        return "FizzBuzz"
    elif not num % 5:
        return "Buzz"
    elif not num % 3:
        return "Fizz"
    return num
      
    # your code here
    pass

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    
    print ("Invalid operation!")
    return None
    
    # your code here
    pass

number = int(input())
factorial = 1
expresion = ""
if number < 0:
   print("Cant proceed")
else :
   for i in range(number, 0, -1):
       factorial *= i
       expresion += f"{i}x"
   expresion += "0!"
   print(f"{expresion}={factorial}")
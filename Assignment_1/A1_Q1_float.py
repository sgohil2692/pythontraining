user_input = input ("Enter  your salary")
try:
   val = float(user_input)
   print("Yes, input string is a float number.")
   print("Input float number value is: ", val)
except ValueError:
   print("That's not an float!")
   print("No.. input string is not a float number. It's a string")
def near_hundred(n):
      return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
print(near_hundred(100))
print(near_hundred(90))
print(near_hundred(80))   
print(near_hundred(220))
print(near_hundred(210))
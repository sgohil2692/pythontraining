def reverse(string): 
    string = "".join(reversed(string)) 
    return string 
  
s = "python program"
  
print ("The original string  is : ",end="") 
print (s) 
  
print ("The reversed string(using reversed) is : ",end="") 
print (reverse(s)) 
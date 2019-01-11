number = 12345678
rev = 0
#this block gives reverse number
while number > 0:
    rem = number % 10
    rev = rev*10 + rem
number = int(number/10)
#number convert to list
number_list = [int(i) for i in str(rev)]

#take only 7654321
number_list1 = number_list[1:len(number_list)]
print(number_list1) #print 7654321

#for multiply by 2 the 1st,3rd,5th,7th (Odd) numbers
for i in range(len(number_list1)):
    if number_list1[i]%2 != 0:
        print(number_list1[i]*2)
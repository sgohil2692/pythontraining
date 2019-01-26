
>>> x=input("Enter the comma separated calues :")
Enter the comma separated calues :2,5,25,4,64,647,46,9,5,1,21
>>> x
'2,5,25,4,64,647,46,9,5,1,21'
>>> x=input("Enter the comma separated calues :").split(',')
Enter the comma separated calues :2,5,25,4,64,647,46,9,5,1,21
>>> x
['2', '5', '25', '4', '64', '647', '46', '9', '5', '1', '21']
>>> tuple(x)
('2', '5', '25', '4', '64', '647', '46', '9', '5', '1', '21')
>>>
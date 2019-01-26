>>> new_list=[ 1 , 2 , 3 , 4 , 5 , 6 , [ "Riyaz" , "Ul" , "Haque" , 7 ] , 8 , 9 , 10 ]
>>> new_list [ -4 ]
['Riyaz', 'Ul', 'Haque', 7]
>>> new_list [ 4 ]
5
>>> new_list [ 6 ] [ 1 ]
'Ul'
>>> new_list . append ( [ "new" ] )
>>> new_list . sort( )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'list' and 'int'
>>> 
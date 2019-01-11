def fizz_buzz(num):
    if num%2==0 and num%6==0:
        return 'FizzBuzz'

    elif num % 2 == 0:
        return 'Fizz'

    elif num % 6 ==0:
        return 'Buzz'
    else:
        return num

for n in range(1,50):
    print(fizz_buzz(n))
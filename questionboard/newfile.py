## Trisha's FizzBuzz
for i in range(1, 21):
    result = ''
    if i % 3 == 0:
        result += 'Fizz'
    if i % 5 ==0:
        result += 'Buzz'
    if not result:
        result = i
    print(result)

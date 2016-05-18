count = 0

while count < 101:
    if count % 3 == 0 and count % 5 == 0:
        print('FizzBuzz')
    elif count % 3 == 0:
        print('fizz')
    elif count % 5 == 0:
        print('buzz')
    else:
        print(count)
    count += 1

import sys


def fizzer(x):
    if x % 3 == 0:
        return 'Fizz'
    else:
        return ''


def buzzer(x):
    if x % 5 == 0:
        return 'Buzz'
    else:
        return ''


def main():
    for index in range(1, int(sys.argv[1])):
        answer = fizzer(index) + buzzer(index)
        if answer == '':
            answer = index
        print(answer)

if __name__ == '__main__':
    main()

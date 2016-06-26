def open_file(filename):
    try:
        f = open(filename, 'r')
        return f
    except IOError as e:
        print(e)
        f.close()
    except:
        print('unexpected error occurred')
        f.close()


def sum_numbers(numbers_file):
    numbers = [line for line in numbers_file.readlines()]
    sum_of_numbers = 0
    for number in numbers:
        try:
            i = int(number)
            sum_of_numbers += i
        except ValueError as e:
            print(e)
        except:
            print('unexpected error occurred')
    return sum_of_numbers


numbers_file = open_file('numbers.txt')
result = sum_numbers(numbers_file)
numbers_file.close()
print('The result is: {}'.format(result))


def list_students(*args):
    students = ['{} {}'.format(num, student.capitalize()) for num, student in enumerate(reversed(args))]

    # students = []
    # for student in reversed(args):
    #     students.append('{} {}'.format(num, student.capitalize()))
    #     num += 1

    return '\n'.join(students)



expected_result = '''0 Tim
1 Tom
2 Tal'''

result = list_students('tal', 'tom', 'tim')

assert expected_result == list_students('tal', 'tom', 'tim')
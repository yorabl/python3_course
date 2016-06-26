class NotMyName(Exception):
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


def guess_my_name(my_name):
    guess = input('What is my name? ')
    if guess.lower() != my_name.lower():
        raise NotMyName


def run_name_game():
    name = input('set name: ')

    while True:
        try:
            guess_my_name(name)
            print('Success!!!')
            break
        except NotMyName:
            print('No!')


run_name_game()
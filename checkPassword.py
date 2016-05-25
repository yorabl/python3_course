def isspecial(c):
    special_charater = '.!$-?+*_'
    result = False
    for i in special_charater:
        if c is special_charater[i]:
            result = True
            break
    return result


def password_check(s):
    strong_params = dict(digit=False, lower=False, upper=False, special=False, not_allowed=False)
    is_strong = True

    if len(s) > 7:
        for i in s:
            if s[i].isspace() or s[i] is '\t':
                strong_params['not_allowed'] = True
                break
            elif s[i].isdigit():
                strong_params['digit'] = True
            elif s[i].islower():
                strong_params['lower'] = True
            elif s[i].isupper():
                strong_params['upper'] = True
            elif isspecial(s[i]):
                strong_params['special'] = True
    if strong_params['not_allowed']:
        is_strong = False
    else:
        for i in strong_params:
            is_strong = strong_params[i]
    return is_strong


def is_strong_password(s):
    assert False, "Changeme"
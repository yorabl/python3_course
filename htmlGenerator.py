def ul(l):
    """
    (list) -> (string)
    Creates an html unordered list from l

    >>> ul(['a','b','c'])
    "<ul>\n\t<li>a</li>\n\t<li>b</li>\n\t<li>c</li>\n</ul>\n"
    """
    tmp_list = []
    for i in l:
        tmp_list.append('<li>{}</li>\n'.format(i))
    result = '''<ul>\n\t{}</ul>\n'''.format('\t'.join(tmp_list))

    print('{}'.format(result))
    return result


assert ul(['item 1', 'item 2']) == '<ul>\n\t<li>item 1</li>\n\t<li>item 2</li>\n</ul>\n'

assert ul(['a', 'b', 'c']) == '<ul>\n\t<li>a</li>\n\t<li>b</li>\n\t<li>c</li>\n</ul>\n'

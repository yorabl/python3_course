def ul(l):
    """
    (list) -> (string)
    Creates an html unordered list from l

    >>> ul(['a','b','c'])
    "<ul>\n\t<li>a</li>\n\t<li>b</li>\n\t<li>c</li>\n</ul>\n"
    """
    str = '<ul>\n\t<li>{}</li>\n\t<li>'.format(l[0])
    str += '</li>\n\t<li>'.join(l[1:])
    str += '</li>\n</ul>\n'

    return str


assert ul(['item 1', 'item 2']) == '<ul>\n\t<li>item 1</li>\n\t<li>item 2</li>\n</ul>\n'

assert ul(['a', 'b', 'c']) == '<ul>\n\t<li>a</li>\n\t<li>b</li>\n\t<li>c</li>\n</ul>\n'

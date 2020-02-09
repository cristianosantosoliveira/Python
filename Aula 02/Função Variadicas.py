#################################################################
def func_variadic(param, *args):
    print("param:", param)
    for arg in args:
        print(arg)

func_variadic("test", "More", "and", "more", "arguments")

#################################################################
def concat(*args, sep='/'):
    return sep.join(args)

concat('earth', 'mars', 'venus', ".")

#################################################################

def func_var_keyword(param, **keywords):
    print("param", param)
    for kw in keywords:
        print(kw, ":", keywords[kw])

func_var_keyword("test", keyword_a="Value A", keyword_b="Value B", keyword_c="Value C")

#################################################################

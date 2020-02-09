def func_variadic_full(param, *args, **keywords):
    print("param", param)
    print("-" * 40)
    for arg in arg:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

func_variadic_full( "test", "More", "and", "more", "arguments", keyword_a="Value A", keyword_b="Value B", keyword_c="Value C")

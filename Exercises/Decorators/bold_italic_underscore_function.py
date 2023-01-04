def format_text(tag, text):
    return f"<{tag}>{text}</{tag}>"

def make_bold(func):
    def wrapper(*args):
        result = func(*args)
        return format_text('b', result)

    return wrapper


def make_italic(func):
    def wrapper(*args):
        result = func(*args)
        return format_text('i', result)

    return wrapper


def make_underline(func):
    def wrapper(*args):
        result = func(*args)
        return format_text('u', result)

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))

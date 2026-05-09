import functools

USERNAME = "dheen"
PASSWORD = "000"


def authenticated():
    print("user authenticated....")
    print("Login success...")


def invalid_page():
    print("Redirecting to login page...")


def login_user(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        username = args[0] if len(args) > 0 else kwargs.get("username")
        password = args[1] if len(args) > 1 else kwargs.get("password")
        print(
            "User entered",
        )
        if username == USERNAME and password == PASSWORD:
            authenticated()
            return func(*args, **kwargs)
        else:
            invalid_page()

    return wrapper


@login_user
def user_dashboard(username, password):
    print("welcome to dashboard...")


user_dashboard("dheen", "0001")

import os


def clean_console():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")



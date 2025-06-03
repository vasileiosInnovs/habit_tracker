from lib.cli.menu import main_menu, login_or_register

if __name__ == '__main__':
    while True:
        user = login_or_register()
        main_menu(user)
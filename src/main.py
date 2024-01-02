from webbot import Browser
from dotenv import load_dotenv
from os import environ

def main():
    username, password = get_login_credentials()
    print(username)

    web = Browser()

    web.go_to("https://https://fallzabdesk.szabist-isb.edu.pk/")

    web.type(username, into="txtLoginName")
    web.type(password, into="txtPassword")

    web.click(tag="<img src=\"images/LoginButton.gif\" alt=\"ZABDESK Login\" width=\"80\" height=\"22\" "
                  "onclick=\"document.forms.form1.submit();\">")

    source = web.get_page_source()
    print(source)


def get_login_credentials():
    load_dotenv()
    return environ.get("USERNAME"), environ.get("PASSWORD")


if __name__ == "__main__":
    main()

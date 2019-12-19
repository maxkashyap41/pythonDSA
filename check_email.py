import re

regex = ('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')

def check(email):
    if(re.search(regex, email)):
        print("\nValid Email Address")
    else:
        print("\nInvalid Email Address")

if __name__ == "__main__":
    email = "mags.041@gmail.com"
    check(email)

    email1 = "loyal.traitor@gmail.com"
    check(email1)

    email2 = "onu_gu_raj.kappu.420.com"
    check(email2)

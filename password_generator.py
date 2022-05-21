from StringPassword import StringPassword
import random


lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
specialChar = "+*ç%&/()=?`^à¨è-.,:_><"
numbers = "0123456789"


def build_string():
    return StringPassword(lowerCase, upperCase, specialChar, numbers)


def generate_password(string_for_password, maxNumberOfChars):
    password_string_final = ""
    tmp = str(string_for_password)
    for i in range(1,maxNumberOfChars):
        password_string_final = password_string_final + tmp[random.randint(0, len(tmp)-1)]
    print("your generated password: "+password_string_final)
    #return password_string_final

def change_message():
    message.value = "You pressed the button!"


if __name__ == "__main__":
    generate_password(build_string(), 16)
    
from StringPassword import StringPassword
import random


# all the chars (as string) for generating the string
lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
specialChar = "+*ç%&/()=?`^à¨è-.,:_><"
numbers = "0123456789"

# build a string with all the chars
def build_string():
    return StringPassword(lowerCase, upperCase, specialChar, numbers)

# generate a random number and take the corresponding char of the string
def generate_password(string_for_password, maxNumberOfChars):
    password_string_final = ""
    tmp = str(string_for_password)
    for i in range(0,maxNumberOfChars):
        password_string_final = password_string_final + tmp[random.randint(0, len(tmp)-1)]
    print("your generated password: "+password_string_final)
    return password_string_final

# read the words file
def build_word_password():
    lines = []
    with open('python\GUI-PasswordGenerator\list\words.txt','r') as file_words:
        lines = file_words.readlines()
    #print(lines[50000])
    file_words.close
    return lines
    

# generate a random value and pick the words at the corresponding line.
def generate_word_password(lines, numberOfWords):
    #TODO: set number of lines automatically
    lines_length = 370105
    word_password_final = []
    word_password_string_final = ""
    for i in range(0,numberOfWords):
        line = ""
        random_value = random.randint(0, lines_length)
        line = lines[random_value]
        word_password_final.append(lines[random_value])
        #for debugging
        print("line ",str(i+1), "random number ", str(random_value), "word: ", line )
    for i in range(0,len(word_password_final)):
        word_password_string_final = word_password_string_final+"-"+word_password_final[i].strip('\n')
    #for debugging
    print(word_password_string_final)
    return word_password_string_final

#main
if __name__ == "__main__":
    generate_password(build_string(), 16)
    generate_word_password(build_word_password(),4)
    
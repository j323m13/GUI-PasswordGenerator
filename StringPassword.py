class StringPassword:
    
    
    def __init__(self, lowerCase, upperCase, specialChar, numbers):
        string_password = ""
        self.lowerCase = lowerCase
        self.upperCase = upperCase
        self.specialChar = specialChar
        self.numbers = numbers
        string_password = string_password+self.lowerCase+self.upperCase+self.specialChar+self.numbers
        print(string_password)

    def __getattribute__(self, __name: str) -> any:
        pass
        



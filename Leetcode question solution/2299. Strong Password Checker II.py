#question

# 2299. Strong Password Checker II

# A password is said to be strong if it satisfies all the following criteria:
# It has at least 8 characters.
# It contains at least one lowercase letter.
# It contains at least one uppercase letter.
# It contains at least one digit.
# It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
# It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
# Given a string password, return true if it is a strong password. Otherwise, return false.


#solution

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        n = len(password)
        hasLower = False
        hasUpper = False
        hasDigit = False
        specialChar = False
        spcl_char= "!@#$%^&*()-+"
        for i in range(n):
            if password[i].islower():
                hasLower = True
            if password[i].isupper():
                hasUpper = True
            if password[i].isdigit():
                hasDigit = True
            if password[i] in spcl_char:
                specialChar = True
        for i in range(1,n):
            if(password[i-1]==password[i]):
                return False
        if (hasLower and hasUpper and hasDigit and specialChar and n >= 8):
            return True
        else:
            return False
        


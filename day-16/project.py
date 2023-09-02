import string

# Password Checker Project

# 1. Get password input.
# 2. Check if the password is in lowercase, uppercase, number
# or specail character.
# 3. If the password doesn't meet all the four conditions,
#  then reject the password with the conditions they doesn't met.
# 4. Only accepts if all the four conditions are met.
# 5. add a condition to check all that password length is greater
#  than 9 digits. If 9 or less, it fails.

psd = input("Enter Your Password: ")
psd_list = list(psd)

qualifications = ["lowercase", "uppercase", "digits", "special character"]


for char in psd_list:
    if char in string.ascii_lowercase:
        if "lowercase" in qualifications:
            qualifications.remove("lowercase")
    elif char in string.ascii_uppercase:
        if "uppercase" in qualifications:
            qualifications.remove("uppercase")
    elif char in string.digits:
        if "digits" in qualifications:
            qualifications.remove("digits")
    else:
        if "special character" in qualifications:
            qualifications.remove("special character")


if len(qualifications) == 0 and len(psd_list) > 9:
    print("Your Password is strong. Good Job!!")


if len(psd_list) <= 9:
    print("Password length must be greater than 9")


if len(qualifications) != 0:
    print("The password is not strong enough. The following conditons are "
          "not met: " + ", ".join(qualifications))

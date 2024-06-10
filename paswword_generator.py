import random,sys,string
def gen_password(length):
    if length<4:
        print("password should contain at least 4 charectors")
        sys.exit (0)
    else:
        upper_case=string.ascii_uppercase
        lower_case=string.ascii_lowercase
        special_char=string.punctuation
        number=string.digits

        password=[random.choice(upper_case)+random.choice(lower_case)+random.choice(special_char)+random.choice(number)]
        combo_char=upper_case+lower_case+special_char+number
        password+=random.choices(combo_char,k=length-4)
        random.shuffle(password)
    return "".join(password)
n=int(input("Enter the password length:"))
password=gen_password(n)
print("suggested password is:",password)



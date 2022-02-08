import random
import string

def password_generator(user_input = int(input("How strong you want your password: "))):
    if user_input >= 8:

        special_characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(special_characters)
                       for i in range(user_input))
    else :
        password_list = ["Default","Welcome123","ChangePassword"]
        password = random.choice(password_list)
        return password



print(password_generator())
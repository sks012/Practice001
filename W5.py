'''
AIM:Generate a random password with at least one special characters @,$ and one number, at list one capital letter
    and total length of 8 
'''

import random
import string

cap_letters=string.ascii_uppercase
numbers=string.digits
special_char1='@'
special_char2='$'
random_password=random.choice(numbers) + random.choice(cap_letters) + random.choice(special_char1) + random.choice(special_char2)
#final_password=''.join(random.choices(random_password))
for i in range(8):
    final_password=''.join(random.choice(random_password))
    print(final_password,end='')
import random
import string
charvalues=string.digits+string.ascii_letters+string.punctuation
password=""

for i in range(1,7):
    password+=random.choice(charvalues)
print(password)
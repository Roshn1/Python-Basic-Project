'''import secrets
import string

alphabet = string.ascii_letters + string.digits
otp = ''.join(secrets.choice(alphabet) for i in range(6))

print(otp)'''

import random
st = "0123456789"
l = 5
a = "".join(random.sample(st,l))
print("Your OTP : ",a)

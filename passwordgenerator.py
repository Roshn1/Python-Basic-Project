import random
st = "0123456789QWERTYUIOPASDFGHJKLZXCVBNM@!#$%^&*()qwertyuiopasdfghjklzxcvbnm"
l = 8
a = "".join(random.sample(st,l))
print("Your new password is generated ", a)


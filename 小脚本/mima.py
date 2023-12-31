import random
import string

all_characters = string.ascii_letters + string.digits + string.punctuation
print

# 生成指定长度的随机密码
password_length = 10
random_password = "".join(random.choice(all_characters) for i in range(password_length))


# 打印随机密码
print(random_password)

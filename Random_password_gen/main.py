#Random password Gen
import random



lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVW"
number = "0123456789"
symbol = "!@#$%^&*()<>:;?/,~`"
length = 9 # whatever length you want i chose 9
all = lower + upper + number + symbol

all = "".join(random.sample(all, length))

print("New password is ", str(all))
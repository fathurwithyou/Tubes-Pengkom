import random
from faker import Faker

print([("".join([str(random.randint(0, 9)) for i in range(20)]), round(
    random.choice([20000, 50000, 100000, 200000, 500000])/1352, 1)) for i in range(20)])

# for i in range(11):
#   s = "08" + random.choice(["5","9","8"]) + "".join([str(random.randint(0,9)) for i in range(8)])
#   print(s)

# fake = Faker()
# for i in range(20):
#   print(fake.email())

# for i in range(30):
#   print(random.randint(50,100))

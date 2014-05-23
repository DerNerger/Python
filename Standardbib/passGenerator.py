import random
import string
def id_generator(size=8 , chars=string.letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

print id_generator()

import random

r = random.randint(1, 100)

if r % 2 == 0:
    print('O número {} é PAR'.format(r))
else:
    print('O número {} é ÍMPAR'.format(r))


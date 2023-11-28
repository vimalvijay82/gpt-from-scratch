adds = []
for i in range(500):
    for j in range(500):
        # save f"{i}+{j}={i+j}\n" to addition.txt
        adds.append(f"{i}+{j}={i+j}\n")
# shuffle
import random
random.shuffle(adds)
str = ''.join(adds)
with open('addition.txt', 'w') as f:
    f.write(str)
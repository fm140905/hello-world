# import random

# f = open('integers.txt', 'w')
# for _ in range(500):
#     f.write(str(random.randint(1, 500)) + '\n')
# f.close()

f1 = open('bin6.txt', 'r')
f2 = open('bin61.txt', 'w')
index = 1
for line in f1:
    line = line.strip()
    # summ += int(line)
    if index % 160 == 0:
        f2.write(line + '\n')
    else:
        f2.write(line + ",")
    index += 1
print(index)
print((index-1)/160)
f1.close()
f2.close

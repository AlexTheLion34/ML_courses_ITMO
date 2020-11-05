import math

p_1 = (28, 10, 1)
p_2 = (49, 49, 1)
p_3 = (48, 35, 0)
p_4 = (36, 33, 1)
p_5 = (45, 54, 0)

l_p = [p_1, p_2, p_3, p_4, p_5]

p = (33, 47)

l_1 = []

for i in range(5):
    l_1.append((math.sqrt((p[0] - l_p[i][0])**2 + (p[1] - l_p[i][1])**2), l_p[i]))

l_2 = []

for i in range(5):
    l_2.append((abs((p[0] - l_p[i][0])) + abs((p[1] - l_p[i][1])), l_p[i]))

l_3 = []

for i in range(5):
    l_3.append((max(abs((p[0] - l_p[i][0])), abs((p[1] - l_p[i][1]))), l_p[i]))

print('Euclid distances sorted: ' + str(sorted(l_1)))
print('Manhattan distances sorted: ' + str(sorted(l_2)))
print('Chebyshev distances sorted: ' + str(sorted(l_3)))

l_4 = []

for a, b in l_1:
    l_4.append((1/(a**2), b))

sum_0 = 0
sum_1 = 0

for a, b in l_4:
    if b[2] == 0:
        sum_0 += a
    else:
        sum_1 += a

print('Sum of weights for class 0: ' + str(sum_0))
print('Sum of weights for class 1: ' + str(sum_1))

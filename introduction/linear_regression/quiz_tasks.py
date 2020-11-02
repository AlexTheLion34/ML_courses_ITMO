import math

theta_1 = ((13 - 12) * (8 - 8.5) + (4 - 12) * (5 - 8.5) + (11 - 12) * (6 - 8.5) + (20 - 12) * (15 - 8.5)) / (
        (13 - 12) ** 2 + (4 - 12) ** 2 + (11 - 12) ** 2 + (20 - 12) ** 2)
theta_0 = 8.5 - theta_1 * 12

print(theta_1)
print(theta_0)

se_theta_0 = math.sqrt(((8 - theta_0 - theta_1 * 13) ** 2 + (6 - theta_0 - theta_1 * 11) ** 2 +
                        (5 - theta_0 - theta_1 * 4) ** 2 + (15 - theta_0 - theta_1 * 20) ** 2) / (4 - 2)) * math.sqrt(
    1 / 4 + 12 ** 2 / ((13 - 12) ** 2 + (4 - 12) ** 2 + (11 - 12) ** 2 + (20 - 12) ** 2)
)

se_theta_1 = math.sqrt(((8 - theta_0 - theta_1 * 13) ** 2 + (6 - theta_0 - theta_1 * 11) ** 2 +
                        (5 - theta_0 - theta_1 * 4) ** 2 + (15 - theta_0 - theta_1 * 20) ** 2) / (4 - 2)) * math.sqrt(
    1 / ((13 - 12) ** 2 + (4 - 12) ** 2 + (11 - 12) ** 2 + (20 - 12) ** 2)
)

print(se_theta_0)
print(se_theta_1)

theta_0_min = theta_0 - 4.303 * se_theta_0
theta_0_max = theta_0 + 4.303 * se_theta_0

print(str(theta_0_min) + ';' + str(theta_0_max))

theta_1_min = theta_1 - 4.303 * se_theta_1
theta_1_max = theta_1 + 4.303 * se_theta_1

print(str(theta_1_min) + ';' + str(theta_1_max))

t = theta_1 / se_theta_1

print(t)

rse = math.sqrt(1 / (4 - 2) * ((8 - theta_0 - theta_1 * 13) ** 2 + (6 - theta_0 - theta_1 * 11) ** 2 +
                               (5 - theta_0 - theta_1 * 4) ** 2 + (15 - theta_0 - theta_1 * 20) ** 2))

print(rse)

r_2 = 1 - ((8 - theta_0 - theta_1 * 13) ** 2 + (6 - theta_0 - theta_1 * 11) ** 2 +
           (5 - theta_0 - theta_1 * 4) ** 2 + (15 - theta_0 - theta_1 * 20) ** 2) / \
      ((8 - 8.5) ** 2 + (5 - 8.5) ** 2 + (6 - 8.5) ** 2 + (15 - 8.5) ** 2)

print(r_2)

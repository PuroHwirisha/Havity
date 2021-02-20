# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 22:54:35 2021
Roll a fair six sided die
@author: Prosper_M
"""

import random

random.seed(20)
# face frequency counters
side1_Frequency = 0
side2_Frequency = 0
side3_Frequency = 0
side4_Frequency = 0
side5_Frequency = 0
side6_Frequency = 0

# roll the die 6 million times
n = 6_000_000
for roll in range(n):  # the underscore separators are for readability
    side = random.randrange(1, 7)

    # increment the respective face counter/frequency
    if side == 1:
        side1_Frequency += 1
    elif side == 2:
        side2_Frequency += 1
    elif side == 3:
        side3_Frequency += 1
    elif side == 4:
        side4_Frequency += 1
    elif side == 5:
        side5_Frequency += 1
    elif side == 6:
        side6_Frequency += 1
# copmute %
p1 = side1_Frequency / n * 100
p2 = side2_Frequency / n * 100
p3 = side3_Frequency / n * 100
p4 = side4_Frequency / n * 100
p5 = side5_Frequency / n * 100
p6 = side6_Frequency / n * 100

print(f'Face{"Frequency":>13}{"%":>6}')
print(f'{1:>4}{side1_Frequency:>13}{p1:>8.2f}')
print(f'{2:>4}{side2_Frequency:>13}{p2:>8.2f}')
print(f'{3:>4}{side3_Frequency:>13}{p3:>8.2f}')
print(f'{4:>4}{side4_Frequency:>13}{p4:>8.2f}')
print(f'{5:>4}{side5_Frequency:>13}{p5:>8.2f}')
print(f'{6:>4}{side6_Frequency:>13}{p6:>8.2f}')

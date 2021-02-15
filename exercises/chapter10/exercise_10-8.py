import random

def bd_paradox(num_people):
    bd_list = []
    for i in range(num_people):
        rnd_bd = random.randint(0, 365)
        bd_list.append(rnd_bd)
    if any(bd_list.count(i) > 1 for i in bd_list):
        return True


num_people = 70
bd_match_count = 0
for i in range(100):
    if bd_paradox(num_people):
        bd_match_count += 1
print('Propability: ' + str(bd_match_count/100))

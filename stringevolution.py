import string
import random

target = str(raw_input('enter desired string: '))

strings = []
reward = []

currentGeneration = 0
NUM_PER_GENERATION = 10
MUTATION_RATE = 0.05


def is_done():
    return strings[0] == target

def sort():
    for i in range(len(strings)):
        biggest = i
        for j in range(i, len(strings)):
            if reward[j] > reward[i]:
                biggest = j
        if biggest != i:
            t1 = reward[i]
            t2 = strings[i]
            reward[i] = reward[biggest]
            strings[i] = strings[biggest]
            reward[biggest] = t1
            strings[biggest] = t2


def determine_reward():
    for i in range(len(strings)):
        r = 0
        for j in range(len(target)):
            if target[j] in strings[i]:
                r += 2
            if target[j] == strings[i][j]:
                r += 6
        reward[i] = r


def breed(str1, str2):
    c = ""
    for i in range(len(str1)):
        if random.random() < MUTATION_RATE:
            c += random.choice(string.ascii_letters + ' ')
        elif random.random() < 2 * MUTATION_RATE:
            c += random.choice(str1 + str2)
        else:
            c += random.choice(str1[i] + str2[i])
    return c

for i in range(NUM_PER_GENERATION):
    strings.append("".join(random.choice(string.ascii_letters + ' ') for _ in range(len(target))))
    reward.append(0)

    print strings[i]

while not is_done():
    currentGeneration += 1
    determine_reward()
    sort()
    for i in range(NUM_PER_GENERATION / 2, NUM_PER_GENERATION):
        strings[i] = breed(strings[random.randint(0, NUM_PER_GENERATION / 2)], strings[random.randint(0, NUM_PER_GENERATION / 2)])
    for s in strings:
        print s

print "it took %d generations to evolve!" % currentGeneration

import random
import json


def rule1(word):
    return '{}U'.format(word)


def rule2(word):
    return 'M{}{}'.format(word[1:], word[1:])


def replace_u(split, index):
    i = 0
    result = ''
    for word in split:
        if i != index:
            result = '{}{}'.format(result, word)
        else:
            result = '{}U'.format(result)


def find_all_indexes(word, substring):
    result = []
    character = substring[0]

    for i in range(0, len(word) - 1 - len(substring)):
        if word[i] is character and word[i + 1] is character and word[i + 2] is character:
            result.append(i)

    return result


def replace(word, index, original, new):
    return '{}{}{}'.format(word[0:index], new, word[(index + len(original)):])


def rule3(word):
    result = []

    indexes = find_all_indexes(word, 'III')

    for index in indexes:
        result.append(replace(word, index, 'III', 'UU'))

    # split_words = word.split('III')
    # for part, count in zip(split_words, range(0, len(split_words))):
    #    result.append(replace_u(split_words, count))
    return result


def rule4(word):
    result = []

    indexes = find_all_indexes(word, 'UU')

    for index in indexes:
        result.append(replace(word, index, 'UU', ''))

    return result


def is_rule1_allowed(word):
    return word.endswith('I')


def is_rule2_allowed(word):
    return True


def is_rule3_allowed(word):
    return word.find('III') >= 0


def is_rule4_allowed(word):
    return word.find('UU') >= 0


axiom = 'MI'

solutions = dict()

solutions['MI'] = 'axiom'
tried = 0

while 'MU' not in solutions.keys() and tried < 100:
    next_theorem_index = random.randint(0, len(solutions))
    if next_theorem_index > 0:
        next_theorem_index = next_theorem_index - 1  # out of bounds...

    next_word = solutions.keys()[next_theorem_index]

    if len(next_word) < 50:
        if is_rule1_allowed(next_word):
            derived = rule1(next_word)
            if derived not in solutions.keys():
                solutions[derived] = '{}, R1'.format(solutions[next_word])

        if is_rule2_allowed(next_word):
            derived = rule2(next_word)
            if derived is not None and derived not in solutions.keys():
                solutions[derived] = '{}, R2'.format(solutions[next_word])

        if is_rule3_allowed(next_word):
            for derivation in rule3(next_word):
                if derivation not in solutions.keys():
                    solutions[derivation] = '{}, R3'.format(solutions[next_word])

        if is_rule4_allowed(next_word):
            for derivation in rule4(next_word):
                if derivation not in solutions.keys():
                    solutions[derivation] = '{}, R4'.format(solutions[next_word])

    tried = tried + 1

print json.dumps(solutions, indent=4, separators=(',', ': '))

print 'MU' in solutions.keys()  # just for the sake of checking.. if you wanna know if it is possible... try it yourself!

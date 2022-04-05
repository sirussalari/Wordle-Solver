import random
import time
import json
import sys
if bool(sys.argv[1]):
    noneArg = sys.argv[1].split(',')
else:
    noneArg = None
if bool(sys.argv[2]):
    matchArg = json.loads(sys.argv[2])
else:
    matchArg = None
if bool(sys.argv[3]):
    closeArg = json.loads(sys.argv[3])
else:
    closeArg = None
startTime = time.time()
with open('fiveLetter.txt') as file:
        words = file.readlines()
def wordle(none = noneArg, match = matchArg, close = closeArg):
    if match == None and close == None and none == None:
        top = len(words) - 1
        index = random.randint(0, top)
        word = words[index]
        chance = (1 / len(words)) * 100
        searchSpace = len(words)
        statement = 'Search space: ' + str(searchSpace) + ' words' + '\nThere is a ' + str(chance) + '% chance that the word is: ' + word
        return statement
    elif none and match and close:
        possible = []
        certain = []
        exact = []
        certainClose = []
        exactClose = []
        nothing = []
        for word in words:
            for key in close:
                if type(close[key]) == int:
                    indices = []
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    if close[key] not in indices:
                        possible.append(word)
                else:
                    indices = []
                    state = True
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    for j in indices:
                        if j in close[key]:
                            state = False
                    if state:
                        possible.append(word)
        for word in possible:
            for key in close:
                if key not in word:
                    certainClose.append(word)
        for word in certainClose:
            if word in possible:
                possible.remove(word)
        for word in possible:
            for key in close:
                if type(close[key]) == int:
                    indices = []
                    state = True
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    for j in indices:
                        if j == close[key]:
                            state = False
                    if state == False:
                        exact.append(word)
                else:
                    indices = []
                    state = True
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    for j in indices:
                        if j in close[key]:
                            state = False
                    if state == False:
                        exact.append(word)
        for word in exactClose:
            if word in possible:
                possible.remove(word) 
        for word in possible:
            for key in match:
                if key not in word:
                    certain.append(word)
                else:
                    if type(match[key]) == int:
                        if word[match[key]] != key:
                            exact.append(word)
                    else:
                        indices = []
                        for i in range(len(word)):
                            if word[i] == key:
                                indices.append(i)
                        if indices != match[key]:
                            exact.append(word)
        for word in certain:
            if word in possible:
                possible.remove(word)
        for word in exact:
            if word in possible:
                possible.remove(word)
        for word in possible:
            for letter in none:
                if letter in word:
                    nothing.append(word)
        for word in nothing:
            if word in possible:
                possible.remove(word)
        singles = set(possible)
        final = []
        for word in singles:
            final.append(word)
        top = len(final) - 1
        index = random.randint(0, top)
        word = final[index]
        chance = (1 / len(final)) * 100
        searchSpace = len(final)
        statement = 'Search space: ' + str(searchSpace) + ' words' + '\nThere is a ' + str(chance) + '% chance that the word is: ' + word
        return statement
    elif match and close:
        possible = []
        certain = []
        exact = []
        certainClose = []
        exactClose = []
        for word in words:
            for key in close:
                if type(close[key]) == int:
                    indices = []
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    if close[key] not in indices:
                        possible.append(word)
                else:
                    indices = []
                    state = True
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    for j in indices:
                        if j in close[key]:
                            state = False
                    if state:
                        possible.append(word)
        for word in possible:
            for key in close:
                if key not in word:
                    certainClose.append(word)
        for word in certainClose:
            if word in possible:
                possible.remove(word)
        for word in possible:
            for key in close:
                if type(close[key]) == int:
                    indices = []
                    state = True
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    for j in indices:
                        if j == close[key]:
                            state = False
                    if state == False:
                        exact.append(word)
                else:
                    indices = []
                    state = True
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    for j in indices:
                        if j in close[key]:
                            state = False
                    if state == False:
                        exact.append(word)
        for word in exactClose:
            if word in possible:
                possible.remove(word)
        for word in possible:
            for key in match:
                if key not in word:
                    certain.append(word)
        for word in certain:
            if word in possible:
                possible.remove(word)
        for word in possible:
            for key in match:
                if type(match[key]) == int:
                     if key in word and word[match[key]] != key:
                        exact.append(word)
                else:
                    indices = []
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    if indices != match[key]:
                        exact.append(word)
        for word in exact:
            if word in possible:
                possible.remove(word)
        final = []
        singles = set(possible)
        for word in singles:
            final.append(word)
        top = len(word) - 1
        index = random.randint(0, top)
        word = final[index]
        chance = (1 / len(final)) * 100
        searchSpace = len(final)
        statement = 'Search space: ' + str(searchSpace) + ' words' + '\nThere is a ' + str(chance) + '% chance that the word is: ' + word
        return statement
    elif match and none:
        possible = []
        certain = []
        exact = []
        nothing = []
        for word in words:
            for key in match:
                if type(match[key]) == int:
                    if key in word and word[match[key]] == key:
                        possible.append(word)
                else:
                    if key in word:
                        indices = []
                        for i in range(len(word)):
                            if word[i] == key:
                                indices.append(i)
                        if indices == match[key]:
                            possible.append(word)
        for word in possible:
            for key in match:
                if key not in word:
                    certain.append(word)
        for word in certain:
            if word in possible:
                possible.remove(word)
        for word in possible:
            for key in match:
                if type(match[key]) == int:
                    if word[match[key]] != key:
                        exact.append(word)
                else:
                    indices = []
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    if indices != match[key]:
                        exact.append(word)
        for word in exact:
            if word in possible:
                possible.remove(word)
        for word in possible:
            for letter in none:
                if letter in word:
                    nothing.append(word)
        for word in nothing:
            if word in possible:
                possible.remove(word)
        final = []
        singles = set(possible)
        for word in singles:
            final.append(word)
        top = len(final) - 1
        index = random.randint(0, top)
        word = final[index]
        chance = (1 / len(final)) * 100
        searchSpace = len(final)
        statement = 'Search space: ' + str(searchSpace) + ' words' + '\nThere is a ' + str(chance) + '% chance that the word is: ' + word
        return statement
    elif close and none:
        possible = []
        certain = []
        exact = []
        nothing = []
        for word in words:
            for key in close:
                if type(close[key]) == int:
                    indices = []
                    state = True
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    for j in indices:
                        if j == close[key]:
                            state = False
                    if state:
                        possible.append(word)
                else:
                    indices = []
                    state = True
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    for j in indices:
                        if j in close[key]:
                            state = False
                    if state:
                        possible.append(word)
        for word in possible:
            for key in close:
                if key not in word:
                    certain.append(word)
        for word in certain:
            if word in possible:
                possible.remove(word)
        for word in possible:
            for key in close:
                if type(close[key]) == int:
                    indices = []
                    state = True
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    for j in indices:
                        if j == close[key]:
                            state = False
                    if state == False:
                        exact.append(word)
                else:
                    indices = []
                    state = True
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    for j in indices:
                        if j in close[key]:
                            state = False
                    if state == False:
                        exact.append(word)
        for word in exact:
            if word in possible:
                possible.remove(word)
        for word in possible:
            for letter in none:
                if letter in word:
                    nothing.append(word)
        for word in nothing:
            if word in possible:
                possible.remove(word)
        final = []
        singles = set(possible)
        for word in singles:
            final.append(word)
        top = len(final) - 1
        index = random.randint(0, top)
        word = final[index]
        chance = (1 / len(final)) * 100
        searchSpace = len(final)
        statement = 'Search space: ' + str(searchSpace) + ' words' + '\nThere is a ' + str(chance) + '% chance that the word is: ' + word
        return statement
    elif none:
        possible = []
        nothing = []
        for word in words:
            for letter in none:
                if letter not in word:
                    possible.append(word)
                    break
        for word in possible:
            for letter in none:
                if letter in word:
                    nothing.append(word)
                    break
        for word in nothing:
            if word in possible:
                possible.remove(word)
        final = []
        singles = set(possible)
        for word in singles:
            final.append(word)
        top = len(final) - 1
        index = random.randint(0, top)
        word = final[index]
        chance = (1 / len(final)) * 100
        searchSpace = len(final)
        statement = 'Search space: ' + str(searchSpace) + ' words' + '\nThere is a ' + str(chance) + '% chance that the word is: ' + word
        return statement
    elif match:
        possible = []
        certain = []
        exact = []
        for word in words:
            for key in match:
                if type(match[key]) == int:
                     if key in word and word[match[key]] == key:
                        possible.append(word)
                else:
                    if key in word:
                        indices = []
                        for i in range(len(word)):
                            if word[i] == key:
                                indices.append(i)
                        if indices == match[key]:
                            possible.append(word)
        for word in possible:
            for key in match:
                if key not in word:
                    certain.append(word)
        for word in certain:
            if word in possible:
                possible.remove(word)
        for word in possible:
            for key in match:
                if type(match[key]) == int:
                    if word[match[key]] != key:
                        exact.append(word)
                else:
                    indices = []
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    if indices != match[key]:
                        exact.append(word)
        for word in exact:
            if word in possible:
                possible.remove(word)
        final = []
        singles = set(possible)
        for word in singles:
            final.append(word)
        top = len(final) - 1
        index = random.randint(0, top)
        word = final[index]
        chance = (1 / len(final)) * 100
        searchSpace = len(final)
        statement = 'Search space: ' + str(searchSpace) + ' words' + '\nThere is a ' + str(chance) + '% chance that the word is: ' + word
        return statement
    elif close:
        possible = []
        certain = []
        exact = []
        for word in words:
            for key in close:
                if type(close[key]) == int:
                    indices = []
                    state = True
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    for j in indices:
                        if j == close[key]:
                            state = False
                    if state:
                        possible.append(word)
                else:
                    indices = []
                    state = True
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    for j in indices:
                        if j in close[key]:
                            state = False
                    if state:
                        possible.append(word)
        for word in possible:
            if key not in word:
                certain.append(word)
        for word in certain:
            if word in possible:
                possible.remove(word)
        for word in possible:
            for key in close:
                if type(close[key]) == int:
                    indices = []
                    state = True
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    for j in indices:
                        if j == close[key]:
                            state = False
                    if state == False:
                        exact.append(word)
                else:
                    indices = []
                    state = True
                    for i in range(len(word)):
                        if word[i] == key:
                            indices.append(i)
                    for j in indices:
                        if j in close[key]:
                            state = False
                    if state == False:
                        exact.append(word)
        for word in exact:
            if word in possible:
                possible.remove(word)
        final = []
        singles = set(possible)
        for word in singles:
            final.append(word)
        top = len(final) - 1
        index = random.randint(0, top)
        word = final[index]
        chance = (1 / len(final)) * 100
        searchSpace = len(final)
        statement = 'Search space: ' + str(searchSpace) + ' words' + '\nThere is a ' + str(chance) + '% chance that the word is: ' + word
        return statement    
print(wordle())
runTime = time.time() - startTime
print('Runtime: ', runTime, 'seconds')
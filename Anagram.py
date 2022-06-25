def anagrams(ana, gra):
    found = False
    deter = ""
    x = []
    for word in gra:
        for letter in word:
            if letter in ana:
                found = True
            else:
                found = False
                break
        if found:
            x.append(word)
    return x

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
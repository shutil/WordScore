a = "programming is awesome"
vowels = ["a","e","i","o","u"]
def wordScore(str):
    a = str
    i = 0

    b = a.split(" ")

    for x in b:
        z = []
        for y in x:
            if y in vowels:
                z.append(y)
        else:
            pass
        num = len(z)
        if num % 2 == 0:
            i += 2
        else:
            i += 1
        

    return i


print(wordScore("programming is awesome"))
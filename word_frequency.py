import sys

DROP_CHARS = "."
DROP_DICT = dict([(c, "") for c in DROP_CHARS])
DROP_TABLE = str.maketrans(DROP_DICT)


def word_frequency(stream):
    word_dict = {}
    for line in stream:
        for word in line.translate(DROP_TABLE).split(" "):
            word = word.upper()
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    return word_dict


for (key, value) in sorted(word_frequency(open("mbox-short.txt").readlines()).items(), key=lambda x:(x[1], x[0]), reverse=True):
    print(key + " = " + str(value))
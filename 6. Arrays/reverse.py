s = "Hi my name is Vansh"


def reverse(string):
    rev_s = ""
    for i in range(len(string) - 1, -1, -1):
        rev_s = rev_s + string[i]
    print(rev_s)


# reverse(s)


def reverse2(string):
    rev_s = []
    for i in range(len(string) - 1, -1, -1):
        rev_s.append(string[i])
    return "".join(rev_s)


# print(reverse2(s))


def reverse3(string):
    rev_s = []
    for i in range(len(string)):
        rev_s.append(string[i])
    rev_s.reverse()
    return "".join(rev_s)


# print(reverse3(s))


def reverse4(string):
    rev_s = list(string)
    rev_s.reverse()
    return "".join(rev_s)


# print(reverse4(s))


def swap(string, a, b):
    string = list(string)
    temp = string[a]
    string[a] = string[b]
    string[b] = temp
    return ''.join(string)


def reverse5(string):
    for i in range(len(string) // 2):
        string = swap(string, i, len(string) - i - 1)
    return string


print(reverse5(s))

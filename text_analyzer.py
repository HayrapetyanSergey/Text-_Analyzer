def count_of_words(filepath):
    with open(filepath, "r") as file:
        lst = [file.read()]
        word = lst[0].split(" ")
    return len(word)

def count_of_letters(filepath):
    single_letters = []
    with open(filepath, "r") as file:
        lst = [row for row in file.read()]
        for i in range(len(lst)):
            if lst[i] not in single_letters and lst[i].isalnum():
                single_letters.append(lst[i])
        return len(single_letters)

def count_of_sentences(filepath):
    with open(filepath, "r") as file:
        lst = [row.strip() for row in file.read()]
        count_1 = lst.count(".")
        count_2 = lst.count('?')
        count_3 = lst.count('!')
        return count_1 + count_2 + count_3

def common_word(filepath):
    count_single_words = []
    single_words = []
    with open(filepath, "r") as file:
        lst = [file.read()]
        words = lst[0].split(" ")
        for i in range(len(words)):
            if words[i] not in single_words:
                single_words.append(words[i])
                count_single_words.append(words.count(words[i]))
        common = max(count_single_words)
        if common != 1:
            ind = count_single_words.index(common) 
            return single_words[ind]
        elif common == 1:
            return 0

def common_letters(filepath):
    count_of_letters = []
    single_letters = []
    with open(filepath, "r") as file:
        lst = [row for row in file.read()]
        for i in range(len(lst)):
            if lst[i] not in single_letters and lst[i].isalnum():
                single_letters.append(lst[i])
                count_of_letters.append(lst.count(lst[i]))
        common = max(count_of_letters)
        if common != 1:
            ind = count_of_letters.index(common)
            return single_letters[ind]
        else:
            return 0

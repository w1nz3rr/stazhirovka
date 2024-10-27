def combine_anagrams(words_array):
    res = {}

    for word in words_array:
        sorted_word = str(sorted(word))

        if sorted_word in res:
            res[sorted_word].append(word)
        else:
            res[sorted_word] = [word]

    return list(res.values())



result = combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream" ])
print(result)

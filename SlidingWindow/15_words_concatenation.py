from collections import Counter


def words_concatenation(str: str, words: list):
    if len(words) == 0 or len(words[0]) == 0:
        return []

    word_frequency = Counter(words)

    result = []
    words_count = len(words)
    word_len = len(words[0])

    for i in range(len(str) - words_count * word_len + 1):
        words_seen = {}

        for j in range(words_count):
            next_word_index = i + j * word_len

            word = str[next_word_index: next_word_index + word_len]
            if word not in word_frequency:
                break

            words_seen[word] = words_seen.get(word, 0) + 1

            if words_seen[word] > word_frequency[word]:
                break

            if j + 1 == words_count:
                result.append(i)

    return result


if __name__ == '__main__':
    print(words_concatenation("catfoxcat", ["cat", "fox"]))
    print(words_concatenation("catcatfoxfox", ["cat", "fox"]))

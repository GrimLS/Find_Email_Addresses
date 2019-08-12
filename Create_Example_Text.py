import random
import urllib.request


def Create_Sample_Email_Address_Text(length):
    word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = urllib.request.urlopen(word_url)
    long_txt = response.read().decode()
    words = long_txt.splitlines()

    with open("Sample.txt", "w") as text:
        random_words = list()
        print(words)
        words_length = len(words)
        for i in range(length):
            random_words.append(words[random.randint(0, words_length)])
            if i % 10 == 0 and i != 0:
                random_words.append("\n")
            if random.randint(0, 10) == 5:
                random_words.append(words[random.randint(0, words_length)] + "@" + words[random.randint(0, words_length)] + ".com")
        random_words = " ".join(random_words)
        text.write(random_words)
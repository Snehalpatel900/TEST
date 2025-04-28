text = """a b c a a b"""
print (text)
#print(len(text))
#print(text.split())
#print(len(text.split()))

word_count = {}
for word in text.split():
    print(word)
    word_count[word] = 1
    print(word_count)
    if word_count[word] == 1:
        word_count[word] = word_count[word] + 1
        print(word_count)
    else:
        word_count[word] = 1
        print(word_count)
print(word_count)


count = int(input())
synonyms_dict = dict()

for _ in range(count):
    word = input()
    synonym = input()
    if word in synonyms_dict:
        synonyms_dict[word].append(synonym)
    else:
        synonyms_dict[word] = [synonym]

for key, value in synonyms_dict.items():
    print(f"{key} - {', '.join(value)}")

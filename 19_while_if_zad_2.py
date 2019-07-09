texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

i = 0
dlug = len(texts)-1

while i < dlug:
    print(i, texts[i], texts[i+1])

    if len(texts[i]) == len(texts[i+1]):
        print("\tFound!", texts[i], texts[i+1])

    i = i+1
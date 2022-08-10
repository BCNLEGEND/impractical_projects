"""Find all word-pair palingrams in a dictionary file"""
from load_dict import load
import time

start_time = time.time()

word_list = set(load('./2of4brif.txt'))

def find_palingrams():
    """Find dictionary palingrams"""
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[:end-i]))
    return pali_list

palingrams = find_palingrams()

sorted_palingrams = sorted(palingrams)

for first, second in sorted_palingrams:
    print(f'{first} {second}')

print(f'Number of palingrams: {len(sorted_palingrams)}')

end_time = time.time()
print(f'Runtime for this program was {end_time - start_time} seconds.')

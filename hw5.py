
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
import csv
import json
import pickle
import string

def main(filename):
    txtfile = open(filename)
    lines = txtfile.readlines()
    all_words = []

    for line in lines:
        line =line.strip()
        words = line.split()

        for word in words:
            word = word.strip(string.punctuation)
            if word:
                all_words.append(word)

    from collections import Counter
    counter = Counter(all_words)

    with open("wordcount.csv", "w") as csv_file:
        # create a csv writer from a file object (or descriptor)
        writer = csv.writer(csv_file,delimiter=',')
        # write table head
        writer.writerow(['word', 'count'])
        # write all (word, count) pair into the csv writer
        writer.writerows(counter.most_common())

    # dump to a json file named "wordcount.json"
    with open('wordcount.json','w') as json_file:
        json.dump(counter,json_file)

    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly
    pickle.dump(counter,open("wordcount.pkl","wb"))

if __name__ == '__main__':
    main("i_have_a_dream.txt")


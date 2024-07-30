with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('/n')

for i in range(len(words_list)):
    words_list[i] = words_list[i].split('#')

word_dict = {}    

for w in words_list:
    word_dict[w[1]] = [int(w[0]),w[2]]
print(word_dict)
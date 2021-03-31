word = input().upper()
word_set = list(set(word))

cnt_list = []

for i in word_set:
    cnt = word.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(word_set[max_index])



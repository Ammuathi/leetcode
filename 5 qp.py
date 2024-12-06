words=['apple','banana','apple','orange','banana','apple']
print(type(words))
word_count ={word:len(list(filter(lambda x:x== word,words)))for word in set(words)}
print(word_count)
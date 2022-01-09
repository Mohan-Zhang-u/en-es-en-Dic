import codecs
import pickle

chars = ['']

for i in range(32, 256): # 512
    c = chr(i)
    if c not in chars:
        chars.append(c)

en_es = open('src/main/resources/dic/en-es.xml').read()
for c in en_es:
    if c not in chars:
        print(c)
        chars.append(c)

es_en = open('src/main/resources/dic/en-es.xml').read()
for c in es_en:
    if c not in chars:
        print(c)
        chars.append(c)
                
chars = sorted(chars)

# tmp_chars = chars
# chars = []
# for char in tmp_chars:
#     if en_es.count(char) + es_en.count(char) > 1:
#         chars.append(char)


for char in chars:
    try:
        print(ord(char))
    except:
        pass

with codecs.open('chars.txt', 'w+', encoding='utf-8') as fp:
    for char in chars:
        fp.writelines(char + '\n')
    
with open('chars.pkl', 'wb') as fp:
    pickle.dump(chars, fp)

import xmltodict
import pickle

l1_list = [] # en
l2_list = [] # es

d = xmltodict.parse(open('src/main/resources/dic/en-es.xml').read())
for l in range(26):
    ws = d['dic']['l'][l]['w']
    for w in ws:
        concept = w['c']
        description = w['d'] # oreja de mar {f}, abulón {m}, loco {m}
        typ = w['t']
        l1_w = concept # english
        if description:
            l2_w = description.split('{')[0]# spanish
            if l1_w and l2_w and (l1_w not in l1_list) and (l2_w not in l2_list):
                l1_list.append(l1_w)
                l2_list.append(l2_w)
            
with open('l1_list.pickle', 'wb') as fp:
    pickle.dump(l1_list, fp)
        
with open('l2_list.pickle', 'wb') as fp:
    pickle.dump(l2_list, fp)

with open('l1_list.txt', 'w+') as fp:
    for i in range(len(l1_list)):
        fp.write(l1_list[i] + '\n')

with open('l2_list.txt', 'w+') as fp:
    for i in range(len(l2_list)):
        fp.write(l2_list[i] + '\n')
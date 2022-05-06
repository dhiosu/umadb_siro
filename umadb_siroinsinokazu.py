import argparse

f = open('memo.txt', 'r')
data = f.read().split()


#parser = argparse.ArgumentParser(description='プログラムの説明')
#parser.add_argument('--db', nargs='*')
#args = parser.parse_args()
#print(type(args.db))
dict = {}
ID = ""
siro = -3
preID = 0
for i in data:
    if i.isdecimal():
        dict[preID] = siro
        preID = i
        ID = ""
        siro = -3
        ID = i
    else:
        pass
    if '（代表' in i:
        siro += 1
dict[preID] = siro
preID = i
removed_value = dict.pop(0)
print(dict)

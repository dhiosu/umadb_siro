import argparse
parser = argparse.ArgumentParser(description='プログラムの説明')
parser.add_argument('--db', nargs='*')
args = parser.parse_args()
#print(type(args.db))
dict = {}
ID = ""
siro = 0
preID = 0
for i in args.db:
    if i.isdecimal():
        dict[preID] = siro
        preID = i
        ID = ""
        siro = 0
        ID = i
    else:
        pass
    if '（代表' in i:
        siro += 1
print(dict)

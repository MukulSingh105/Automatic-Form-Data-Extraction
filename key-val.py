import re
import json

f = open("demofile.txt", "r")
str = (f.read())
opt = re.sub(r':|\)|\(|/?|\||\*|\.|>|-','', str)
opt = re.sub(r'[0-9] ','', opt)
print(opt)

dict = {}

for line in opt.split('\n'):
    if '@' in line:
        l = line.split('@')
        dict[l[0]] = l[1]

print(json.dumps(dict, sort_keys=True, indent=4))

import re

string = "123xxx123"
pattern = re.compile("\\d+|\\w{3}")
s = pattern.findall(string)





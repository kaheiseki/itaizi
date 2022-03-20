import sys
sys.dont_write_bytecode  = True
sys.path.append("../itaizi")
from list import itaizi_list

# TODO keyとvalueを持ってくる
key = ["hoge","hoge"]
value = ["hoge","hoge"]


with open("../itaizi/sample.py",mode = "w") as f:
  f.write("itaizi_list = {\n")
  for i in range(len(key)):
    if i != len(key) - 1:
      f.write("  \"" + key[i] + "\":\"" + value[i] + "\",\n")
    elif i == len(key) - 1:
      f.write("  \"" + key[i] + "\":\"" + value[i] + "\"\n") 
  f.write("}")
import sys
sys.dont_write_bytecode  = True
sys.path.append("../itaizi")
from list import itaizi_list

# TODO keyとvalueを持ってくる
key = ["hoge","hoge"]
value = ["hoge","hoge"]


with open("../itaizi/sample.py",mode = "w") as f:
  for i in range(len(key)):
    f.write(key[i] + ":" + value[i] + "\n")
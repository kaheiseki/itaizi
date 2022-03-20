import sys
sys.dont_write_bytecode  = True
sys.path.append("../itaizi")
from list import itaizi_list

# TODO keyとvalueを持ってくる
key = ["hoge","hoge"]
value = ["hoge","hoge"]


# 本番ではpathをsample.pyからlist.pyに変える
with open("../itaizi/sample.py",mode = "w") as f:
  f.write("itaizi_list = {\n")
  for index in range(len(key)):
    if index != len(key) - 1:
      f.write("  \"" + key[index] + "\":\"" + value[index] + "\",\n")
    elif index == len(key) - 1:
      f.write("  \"" + key[index] + "\":\"" + value[index] + "\"\n") 
  f.write("}")
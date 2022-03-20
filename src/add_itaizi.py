from socket import SO_VM_SOCKETS_BUFFER_MIN_SIZE
import sys
sys.dont_write_bytecode  = True
sys.path.append("../itaizi")
from list import itaizi_list

# TODO keyとvalueを持ってくる
itaizi = ["hoge","hoge"]
seizi = ["hoge","hoge"]


# 本番ではpathをsample.pyからlist.pyに変える
with open("../itaizi/sample.py",mode = "w") as f:
  f.write("itaizi_list = {\n")
  for index in range(len(itaizi)):
    if index != len(itaizi) - 1:
      f.write("  \"" + itaizi[index] + "\":\"" + seizi[index] + "\",\n")
    elif index == len(itaizi) - 1:
      f.write("  \"" + seizi[index] + "\":\"" + seizi[index] + "\"\n") 
  f.write("}")
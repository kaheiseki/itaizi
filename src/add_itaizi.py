import sys
sys.dont_write_bytecode  = True

# TODO itaiziとseiziに対応するリストをそれぞれ持ってくる
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
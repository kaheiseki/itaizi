from .list import itaizi_list

# 文字列中の異体字を正字に変換したものを返す関数
def to_seizi(string):
  text = ""
  for char in string:
    if char in itaizi_list:
      text += itaizi_list(char)
    else:
      text += char
  return text
  
# 文字列中の正字をい異体字に変換したものを返す関数
def to_itaizi(string):
  text = ""
  for char in string:
    if char in itaizi_list.values():
      for key,value in itaizi_list.items():
        if value == char:
          text += key
    else:
      text += char
  return text 
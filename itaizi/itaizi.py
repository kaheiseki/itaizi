from .list import itaizi_list

# 文字列中の異体字を正字に変換したものを返す関数
def to_seizi(string):
  text = ""
  for char in string:
    if char in itaizi_list:
      text += itaizi_list[char]
    else:
      text += char
  return text
  
# 文字列中の正字を異体字に変換したものを返す関数
def to_itaizi(string):
  text = ""
  for char in string:
    if char in itaizi_list.values():
      for key,value in itaizi_list.items():
        if value == char:
          text += key
          break
    else:
      text += char
  return text 

# 文字列中に異体字が含まれているかどうか確認する関数
def exist_itaizi(string):
  for char in string:
    if char in itaizi_list:
      return True
    else:
      return False
  
# 文字列中に含まれている異体字の数を数える関数
def count_itaizi(string):
  count = 0
  for char in string:
    if char in itaizi_list:
      count += 1
  return count
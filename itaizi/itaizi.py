from .list import itaizi_list

def to_seizi(char):
  if char in itaizi_list:
    return itaizi_list(char)
  else:
    return char
  

def to_itaizi(char):
  if char in itaizi_list.values():
    for key,value in itaizi_list.items():
      if value == char:
        return key
  else:
    return char
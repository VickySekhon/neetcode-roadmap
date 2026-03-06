def add_spaces(text):
     # new_t = ""
     # i = 0
     # while i < len(text)-1:
     #      if text[i].isalpha() and text[i+1].isalpha():
     #           new_t += text[i] + " " + text[i+1] + " "
     #           i += 2
     #      else:
     #           if not text[i].isalpha() and text[i+1].isalpha():
     #                new_t -= " "
     #                new_t += text[i]
                    
     #                new_t += text[i+1]
                    
     #           elif not text[i+1].isalpha() and text[i].isalpha():
                    
     #           else:
                    
     #           i += 1
               
     # print(i)
     # new_t += text[i:]
     # return f"'{new_t}'" 
     chars = list(text)
     new_s = ""

     for char in chars:
          if char.isalpha():
               new_s += f"{char} "
          else:
               if new_s == "":
                    new_s += char
               else:
                    if new_s[-1] == " ":
                         new_s = new_s.rstrip()
                    new_s += char
     return f"'{new_s.strip()}'"
     # chars = list(text)
     # new_s = ""
     # for char in chars:
     #      if char.isalpha():
     #           new_s += char + " "
     #      else:
     #           if new_s == "":
     #                new_s += char
     #           else:
     #                if new_s[-1] == " ":
     #                     new_s = new_s.rstrip()
     #                new_s += char
     # return f'"{new_s.rstrip()}"'
x = add_spaces("codingrocks!") # c o d i n g r o c k s!
x = add_spaces("!!codingrocks!") # !!c o d i n g r o c k s!
x = add_spaces("c!!codingrocks!") # c!!c o d i n g r o c k s!
#x = add_spaces("codingrocks") # c o d i n g r o c k s
print(x)
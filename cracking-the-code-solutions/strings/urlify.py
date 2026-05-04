def urlify(s, l):
     s = s.strip()
     new_s = ""
     
     for char in s:
          if char == " ":
               new_s += "%20"
          else:
               new_s += char
     return new_s

print(urlify("hello there mr vicky      ", 26))

# print(len("hello%20there%20mr%20vicky"))
# print(len("hello there mr vicky"))
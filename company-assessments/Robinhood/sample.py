def function(words, k):
     frequencies = {}

     for i in words:
          if frequencies.get(i) is None:
               frequencies[i] = 1
          else:
               frequencies[i] += 1
     
     x = sorted(frequencies.items(), key=lambda x : (-x[1], x[0]))[:k]
     return list(dict(x).keys())

x = function(["the","day","is","sunny","the","the","the","sunny","is","is", "sunny"], 4)
print(x)
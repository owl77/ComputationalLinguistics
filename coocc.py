
grammar = ["the","of", "in", "for", "you", "they", "from","to", "by", "but", "i", "between", "with", "he","she","them", "we", "it", "this","that","those","these","not","is","are","were","was", "be","have","had", "has", "his","her", "their", "if", "then","and","or", "a", "neither", "whether", "since", "because", "else", "so", "do", "did", "didn't", "each", "will", "shall", "would", "which", "should", "could","can","must", "might", "may","ought",
"itself", "socrates" ,"its","didnt", "our", "as","on","no", "at","up","down","over","under", "out","how","can","him",
"an","your","another","than","any","also","there","some","very","been","us", "my","mine","dont","still","rather","after", "more","much", "why", "too", "yet","yes","yours", "what","when","who",
"nor","does", "having", "again", "further", "through", "every", "own","into","only", "himself","herself","itself","get","go","me","im","isnt","indeed", "about", "both","either","neither","however","whom"
"most"
]

punctuation = [":",",",";","?","!",".","'s","(",")","'","-", '"']

text = []
lex = input("Enter term : ")

with open("plato.txt", 'r',  encoding='utf8' ) as f:
 for line in f:
    words = line.split()
    
    newwords= []
    for w in words:
       for p in punctuation:
        w = w.replace(p,"")
       w = w.lower()
       newwords.append(w)
    if lex in newwords:
      text = text + newwords
f.close()

text = [w for w in text if not w in grammar and len(w) > 1 and not '¯' in w]


voc = sorted(list(set(text)))
print ("Vocabulary size: ")
print(len(voc))
freq = {}
for v in voc:
  print (v)
  freq[v] = 0
  for w in text:
   if w == v:
     freq[v] = freq[v] +1

def get_max(dic):
 max = 0
 key = ""
 for k in dic.keys():
   if dic[k] > max:
    key = k
    max = dic[k]
 return key

import copy

def dic_order(dic):
 dic2 = copy.deepcopy(dic)
 ord = []
 while len(dic2.keys()) > 0:
  aux = get_max(dic2)
  ord.append(aux)
  dic2.pop(aux)

 return ord

  
name = lex +"freq.txt"

f = open(name, "a",  encoding='utf8')

for k in dic_order(freq):
 f.write(k + " : " + str(freq[k]) + "\n" )
   
f.close()

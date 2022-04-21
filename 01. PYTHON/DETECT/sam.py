# from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance

def read_file(file_name):
  file = open(file_name,"r")
  file_data = file.readlines()
  dict_file = file_data[0].split(",")
  sentences = []
  for sentence in dict_file:
    sentences.append(sentence)
  sentences.pop()
  return sentences

def sentence_similarity (ui_input,data_set_sent,stopwords = None):
  if stopwords is None:
    stopwords = []
  ui_input = [w.lower() for w in ui_input]
  data_set_sent = [w.lower() for w in data_set_sent]
  all_words = list(set(ui_input+data_set_sent))

  vector1 = [0]* len(all_words)
  vector2 = [0]* len(all_words)
  for w in ui_input:
    if w in stopwords:
      continue
    vector1[all_words.index(w)] += 1
  for w in data_set_sent:
    if w in stopwords:
      continue
    vector2[all_words.index(w)] += 1
  return 1-cosine_distance(vector1,vector2)

gui_ip = "HC:Unsafe condition: Access not provided in the excavation for ingress/egress"

data_set = read_file("F:\DETECT\data_set.txt")
sw = ["is","the"]
temp=0
for i in range (len(data_set)):
  cos_value=sentence_similarity(gui_ip,data_set[i],sw)
  print(cos_value)
  if cos_value>temp:
    temp = cos_value
    sent_index = i
print (data_set[sent_index])
  
  






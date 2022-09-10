from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance

def read_file(file_name):
  file = open(file_name,"r")
  file_data = file.readlines()
  dict_file = file_data[0].split(",")
  print(dict_file)
  sentences = []
  for sentence in dict_file:
    sentences.append(sentence.split(" "))
  print (sentences)
  sentences.pop()
  return sentences

a=read_file("F:\DETECT\ABC.txt")



def sentence_similarity (ui_input,data_set_sent,stopwords = None):
  if stopwords is None:
    stopwords = []
  ip1=[]
  ui_input=list(ui_input)
  for words in ui_input:
    ip1.append(words.split(" "))
  # print(ip1)


  ui_input = [ip1.append(words.split(" ")) for words in list(ui_input)]
  data_set_sent = [w.lower() for w in data_set_sent]
  all_words = list(set(ui_input+data_set_sent))




  vector1 = [0]* len(all_words)
  vector2 = [0]* len(all_words)

  for w in ui_input:
    if w in stopwords:
      print (w)
      continue
    vector1[all_words.index(w)] += 1
  for w in data_set_sent:
    if w in stopwords:
      continue
    vector2[all_words.index(w)] += 1
  return 1-cosine_distance(vector1,vector2)

gui_ip = "my name is Abishek, the programmer"
ip2 = "My name is abishek gurumurthy"
stopwords = stopwords.words('english')
cos_value=sentence_similarity(gui_ip,ip2)
print(cos_value)

# gui_ip = "HC:Unsafe condition: Access not provided in the excavation for ingress/egress"

# data_set = read_file("F:\DETECT\data_set.txt")
# data_set = read_file("F:\DETECT\ABC.txt")
# temp=0
# for i in range (len(data_set)):
#   cos_value=sentence_similarity(gui_ip,data_set[i])
#   print(cos_value)
#   if cos_value>temp:
#     temp = cos_value
#     sent_index = i
# print (data_set[sent_index])

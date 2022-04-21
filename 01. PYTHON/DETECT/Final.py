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

def sentence_similarity (ui_input,data_set_sent):
  ui_input = [w.lower() for w in ui_input]
  data_set_sent = [w.lower() for w in data_set_sent]
  all_words = list(set(ui_input+data_set_sent))

  vector1 = [0]* len(all_words)
  vector2 = [0]* len(all_words)
  for w in ui_input:
    vector1[all_words.index(w)] += 1
  for w in data_set_sent:
    vector2[all_words.index(w)] += 1
  return 1-cosine_distance(vector1,vector2)


def validate (ip1,ip2):
    gui_ip = ip1
    data_set = read_file(ip2)
    temp=0
    for i in range (len(data_set)):
      cos_value=sentence_similarity(gui_ip,data_set[i])
      if cos_value>temp:
        temp = cos_value
        sent_index = i
    return (data_set[sent_index])

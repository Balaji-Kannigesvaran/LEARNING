from os import read
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

# def read_file(file_name):
#   file = open(file_name,"r")
#   file_data = file.readlines()
#   dict_file = file_data[0].split(",")
#   sentences = []
#   for sentence in dict_file:
#     sentences.append(sentence)
#   sentences.pop()
#   # for sentence in dict_file:
#   #   sentences.append(sentence.replace("[^a-zA-Z]"," ").split(" "))
#   # sentences.pop()
#   # return sentences
#   print (sentences)

# emplist = read_file("F:\DETECT\data_set.txt")

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

s0 = "HC:Unsafe condition: Access not provided in the excavation for ingress/egress"
s1 = "HC:Unsafe condition: Excavation access not provided"
s2 = "HC:Unsafe environment: No access for is provided in the excavation"
s3 = "HC:Unsafe condition: Entry and exit is not provided"
s4 = "HC:Unsafe condition: No access for ingress/egress is provided in the excavation"

a1 = sentence_similarity(s0,s1) 
print (a1)
a2 = sentence_similarity(s0,s2) 
print (a2)
a3 = sentence_similarity(s0,s3) 
print (a3)
a4 = sentence_similarity(s0,s4) 
print (a4)


# def generate_similarity_matrix (sentences,stop_words):
#   sim_mat=np.zeros((len(sentences), len(sentences)))
#   for idx1 in range (len(sentences)):
#     for idx2 in range (len(sentences)):
#       if idx1 == idx2:
#         continue
#       sim_mat[idx1][idx2]=sentence_similarity(sentences[idx1],sentences[idx2],stop_words)
#   return sim_mat

# def gen_sum (file_name,top_n=5):
#   stop_words = stopwords.words('english')
#   output = []
#   sentences = read_file(file_name)
#   sentence_similarity_matrix = generate_similarity_matrix(sentences,stop_words)
#   sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
#   scores = nx.pagerank(sentence_similarity_graph)
#   ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)),reverse = True)
#   print (ranked_sentence[0][1])

# # gen_sum("F:\DETECT\data_set.txt",1)



from nltk.cluster.util import cosine_distance


class synonym_sentence_generator:
  """
  This class is the where the synonym sentence validation happens.
  The class is called in the GUI and the respective inputs are being sent back post execution.   
  """
  
  # The inputs are received from GUI and is assigned to the object variables
  def __init__(self, ip1, ip2):
    self.ip1=ip1
    self.ip2=ip2

  #This is the method to perform the sentence comparison and return the synonymous sentence
  def validate (self):
      gui_ip = self.ip1
      data_set = self.read_file(self.ip2)
      temp=0
      for i in range (len(data_set)):
        cos_value=self.sentence_similarity(gui_ip,data_set[i])
        if cos_value>temp:
          temp = cos_value
          sent_index = i
      return (data_set[sent_index])

  #This method read the sentences in the file and a list of the sentences in the file is generated
  def read_file(self,file_name):
    file = open(file_name,"r")
    file_data = file.readlines()
    txt_file = file_data[0].split(",")
    sentences = []
    for sentence in txt_file:
      sentences.append(sentence)
    sentences.pop()
    return sentences


  # This method is used to find the similarity of the sentences using cosine_distance from nltk library
  def sentence_similarity (self,ui_input,data_set_sent):
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








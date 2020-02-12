import string;
class WordPredictor:
    def __init__(self):
        self.s = "";

    def get_most_likely_successor(self,word):
       filename=r'C:\Users\shwet\Desktop\NZ\11-0.txt';
       ind=[];
       succedor=[];
       origin=[];
       with open(filename, 'rb') as f:
                content = f.read();
                content = content.translate(None, string.punctuation).lower();
                mylist = content.split(); #Get all the strings in the txt file in a list separated by space
                ind=[i for i, x in enumerate(mylist) if x == word];  #take indeces of that word from list
       m=0;
       for i in ind:
           m=i+1;
           if m < len(mylist):
               succedor.append(mylist[m]); #take all its succussor words in another list
           else:
               print "this is last element";
       count1=0;
       dict1={};
       origin=set(succedor); #all unique succeding elements in a lis
       for i in origin:
           freq=succedor.count(i);
           dict1[i]=freq;  #form key value pair of word and its frequency
       max_value = max(dict1.values());
       l3=[];
       for key in dict1:
           if dict1.get(key)==max_value:   #get words having max frequency
               l3.append(key);
       return l3;
       f.close();
                           
strObj = WordPredictor();  #create object of class
strObj.get_most_likely_successor("rabbit"); #call the method

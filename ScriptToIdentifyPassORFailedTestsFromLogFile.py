#This File is checking test case logs for passed test cases and copying logs of passed tests to a different folder
import csv
import os
import shutil
counter=0
base_dir = r'c\abc.txt'



with open('C:\csv\Regression.csv', 'rb') as csvfile:
   spamreader = csv.reader(csvfile)
   for row in spamreader:

         filename = row[2]
         
         path=os.path.join(base_dir, filename)
         
         dst=r'C:\csv\logs'
         
         for root, dirs, files in os.walk(path):
             
             for m in files:
                 
                 if m.startswith ('Test') and m.endswith ('.log'):
                   path1=os.path.join(root, m)

                   with open(path1, 'r') as inF:
                      for line in inF:
                            
                          if ('TEST Test' in line) and ('PASSED' in line):
                               

                               src=os.path.join(path, m)
                               
                               
                               shutil.copy2(src, dst)
 
   

   
   



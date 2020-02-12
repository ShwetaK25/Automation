#This File is checking test case logs for passed test cases and copying logs of passed tests to a different folder
import csv
import os
import shutil
counter=0
base_dir = r'S:\NGP\Accurev_STP_4MAR\PRMSV\PRMSV_Build\logs'


###OR
##try:
##       base_dir = int(raw_input("Please enter the path of log files: "))
##except :
##       print "Oops!  That was no valid path.  Please enter valid path."

with open('S:\NGP\sonkarv\csv\MAU_AUTO_Regression.csv', 'rb') as csvfile:
   spamreader = csv.reader(csvfile)
   for row in spamreader:
##       if row[0]=='ING2' and row[9]=='Passed':
##           print (row)
##           counter=counter+1
##           print row
##   print 'counter'+str(counter)
         filename = row[2]
         
         path=os.path.join(base_dir, filename)
         
         dst=r'S:\NGP\sonkarv\csv\logs'
         
         for root, dirs, files in os.walk(path):
             
             for m in files:
                 
                 if m.startswith ('Test') and m.endswith ('.log'):
                   path1=os.path.join(root, m)

                   with open(path1, 'r') as inF:
                      for line in inF:
                            
                          if ('TEST Test' in line) and ('PASSED' in line):
                               

                               src=os.path.join(path, m)
                               
                               
                               shutil.copy2(src, dst)
 
   

   
   



import os
import sys
import re
import json
import csv
import pandas as pd

input_filename = sys.argv[1];

choice = sys.argv[2][1];
def tsv2Csv(input_file,output_file):
    with open(input_file, 'r') as myfile:  
        with open(output_file, 'w') as csv_file:
            for line in myfile:
            
        # Replace every tab with comma
                fileContent = re.sub("\t", ",", line)
            
        # Writing into csv file
                csv_file.write(fileContent)


def tsv2json(input_file,output_file):
    arr = []
    file = open(input_file, 'r')
    a = file.readline()
    
    titles = [t.strip() for t in a.split('\t')]
    for line in file:
        d = {}
        for t, f in zip(titles, line.split('\t')):
            
            # Convert each row into dictionary with keys as titles
            d[t] = f.strip()
            
        # we will use strip to remove '\n'.
        arr.append(d)
        
        # we will append all the individual dictionaires into list 
        # and dump into file.
    with open(output_file, 'w', encoding='utf-8') as output_file:
        output_file.write(json.dumps(arr, indent=4))


def tsv2xml(input_file,output_file):
    df= pd.read_csv(input_file)
    with open(output_file, 'w') as myfile: 
        myfile.write(df.to_xml())

# reading given tsv file
if(choice == 'c'):
    # input_filename = 'sample1.txt'
    output_filename = 'sample1.csv'
    tsv2Csv(input_filename,output_filename)
    
#-------------------------------------------
if(choice == 'j'):
    # input_filename = 'sample1.txt'
    output_filename = 'sample1.json'
    tsv2json(input_filename,output_filename)

#=-------\

if(choice == 'x'):
    tsv2Csv("sample1.txt","sample1forxml.csv")
    input_filename = 'sample1forxml.csv'
    output_filename = 'sample1.xml'
    tsv2xml(input_filename,output_filename)
    os.remove("sample1forxml.csv")
   

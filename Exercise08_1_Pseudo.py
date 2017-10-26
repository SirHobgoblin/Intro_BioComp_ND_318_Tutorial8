#Exercise 8, Python question 1
#10/13/17, MMD
#import os and packages
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
#set working directory
os.chdir('C:\\Users\\jsh\\OneDrive\\github\\BioComp\\Intro_Biocomp_ND_318_Tutorial8\\')

#Open files to read and write
vcffile = open("Cflorida.vcf","r")
outfile = open("CfloridaCounts.txt","w")

#assign regex to variable name, or compile to variable name

#loop over file
for :#look at old code to see how you looped over a file
    #strip end of line
    if : #how can you tell if this is the header line?
        #write unchanged header line to file
    elif : #how can you tell if this is the line with the column headings?
        #standardize (replace) sample names with TX and FL regexes
        #write new version of line to file
    else: #now you're in the data
        #replace full SNP info with allele counts only
        #replace missing data with NA
        #write new version of line to new file
        
#Close files


#for loop over each column
    #if first row contains ".A" or ".a"
    #then replace with "Cf.Sfa." followed by the 3 digit sample ID
    #for every other row in a column, only include info between the first and second ":"
        #if the info between the two colons is "." replace with "NA"
    
    #if first row contains ".G" or ".g"
    #then replace with "Cf.Gai." followed by the 3 digit sample ID
    #for every other row in a column, only include info between the first and second ":"
        #if the info between the two colons is "." replace with "NA"

#write this all to "CfloridaCounts.txt"

#Exercise 8, Python question 1
#10/13/17, MMD
#What do we want to do? 
#standardize all TX samples to CF.SFA.XXX 
#standardize all FL samples to CF.GAI.XXX
#Then
#Extract the allel count for each SNP/individual (., replace with NA)
#Create a new file CfloridaCounts.txt that will be the corrected version of Cflorida.vcf


#import os and packages
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import re
#set working directory
os.chdir('C:\\Users\\jsh\\OneDrive\\github\\BioComp\\Intro_Biocomp_ND_318_Tutorial8\\')



#Open files to read and write
vcffile = open("Cflorida.vcf","r")
#line = line.strip() #stips \n
#line = vcffile.readline().strip() #advances to the next line and strips
#vcffile.close() #closes file, do we want this, yet?


outfile = open("CfloridaCounts.txt","w")
#outfile.write(string + "\n") #appends line to file, but need to define string?
#outfile.close() #closes file

#create empty dictionary
dictionary = []
for line in vcffile:
    line = line.strip()
    cols = line.strip()
    if cols[0] in dictionary:
        print("Duplicate: " + cols[1])
        break
    else:
        dictionary[cols[0]] = cols[1]


#re.sub(regexString,replacement,searchString)
#The regex string we should search for the TX samples is:
"[Cc][Ff](07)?\.[Aa]2?" and replace with "Cf.Sfa"

#The regex string we should search for the FL samples is:
"[Cc][Ff](07)\.[Gg][2Aa]([Ii])?" and replace with "Cf.Gai"
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
        
#Going to try and make the above for loop
        
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

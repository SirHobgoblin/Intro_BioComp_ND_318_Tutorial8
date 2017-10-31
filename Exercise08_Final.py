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
import fileinput
import string
import sys
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy

#set working directory
os.chdir('C:\\Users\\jsh\\OneDrive\\github\\BioComp\\Intro_Biocomp_ND_318_Tutorial8\\')
#os.chdir('/Users/omneelay/Desktop/Exercise8stuff/Intro_Biocomp_ND_318_Tutorial8/')

#read file and open new file
vcffile = open("Cflorida.vcf","r")
outfile = open('CfloridaCounts.txt','w')

#Loop
for Line in vcffile:
    Line=Line.strip()
    if '#' in Line: #finds the heading lines that contain the sample names
        fl=re.sub("([Cc][Ff]\.[Gg](2|AI|ai))", "Cf.Gai",Line) #florida regex
        tx=re.sub("([Cc][Ff](07)?\.[Aa]2?)","Cf.Sfa", fl) #texas regex
        outfile.write(tx + "\n") #write names to file
    else: #all other lines
        alleledata = re.sub(r"\d/\d:(\d,\d):\d:\d+:\d+,\d+,\d+" , r"\1" , Line) #regular alleles regex select allele count from data
        missingdata = re.sub("\./\.:\.:\.:\.:\." , "NA" , alleledata) #missing alleles regex, replace with NA
        outfile.write(missingdata + "\n") #write data to file

#close files        
outfile.close()
vcffile.close()

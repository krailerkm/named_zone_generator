#!/usr/bin/python
# -*- coding: utf-8 -*-
# 9 September 2020 Codeing by Krailerk M.
# This script for convert txt list of url to named new zone for block in pdns
#                                           
#  _____         _ _         _      _____   
# |  |  |___ ___|_| |___ ___| |_   |     |  
# |    -|  _| .'| | | -_|  _| '_|  | | | |_ 
# |__|__|_| |__,|_|_|___|_| |_,_|  |_|_|_|_|
#                                           
#
import datetime
import re

def main():
    ## Run date time
    today = datetime.date.today()
    #print(today.strftime("%d %b %Y"))
    ## Open file for read all url from text
    fileOP = open("./input/urllist.txt", "r")
    ## Readline from file to parameter
    beforeCUT = fileOP.readlines()
    #print(beforeCUT)
    ## Close file for read all url from text
    fileOP.close()
    ## Parameter for store string
    outCUT = str()
    ## Loop for split only url cut off part and record
    for n in beforeCUT:
        name = re.sub(r"\s+", "", n)
        #print("@"+name)
        ## Cut off http://
        if name[:7] == "http://":
            ## CUT http://
            tmp = name[7:]
            print(tmp)
            ## Store to string
            outCUT += tmp + " "
        ## Cut off https://
        elif name[:8] == "https://":
            ## CUT https://
            tmp = name[8:]
            print(tmp)
            ## Store to string
            outCUT += tmp + " "
        ## Cut off not domain and part
        elif n[:2] == "\n":
            ## Pass any things
            pass
        ## Any domain and part
        else:
            ## Any word sotore
            tmp = name
            #print(tmp)
            ## Store to string
            outCUT += tmp + " "
    #print(outCUT)
    ## Find unique url from many url list
    unique_words = set(outCUT.split())
    #print(unique_words)
    ## Name of blocker
    nameBlock = "Krailerk M."
    ## Name of requester
    nameRequest = "Sopis J."
    ## Number of case from Court's order
    noCase = "Case No. 327-2563"
    ## Generate comment of line
    tmpstr1 = "//// " + nameBlock + " //// Request by " + nameRequest + " //// According to the Court's order, " + noCase + " //// " + str(today.strftime("%d %b %Y")) + "\n"
    ## Str parameter for store data record zone
    tmpstr = str()
    ## Test and script
    tmptest = str()
    ## Test run and reload script
    tmptest1 = "named-checkconf\nrndc reload\n"
    ## Start init tmptest
    tmptest += tmptest1
    ## Loop for generate zone file
    for tmpUniqueURL in unique_words:
        ## Create zone record and link to zone file
        tmpstr2 = "zone \"" + tmpUniqueURL + "\" IN {\n        type master;\n        file \"data/db.block.mdes.go.th\";\n        allow-update { none; };\n};\n\n"
        ## Put all data to tmp string
        tmpstr += tmpstr1 + tmpstr2
        ## Test all domain
        tmptest += "nslookup " + tmpUniqueURL + "\n"
    ## Show output
    #print(tmpstr)
    ## Open output file output
    fileOut = open("./output/outzone.txt", "w")
    ## Write Export output to file
    fileOut.write(tmpstr)
    ## Close file output
    fileOut.close
    ## Show test
    #print(tmptest)
    ## Open test file test
    fileOut = open("./output/outtest.txt", "w")
    ## Write Export test to file
    fileOut.write(tmptest)
    ## Close file test
    fileOut.close

## Run main function
if __name__ == "__main__":
    ## Call main
    main()
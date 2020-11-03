#!/usr/bin/python
# -*- coding: utf-8 -*-
# 9 September 2020 Codeing by Krailerk M.
# This script for convert txt list of url to named new zone for block in pdns
# NCG v1.0a - (Named configuration generator version 1.0a) 
#  _____         _ _         _      _____   
# |  |  |___ ___|_| |___ ___| |_   |     |  
# |    -|  _| .'| | | -_|  _| '_|  | | | |_ 
# |__|__|_| |__,|_|_|___|_| |_,_|  |_|_|_|_|
#                                           
#
#Used to make requests
import urllib.request
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()
x = urllib.request.urlopen("https://pornhub.com", context=context)

print(x.read())
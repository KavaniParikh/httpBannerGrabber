#__author__ = Kavani
import requests
import os
print("-------------------------------------")
print("------------BANNER GRABBER-----------")
print("-------------------------------------")
print("                           Author: Kavani Parikh                      ")
print('Enter URL in "http://www.abc.com"')
source = input()
print("-------------------------------------")
print ("you entered " + source)
req_g = requests.get(source)
req_o = requests.options(source)
print("-------------------------------------")
print("---------Printing Banner-------------")
print("-------------------------------------")
print("\n")
print(req_g.headers)
print("\n")
file_obj = open('banner.txt','w')
file_obj.write("\n---------------------GET Method Result---------------------\n")
print("\n")
file_obj.write(str(req_g.headers))
file_obj.write("\n")
file_obj.write("\n---------------------OPTIONS Method Result-----------------\n")
file_obj.write("\n 'Allow:' parameter shows allowed HTTP Methods \n")
file_obj.write("\n")
file_obj.write(str(req_o.headers))
file_obj.write("\n-----------------------------------------------------------\n")
file_obj.close()
print("-------------------------------------")
print("--------Saving Results---------------")
print("\n")
print("Path : " + os.getcwd() + "\\banner.txt")
print("\n")
print("-------------------------------------")

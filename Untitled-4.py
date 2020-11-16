#!/oci/bin/python
import configparser
import os
import sys
import oci

n = len(sys.argv)
if n==2:
   student=sys.argv[1]
   print(student)
else :
   print("Please enter tenancy name as argument")
   exit(200)
def tenancy_connect(student):
    tenancy_name=configparser.ConfigParser()
    tenancy_name.read('/root/.oci/config')
    name1=tenancy_name[student]['user']
    print(name1)
tenancy_connect(student)

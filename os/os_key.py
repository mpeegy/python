#!/usr/bin/env python
from fingerprint import fingerprint
from subprocess import call
os = fingerprint()
#Получить корректный ключ для EPM
epm_keyword = {"ubuntu":"dpkg", "redhat":"rpm", "SunOS":"pkg", "osx":"osx"}
try:
    epm_keyword[os]
except (Exception, err):
    print (err)
subprocess.call("epm if %s helloEPM hello_epm.list" % 
platform_cmd,shell=True)

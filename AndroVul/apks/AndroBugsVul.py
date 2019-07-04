# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 13:43:13 2018

@author: AN68090
"""

# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join
import subprocess
import os
import re

httoUrlCountera = 0
path1 ='C:\\AndroVul\\apks\\Reports'
#path2 = 'C:\\Users\\an68090\\Desktop\\result2\\Reports'
csvReport = 'AndroBugsVul.csv'
"""regex = re.compile(b'(\Critical])(.*?)\w*(Checking:)')"""
regex = re.compile(b'(Critical]|Warning])(.*?)(Checking:)')

def getAllFilesInAFolder(_path):
    result = []
    try:
        for f in listdir(_path):
            if(isfile(join(_path, f))):
                result.append(join(_path,f))
            else:
                result.extend(getAllFilesInAFolder(join(_path, f)))
    except Exception:
            result.append('Error searching file')
    
    return result


def getHttpGet(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        b = re.findall(b'(Critical]|Warning])(.*?)(Checking:)', s)
        #print(b)
        return b
    
def containsVulnerability(result, name):
    for sentence in result:
        if 'Critical' in str(sentence[0]):
            if name in str(sentence[1]):
                return '1'
        else:
            if name in str(sentence[1]):
                return '0.5'
    return '0'
    
reportCsvFile = open(csvReport, 'w')
reportCsvFile.write('App Package;SSL Connection;Vulnerability in Storage Access;Android SQLite Databases Encryption;Attack in Android Debug Mode ;AndroidManifest "intent-filter"  ;Using critical function  ;AndroidManifest System Use Permission  ;Dynamic Code Loading  ;Sandbox Permission  ;AndroidManifest Normal ProtectionLevel of Permission ;Getting system permission  ;File Unsafe Delete ;Fragment Vulnerability ;Using MonoDroid Framework ;String Encryption ; APK Installer Sources ; KeyStore File Location ; KeyStore Protection ; Code Setting Preventing Screenshot Capturing ; Getting Signature Code ; KeyStore Type Checking ; Master Key Type I Vulnerability  ; Native Library Loading ; AndroidManifest Dangerous ProtectionLevel of Permission  ; AndroidManifest Exported Components   ; AndroidManifest PermissionGroup ; Implicit Service Checking  ; AndroidManifest Exported Lost Prefix  ; AndroidManifest ContentProvider Exported ; Getting IMEI and Device ID  ; Getting ANDROID_ID ; Sending SMS ; AndroidManifest sharedUserId ; SSL Implementation ; SSL Certificate Verification ; Unnecessary Permission ;Accessing the Internet ;WebView Local File Access Attacks ;WebView Potential XSS Attacks ;WebView RCE Vulnerability ;Google Cloud Messaging Suggestion')
reportCsvFile.write('\n')
for f in listdir(path1):
    if (isfile(join(path1, f))and f.endswith(".txt")):
        
        dirOfFile = f[:-4]
        listOfFilesInFolder = getAllFilesInAFolder(join(path1, dirOfFile))
        """fileReport = open('Report-' + f +'.html', 'w')
        fileReport.write('<head>\n')
        fileReport.write('<body>\n')
        fileReport.write('<h1>Report for '+ join(path2,f)+ '</h1>\n')"""
        r = getHttpGet(join(path1,f))
        reportCsvFile.write(f + ';' + containsVulnerability(r, 'SSL Connection')  + ';' + containsVulnerability(r, 'External Storage Accessing' ) + ';' + containsVulnerability(r, 'SQLite Databases') + ';' + containsVulnerability(r, 'Android Debug Mode') + ';' +  containsVulnerability(r, 'intent-filter') + ';' + containsVulnerability(r, 'Runtime Command') + ';' + containsVulnerability(r, 'AndroidManifest System Use Permission ') + ';'  + containsVulnerability(r, 'Dynamic Code Loading') + ';' + containsVulnerability(r, 'Sandbox Permission ') + ';' + containsVulnerability(r, 'AndroidManifest Normal ProtectionLevel of Permission') + ';' + containsVulnerability(r, 'getting system permission') + ';' + containsVulnerability(r, 'File Unsafe Delete') + ';' + containsVulnerability(r, 'Fragment Vulnerability' ) + ';' + containsVulnerability(r, 'MonoDroid') + ';' + containsVulnerability(r, 'Base64 String Encryption' ) + ';' + containsVulnerability(r, 'APK Installing Source' ) + ';' + containsVulnerability(r, 'KeyStore File Location' ) + ';' + containsVulnerability(r, 'KeyStore Protection' ) + ';' + containsVulnerability(r, 'Code Setting Preventing Screenshot Capturing' ) + ';' + containsVulnerability(r, 'Getting Signature Code' ) + ';' + containsVulnerability(r, 'KeyStore Type Checking' ) + ';' + containsVulnerability(r, 'Master Key Type I Vulnerability' ) + ';' + containsVulnerability(r, 'Native Library Loading' ) + ';' + containsVulnerability(r, 'AndroidManifest Dangerous ProtectionLevel of Permission ' ) + ';' + containsVulnerability(r, 'AndroidManifest Exported Components ') + ';' + containsVulnerability(r, 'AndroidManifest PermissionGroup  ') + ';' + containsVulnerability(r, 'Implicit Service Checking ') + ';' + containsVulnerability(r, 'AndroidManifest Exported Lost Prefix ') + ';' + containsVulnerability(r, 'AndroidManifest ContentProvider Exported ') + ';' + containsVulnerability(r, 'Getting IMEI and Device ID ') + ';' + containsVulnerability(r, 'Getting ANDROID_ID ') + ';' + containsVulnerability(r, 'Sending SMS') + ';' + containsVulnerability(r, 'AndroidManifest sharedUserId') + ';' + containsVulnerability(r, 'SSL Implementation') + ';' + containsVulnerability(r, 'SSL Certificate Verification') + ';' + containsVulnerability(r, 'Unnecessary Permission') + ';' + containsVulnerability(r, 'Accessing the Internet') + ';' + containsVulnerability(r, 'WebView Local File Access Attacks') + ';' + containsVulnerability(r, 'WebView Potential XSS Attacks') + ';' + containsVulnerability(r, 'Remote Code Execution') + ';' + containsVulnerability(r, 'Google Cloud Messaging Suggestion')) 
        reportCsvFile.write('\n')
reportCsvFile.close()        
"""fileReport.close()"""                 
                        
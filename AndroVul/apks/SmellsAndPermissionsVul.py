
"""
Created on Fri Feb  9 14:47:22 2018

@author: AN68090
"""
from os import listdir
from os.path import isfile, join
import subprocess
import os
import re
import shutil

apktool_path = 'C:\\AndroVul\\apktool\\aapt.exe'
androbugs_path = 'C:\\AndroVul\\AndroBugs_Framework\\androbugs.exe'

path1 = 'C:\\AndroVul\\apks' 




commanBaseLine = 'java -jar C:\\AndroVul\\apktool\\apktool.jar d '
csvReport = 'SmellsAndPermissionsVul.csv'
httoUrlCountera = 0
httoUrlCounterb = 0
httoUrlCounter1a = 0
httoUrlCounter1b = 0
httoUrlCounter2a = 0
httoUrlCounter2b = 0
httoUrlCounter3a = 0
httoUrlCounter3b = 0
httoUrlCounter4a = 0
httoUrlCounter4b = 0
httoUrlCounter5a = 0
httoUrlCounter5b = 0
httoUrlCounter6a = 0
httoUrlCounter6b = 0
httoUrlCounter7a = 0
httoUrlCounter7b = 0
httoUrlCounter8a = 0
httoUrlCounter8b = 0
r10 = ''
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
            
    
def getHttpURLConnection(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        m = re.findall(b'HttpURLConnection', s)
        f.close()
        return len(m) > 0 

def getHttpURLConnectionCount(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        m1 = re.findall(b'HttpURLConnection', s)
        f.close()
        return len(m1) 

def getString(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        d1 = re.findall(b'Ljava/lang/String', s)
        f.close()
        return len(d1) > 0
    
def getStringCount(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        d = re.findall(b'Ljava/lang/String', s)
        f.close()
        return len(d) 

def getClipData(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        y = re.findall(b'Landroid/content/ClipData', s)
        f.close()
        return len(y) > 0
    
def getClipDataCount(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        y1 = re.findall(b'Landroid/content/ClipData', s)
        f.close()
        return len(y1)  
    
def getTrustManager(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        k = re.findall(b'Ljavax/net/ssl/X509TrustManager', s)
        f.close()
        return len(k) > 0  

def getTrustManagerCount(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        k1 = re.findall(b'Ljavax/net/ssl/X509TrustManager', s)
        f.close()
        return len(k1)

 
def getContext(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        p = re.findall(b'Landroid/content/Context', s)
        f.close()
        return len(p) > 0 

def getContextCount(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        p1 = re.findall(b'Landroid/content/Context', s)
        f.close()
        return len(p1)   

def getWebSettings(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        h = re.findall(b'Landroid/webkit/WebSettings', s)
        f.close()
        return len(h) > 0
    
def getWebSettingsCount(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        h1 = re.findall(b'Landroid/webkit/WebSettings', s)
        f.close()
        return len(h1)     

def getWebWebView(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        x = re.findall(b'Landroid/webkit/WebView', s)
        f.close()
        return len(x) > 0 
    
def getWebWebViewCount(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        x1 = re.findall(b'Landroid/webkit/WebView', s)
        f.close()
        return len(x1) 
    
    
def getHttpGet(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        b = re.findall(b'Lorg/apache/http/client/methods/HttpGet', s)
        f.close()
        return len(b) > 0 
    
def getHttpGetCount(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        b1 = re.findall(b'Lorg/apache/http/client/methods/HttpGet', s)
        f.close()
        return len(b1) 
    

def getSchemeRegistry(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        q = re.findall(b'Lorg/apache/http/conn/scheme/SchemeRegistry', s)
        f.close()
        return len(q) > 0 
    
def getSchemeRegistryCount(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        q1 = re.findall(b'Lorg/apache/http/conn/scheme/SchemeRegistry', s)
        f.close()
        return len(q1)  




def getHttpGetPerm(filePath):
    with open(filePath,"rb") as f:
        s = f.read()
        b = re.findall(b'READ_CALENDAR', s)
        b += re.findall(b'WRITE_CALENDAR' , s)
        b += re.findall(b'CAMERA' , s)
        b += re.findall(b'READ_CONTACTS' , s)
        b += re.findall(b'WRITE_CONTACTS' , s)
        b += re.findall(b'GET_ACCOUNTS' , s)
        b += re.findall(b'ACCESS_FINE_LOCATION' , s)
        
        b += re.findall(b'ACCESS_COARSE_LOCATION' , s)
        b += re.findall(b'RECORD_AUDIO' , s)
        b += re.findall(b'READ_PHONE_STATE' , s)
        b += re.findall(b'CALL_PHONE' , s)
        b += re.findall(b'READ_CALL_LOG' , s)
        b += re.findall(b'WRITE_CALL_LOG' , s)
        b += re.findall(b'ADD_VOICEMAIL' , s)
        b += re.findall(b'USE_SIP' , s)
        b += re.findall(b'PROCESS_OUTGOING_CALLS' , s)
        b += re.findall(b'BODY_SENSORS' , s)
        b += re.findall(b'SEND_SMS' , s)
        b += re.findall(b'RECEIVE_SMS' , s)
        b += re.findall(b'READ_SMS' , s)
        b += re.findall(b'RECEIVE_WAP_PUSH' , s)
        b += re.findall(b'RECEIVE_MMS' , s)
        b += re.findall(b'READ_EXTERNAL_STORAGE' , s)
        b += re.findall(b'WRITE_EXTERNAL_STORAGE' , s)
       
        
        return b

def containsVulnerability(result, name):
    for sentence in result:
        
        if str(name) in str(sentence):
            return '1'
    return '0'

    

reportCsvFile = open(csvReport, 'w')
reportCsvFile.write('App Package;Insecure Network Protocol True %;Unique Hardware Identifier True %;Exposed Clipboard True %;Improper Certificate Validation True % ;Dynamic Code Loading True %;XSS-like Code Injection True;Broken Web Views Sandbox True  %;Header Attacment True % ;Custom Scheme Channel True % ;READ_CALENDAR;WRITE_CALENDAR;CAMERA;READ_CONTACTS;WRITE_CONTACTS  ;GET_ACCOUNTS  ;ACCESS_FINE_LOCATION ;ACCESS_COARSE_LOCATION  ;RECORD_AUDIO  ;READ_PHONE_STATE ;CALL_PHONE  ;READ_CALL_LOG ;WRITE_CALL_LOG ;ADD_VOICEMAIL ;USE_SIP ; PROCESS_OUTGOING_CALLS; BODY_SENSORS ; SEND_SMS ; RECEIVE_SMS ; READ_SMS ; RECEIVE_WAP_PUSH ; RECEIVE_MMS  ; READ_EXTERNAL_STORAGE ; WRITE_EXTERNAL_STORAGE  ')

for f in listdir(path1):
    if (isfile(join(path1, f)) and f.endswith(".apk")):
            s = commanBaseLine  + join(path1,f)
            #print (s) 
            os.system(s)
            s = androbugs_path + ' -f ' + join(path1,f)
            os.system(s) 
            dirOfFile = f[:-4]
            listOfFilesInFolder = getAllFilesInAFolder(join(path1, dirOfFile))

            auxCountVul = 0
            httoUrlCountera = 0
            httoUrlCounterb = 0
            httoUrlCounter1a = 0
            httoUrlCounter1b = 0
            httoUrlCounter2a = 0
            httoUrlCounter2b = 0
            httoUrlCounter3a = 0
            httoUrlCounter3b = 0
            httoUrlCounter4a = 0
            httoUrlCounter4b = 0
            httoUrlCounter5a = 0
            httoUrlCounter5b = 0
            httoUrlCounter6a = 0
            httoUrlCounter6b = 0
            httoUrlCounter7a = 0
            httoUrlCounter7b = 0
            httoUrlCounter8a = 0
            httoUrlCounter8b = 0
            r10 = ''
            for fileName in listOfFilesInFolder:
                if(fileName.endswith('.smali')):
                    r = getHttpURLConnectionCount(join(path1,fileName))
                    if(r > 0):
                        httoUrlCountera += 1
                    else :
                        httoUrlCounterb += 1
                    r1 = getStringCount(join(path1,fileName))
                    if(r1 > 0):
                        httoUrlCounter1a += 1 
                    else:
                        httoUrlCounter1b += 1
                        
                    r2 = getClipDataCount(join(path1,fileName))
                    if(r2 > 0):
                        httoUrlCounter2a += 1
                    else:
                        httoUrlCounter2b += 1
                        
                    r3 = getTrustManagerCount(join(path1,fileName))
                    if(r3 > 0):
                        httoUrlCounter3a += 1
                    else:
                        httoUrlCounter3b += 1
                        
                    r4 = getContextCount(join(path1,fileName))
                    if(r4> 0):
                        httoUrlCounter4a += 1
                    else:
                        httoUrlCounter4b += 1
                    
                    r5 = getWebSettingsCount(join(path1,fileName))
                    if(r5> 0):
                        httoUrlCounter5a += 1
                    else:
                        httoUrlCounter5b += 1
                        
                    r6 = getWebWebViewCount(join(path1,fileName))
                    if(r6> 0):
                        httoUrlCounter6a += 1 
                    else:
                        httoUrlCounter6b += 1
                     
                    r7 = getHttpGetCount(join(path1,fileName))
                    if(r7> 0):
                        httoUrlCounter7a += 1
                    else:
                        httoUrlCounter7b += 1
                    r8 = getSchemeRegistryCount(join(path1,fileName))
                    if(r8> 0):
                        httoUrlCounter8a += 1
                    else:
                        httoUrlCounter8b += 1
                if (fileName.endswith('AndroidManifest.xml') and auxCountVul==0):
                    r10 = getHttpGetPerm(join(path1,fileName))
                    auxCountVul+=1
            try:
                reportCsvFile.write('\n')
                reportCsvFile.write(f+ ';'+str(((httoUrlCountera / (httoUrlCountera + httoUrlCounterb)) * 100 )))
                reportCsvFile.write( ';'+str(((httoUrlCounter1a / (httoUrlCounter1a + httoUrlCounter1b)) * 100 )))
                reportCsvFile.write( ';'+str(((httoUrlCounter2a / (httoUrlCounter2a + httoUrlCounter2b)) * 100 )))
                reportCsvFile.write( ';'+str(((httoUrlCounter3a / (httoUrlCounter3a + httoUrlCounter3b)) * 100 )))
                reportCsvFile.write( ';'+str(((httoUrlCounter4a / (httoUrlCounter4a + httoUrlCounter4b)) * 100 )))
                reportCsvFile.write( ';'+str(((httoUrlCounter5a / (httoUrlCounter5a + httoUrlCounter5b)) * 100 )))
                reportCsvFile.write( ';'+str(((httoUrlCounter6a / (httoUrlCounter6a + httoUrlCounter6b)) * 100 )))
                reportCsvFile.write( ';'+str(((httoUrlCounter7a / (httoUrlCounter7a + httoUrlCounter7b)) * 100 )))
                reportCsvFile.write( ';'+str(((httoUrlCounter8a / (httoUrlCounter8a + httoUrlCounter8b)) * 100 )))
                reportCsvFile.write( ';'+ containsVulnerability(r10, b'READ_CALENDAR'))
                reportCsvFile.write( ';' + containsVulnerability(r10, b'WRITE_CALENDAR' ))
                reportCsvFile.write( ';' + containsVulnerability(r10, b'CAMERA') )
                reportCsvFile.write( ';' + containsVulnerability(r10, b'READ_CONTACTS'))
                reportCsvFile.write( ';' +  containsVulnerability(r10, b'WRITE_CONTACTS'))
                reportCsvFile.write( ';' + containsVulnerability(r10, b'GET_ACCOUNTS'))
                reportCsvFile.write( ';' + containsVulnerability(r10, b'ACCESS_FINE_LOCATION'))
                reportCsvFile.write( ';'  + containsVulnerability(r10, b'ACCESS_COARSE_LOCATION'))
                reportCsvFile.write( ';' + containsVulnerability(r10, b'RECORD_AUDIO'))
                reportCsvFile.write( ';' + containsVulnerability(r10, b'READ_PHONE_STATE'))
                reportCsvFile.write( ';' + containsVulnerability(r10, b'CALL_PHONE'))
                reportCsvFile.write( ';' + containsVulnerability(r10, b'READ_CALL_LOG'))
                reportCsvFile.write( ';' + containsVulnerability(r10, b'WRITE_CALL_LOG' ))
                reportCsvFile.write( ';' + containsVulnerability(r10, b'ADD_VOICEMAIL')) 
                reportCsvFile.write( ';' + containsVulnerability(r10, b'USE_SIP' ))
                reportCsvFile.write( ';' + containsVulnerability(r10, b'PROCESS_OUTGOING_CALLS' ))
                reportCsvFile.write( ';' + containsVulnerability(r10, b'BODY_SENSORS' ))
                reportCsvFile.write( ';' + containsVulnerability(r10, b'SEND_SMS' ))
                reportCsvFile.write( ';' + containsVulnerability(r10, b'RECEIVE_SMS' ) )
                reportCsvFile.write( ';' + containsVulnerability(r10, b'READ_SMS' ))
                reportCsvFile.write( ';' + containsVulnerability(r10, b'RECEIVE_WAP_PUSH' ))
                reportCsvFile.write( ';' + containsVulnerability(r10, b'RECEIVE_MMS' ))
                reportCsvFile.write( ';' + containsVulnerability(r10, b'READ_EXTERNAL_STORAGE' ) )
                reportCsvFile.write( ';' + containsVulnerability(r10, b'WRITE_EXTERNAL_STORAGE') ) 
            except:
                reportCsvFile.write( f+ ';' + 'problem' )
            """try:
                shutil.rmtree(join(path1,f[:-4]))
            except ValueError:
                print('error' + str(ValueError))"""
reportCsvFile.close()

            

import sys,random,string

alphabet="abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPER="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
polybiusSquare=[
 ['a','b','c','d','e'],
 ['f','g','h','i','k'],
 ['l','m','n','o','p'],
 ['q','r','s','t','u'],
 ['v','w','x','y','z']
]

DEBUG=True
def getKeyStream(key,text):
 keyStream=[]
 ki=0
 for i in range(len(text)):
  if text[i].isalpha():
   keyStream.append(key[ki%len(key)])
   ki+=1
  else:
   keyStream.append(text[i])
 return keyStream
def encryptVigenere(text,key):
 result=""
 keyStream=getKeyStream(key,text)
 for i in range(len(text)):
  ch=text[i]
  if ch.islower():
   pi=alphabet.index(ch)
   ki=alphabet.index(keyStream[i].lower())
   ci=(pi+ki)%26
   result+=alphabet[ci]
  elif ch.isupper():
   pi=ALPHABET_UPPER.index(ch)
   ki=ALPHABET_UPPER.index(keyStream[i].upper())
   ci=(pi+ki)%26
   result+=ALPHABET_UPPER[ci]
  else:
   result+=ch
 return result






def decryptVigenere(text,key):
 result=""
 keyStream=getKeyStream(key,text)
 for i in range(len(text)):
  ch=text[i]
  if ch.islower():
   ci=alphabet.index(ch)
   ki=alphabet.index(keyStream[i].lower())
   pi=(ci-ki)%26
   result+=alphabet[pi]
  elif ch.isupper():
   ci=ALPHABET_UPPER.index(ch)
   ki=alphabet.index(keyStream[i].lower())
   pi=(ci-ki)%26
   result+=alphabet[pi]
  else:
   result+=ch
 return result





def findInSquare(ch):
 if ch=='j':ch='i'
 for i in range(5):
  for j in range(5):
   if polybiusSquare[i][j]==ch:
    return i+1,j+1
 return None,None
def encryptPolybius(text):
 res=""
 for ch in text.lower():
  if ch.isalpha():
   r,c=findInSquare(ch)
   if r!=None:
    res+=str(r)+str(c)+" "
  else:
   res+=ch
 return res.strip()

def autodemo():
 tool=CipherTool()
 texts=["one","two","yhree"]
 for t in texts:
  k="key"
  e1=tool.encV(t,k)
    d1=tool.decV(e1,k)
  e2=tool.encP(t)




  d2=tool.decP(e2)
  print(t,e1,d1,e2,d2)



def decryptPolybius(code):
 res=""
 parts=code.split()
 for p in parts:
  if p.isdigit() and len(p)==2:
   r=int(p[0])-1
   c=int(p[1])-1
   if r>=0 and r<5 and c>=0 and c<5:
    res+=polybiusSquare[r][c]
  else:
   res+=p
 return res

def encryptCaesar(text,shift):
 res=""
 for ch in text:
  if ch.islower():
   i=alphabet.index(ch)
   res+=alphabet[(i+shift)%26]
  elif ch.isupper():
   i=ALPHABET_UPPER.index(ch)
   res+=ALPHABET_UPPER[(i+shift)%26]
  else:
   res+=ch
 return res

def decryptCaesar(text,shift):
 res=""
 for ch in text:
  if ch.islower():
   i=alphabet.index(ch)
   res+=alphabet[(i-shift)%26]
  elif ch.isupper():
   i=ALPHABET_UPPER.index(ch)
   res+=ALPHABET_UPPER[(i-shift)%26]
  else:
   res+=ch
 return res





def printMenu():
 print("1 Vigenere encrypt")
 print("2 Vigenere decrypt")
 print("3 Polybius encrypt")
 print("4 Polybius decrypt")
 print("5 Caesar encrypt")
 print("6 Caesar decrypt")
 print("7 Exit")

def doStuff():
 while True:
  printMenu()
  c=input("Choice:")
  if c=="1":
   t=input("Text:")
   k=input("Key:")
   print(encryptVigenere(t,k))
  elif c=="2":
   t=input("Text:")
   k=input("Key:")
   print(decryptVigenere(t,k))
  elif c=="3":
   t=input("Text:")
   print(encryptPolybius(t))
  elif c=="4":
   t=input("Code:")
   print(decryptPolybius(t))
  elif c=="5":
   t=input("Text:")
   s=int(input("Shift:"))
   print(encryptCaesar(t,s))
  elif c=="6":
   t=input("Text:")
   s=int(input("Shift:"))
   print(decryptCaesar(t,s))
  elif c=="7":
   break
  else:
   print("Wrong input")

class CipherTool:
 def __init__(self):
  self.history=[]

 def encV(self,text,key):
  r=encryptVigenere(text,key)
  self.history.append(("vig-enc",text,r))
  return r

 def decV(self,text,key):
  r=decryptVigenere(text,key)
  self.history.append(("vig-dec",text,r))
  return r

 def encP(self,text):
  r=encryptPolybius(text)
  self.history.append(("poly-enc",text,r))
  return r

 def decP(self,text):
  r=decryptPolybius(text)
  self.history.append(("poly-dec",text,r))
  return r

 def encC(self,text,shift):
  r=encryptCaesar(text,shift)
  self.history.append(("caesar-enc",text,r))
  return r

 def decC(self,text,shift):
  r=decryptCaesar(text,shift)
  self.history.append(("caesar-dec",text,r))
  return r




def testVigenere():
 samples=["Hello World","Attack At Dawn","Python"]
 key="secret"
 for s in samples:
  e=encryptVigenere(s,key)
  d=decryptVigenere(e,key)
  if DEBUG:
   print("VIG",s,e,d)



def testPolybius():
 samples=["hello","attack","polybius square"]
 for s in samples:
  e=encryptPolybius(s)
  d=decryptPolybius(e)
  if DEBUG:
   print("POLY",s,e,d)

class CipherTool:
 def __init__(self):
  self.history=[]




 def encV(self,text,key):
  r=encryptVigenere(text,key)
  self.history.append(("vig-enc",text,r))
  return r
 def decV(self,text,key):
  r=decryptVigenere(text,key)
  self.history.append(("vig-dec",text,r))
  return r
 def encP(self,text):
  r=encryptPolybius(text)
  self.history.append(("poly-enc",text,r))
  return r
 def decP(self,text):
  r=decryptPolybius(text)
  self.history.append(("poly-dec",text,r))
  return r

 def printHistory(self):
  for h in self.history:
   print(h)




def autoDemo():
 tool=CipherTool()
 texts=["demo one","demo two","crypto test"]
 for t in texts:
  k="key"
  e1=tool.encV(t,k)
  d1=tool.decV(e1,k)
  e2=tool.encP(t)
  d2=tool.decP(e2)
  print(t,e1,d1,e2,d2)




def main():
 if len(sys.argv)>1:
  if sys.argv[1]=="test":
   testVigenere()
   testPolybius()
  elif sys.argv[1]=="demo":
   autoDemo()
  else:
   doStuff()
 else:
  doStuff()

if __name__=="__main__":
 main()
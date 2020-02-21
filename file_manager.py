import os
import shutil
k=[]
def e(s):
    f=open(s,"rb")
    p=list(f.read())
    f.close()
    l=len(p)
    for i in range(n):
        t=k[i]
        for j in range(l):
            p[j]=(p[j]+(t%10))%256
            t=t//10
            if t==0:
                t=k[i]
    p=bytes(p)
    f=open(s,"wb")
    f.write(p)
    f.close()
    return

def enc():
    z=0
    print("Enter no of keys")
    global n
    n=int(input())
    print("Enter each key and press enter")
    for i in range(n):
        k.append(int(input()))
    s=input("Enter file path or a path to encrypt multiple files:")
    if s.find('.')>-1:
        e(s)
        z=z+1
    for root, dirs, files in os.walk(s):
        for file in files:
            try:
                e(root+'/'+str(file))
                print (root+'/'+str(file))
                z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)
    
def d(s):
    f=open(s,"rb")
    p=f.read()
    p=list(p)
    l=len(p)
    for i in range(n):
        t=k[i]
        for j in range(l):
            p[j]=(p[j]+256-(t%10))%256
            t=t//10
            if t==0:
                t=k[i]
    f.close()
    f=open(s,"wb")
    f.write(bytes(p))
    f.close
    return

def dec():
    z=0
    print("Enter no of keys")
    global n
    n=int(input())
    print("Enter each key and press enter")
    for i in range(n):
        k.append(int(input()))
    s=input("Enter file path or a path to decrypt multiple files:")
    if s.find('.')>-1:
        d(s)
        z=z+1
    for root, dirs, files in os.walk(s):
        for file in files:
            try:
                d(root+'/'+str(file))
                print (root+'/'+str(file))
                z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)

def searchfile():
    z=0
    s=input("Enter the similar file name:")
    for root, dirs, files in os.walk('/'):
        for file in files:
            try:
                if s in file:
                    print (root+'/'+str(file))
                    z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)

def searchext():
    z=0
    s=input("Enter the file extension:")
    for root, dirs, files in os.walk('/'):
        for file in files:
            try:
                if file.endswith(s):
                    print (root+'/'+str(file))
                    z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)

def searchhidden():
    z=0
    for root, dirs, files in os.walk('/'):
        for file in files:
            try:
                if file.startswith("."):
                    print (root+'/'+str(file))
                    z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)
    
def searchpath():
    z=0
    e=input("Enter the path:")
    if e.find('.')>-1:
        print(e)
    for root, dirs, files in os.walk(e):
        for file in files:
            try:
                print (root+'/'+str(file))
                z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)
    
def searcheverything():
    z=0
    for root, dirs, files in os.walk('/'):
        for file in files:
            try:
                print (root+'/'+str(file))
                z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)
    
def copyhidden():
    z=0
    d=input("Enter the destination :")
    for root, dirs, files in os.walk('/'):
        for file in files:
            try:
                if file.startswith("."):
                    shutil.copy2(root+'/'+file,d)
                    print (root+'/'+str(file))
                    z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)

def copyext():
    z=0
    d=input("Enter the destination :")
    e=input("Enter the extension:")
    for root, dirs, files in os.walk('/'):
        for file in files:
            try:
                if file.endswith(e):
                    shutil.copy2(root+'/'+file,d)
                    print (root+'/'+str(file))
                    z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)

def copypath():
    z=0
    d=input("Enter the destination :")
    e=input("Enter the path:")
    if e.find('.')>-1:
        shutil.copy2(e,d)
        print(e)
        z=z+1
    for root, dirs, files in os.walk(e):
        for file in files:
            try:
                shutil.copy2(root+'/'+file,d)
                print (root+'/'+str(file))
                z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)

def copyfile():
    z=0
    d=input("Enter the destination :")
    e=input("Enter the similar file name:")
    for root, dirs, files in os.walk('/'):
        for file in files:
            try:
                if e in file:
                    shutil.copy2(root+'/'+file,d)
                    print (root+'/'+str(file))
                    z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)

def copyeverything():
    z=0
    d=input("Enter the destination :")
    for root, dirs, files in os.walk('/'):
        for file in files:
            try:
                shutil.copy(root+'/'+file,d)
                print (root+'/'+str(file))
                z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)

def movehidden():
    z=0
    d=input("Enter the destination :")
    for root, dirs, files in os.walk('/'):
        for file in files:
            try:
                if file.startswith("."):
                    shutil.move(root+'/'+file,d)
                    print (root+'/'+str(file))
                    z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)

def moveext():
    z=0
    d=input("Enter the destination :")
    e=input("Enter the extension:")
    for root, dirs, files in os.walk('/'):
        for file in files:
            try:
                if file.endswith(e):
                    shutil.move(root+'/'+file,d)
                    print (root+'/'+str(file))
                    z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)

def movepath():
    z=0
    d=input("Enter the destination :")
    e=input("Enter the path:")
    if e.find('.')>-1:
        shutil.move(e,d)
        print(e)
        z=z+1
    for root, dirs, files in os.walk(e):
        for file in files:
            try:
                shutil.move(root+'/'+file,d)
                print (root+'/'+str(file))
                z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)

def movefile():
    z=0
    d=input("Enter the destination :")
    e=input("Enter the similar file name:")
    for root, dirs, files in os.walk('/'):
        for file in files:
            try:
                if e in file:
                    shutil.move(root+'/'+file,d)
                    print (root+'/'+str(file))
                    z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)

def moveeverything():
    z=0
    d=input("Enter the destination :")
    for root, dirs, files in os.walk('/'):
        for file in files:
            try:
                shutil.move(root+'/'+file,d)
                print (root+'/'+str(file))
                z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)

def delhidden():
    z=0
    for root, dirs, files in os.walk('/'):
        for file in files:
            try:
                if file.startswith("."):
                    os.remove(root+'/'+str(file))
                    print (root+'/'+str(file))
                    z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)

def delext():
    z=0
    e=input("Enter the extension:")
    for root, dirs, files in os.walk('/'):
        for file in files:
            try:
                if file.endswith(e):
                    os.remove(root+'/'+str(file))
                    print (root+'/'+str(file))
                    z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)

def delpath():
    z=0
    e=input("Enter the path:")
    if e.find('.')>-1:
        os.remove(e)
        print(e)
        z=z+1
    for root, dirs, files in os.walk(e):
        for file in files:
            try:
                os.remove(root+'/'+str(file))
                print (root+'/'+str(file))
                z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)

def delfile():
    z=0
    e=input("Enter the similar file name:")
    for root, dirs, files in os.walk('/'):
        for file in files:
            try:
                if e in file:
                    os.remove(root+'/'+str(file))
                    print (root+'/'+str(file))
                    z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)

def deleverything():
    z=0
    for root, dirs, files in os.walk('/'):
        for file in files:
            try:
                os.remove(root+'/'+str(file))
                print (root+'/'+str(file))
                z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)
    
def hide():
    z=0
    s=input("Enter your secret directory(folder)")
    os.chdir(s)
    f=input("Enter the path of the file:")
    if f.find('.')>-1:
        l=len(f)
        i=l-1
        file=""
        q=""
        while f[i]!='/':
            file=file+f[i]
            i=i-1
        l=len(file)
        i=l-1
        while i>-1:
            q=q+file[i]
            i=i-1
        q='.'+q
        os.rename(f,q)
        z=z+1
    for root, dirs, files in os.walk(f):
        for file in files:
            try:
                os.rename(root+'/'+file,'.'+file)
                z=z+1
            except:
                print("error")
    print("Number of files accessed : ",end="")
    print(z)
    
def checkyourhidden():
    z=0
    s=input("Enter your secret directory(folder)")
    for root, dirs, files in os.walk(s):
        for file in files:
            if file.startswith('.'):
                print(root+'/'+file)
                z=z+1
    print("Number of files accessed : ",end="")
    print(z)
    
#def restorehidden()
 #   z=0
            
global t
t=10
print("Welcome")
while t:
    print("MENU:")
    print("SEARCH operations:")
    print("1.File name				2.Extension(.mp4,.jpg etc)")
    print("3.Hidden files			4.File Path")
    print("5.Everything\n")
    
    print("DELETE operations:")
    print("6.File name				7.Extension(.mp4,.jpg etc)")
    print("8.Hidden files			9.File Path")
    print("10.Everything\n")
    
    print("COPY operations:")
    print("11.File name				12.Extension(.mp4,.jpg etc)")
    print("13.Hidden files			14.File Path")
    print("15.Everything\n")
    
    print("MOVE operations:")
    print("16.File name				17.Extension(.mp4,.jpg etc)")
    print("18.Hidden files			19.File Path")
    print("20.Everything\n")
    
    print("21.Encryption			22.Decryption\n23.Hide\n24.Check your hidden files\n0.Exit\n")
    print("Enter your choice\n")
    t=int(input())
    if t==1:
        searchfile()
    elif t==2:
        searchext()
    elif t==3:
        searchhidden()
    elif t==4:
        searchpath()
    elif t==5:
        searcheverything()
    elif t==6:
        delfile()
    elif t==7:
        delext()
    elif t==8:
        delhidden()
    elif t==9:
        delpath()
    elif t==10:
        deleverything()
    elif t==11:
        copyfile()
    elif t==12:
        copyext()
    elif t==13:
        copyhidden()
    elif t==14:
        copypath()
    elif t==15:
        copyeverything()
    elif t==16:
        movefile()
    elif t==17:
        moveext()
    elif t==18:
        movehidden()
    elif t==19:
        movepath()
    elif t==20:
        moveeverything()
    elif t==21:
        enc()
    elif t==22:
        dec()
    elif t==23:
        hide()
    elif t==24:
        checkyourhidden()

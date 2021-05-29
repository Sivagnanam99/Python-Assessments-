f=open("sample.txt","a")
f.write("\n I am Inserting into Sample File")
f.close()

f=open("sample.txt","r")
print(f.read())


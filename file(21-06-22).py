file=open("f1.txt","w")
print(" file is created")
file.write("hello world ")
file.close()
print("end of the file")
file=open("f1.txt","a")
file.write("hello manasa")
file.close()
file=open("f1.txt","r")
text=file.read()
text2=file.readlines()
print(text)
print(text2)
file.close()




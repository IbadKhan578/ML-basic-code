# I/o file handling 

# f=open("sample.txt","r")   # open a file with name and file mode as parameter, r stand for readonly 
# data= f.read()  # read func will return data of that file.
# print(data);
# f.close();


f = open("sample.txt","a+")

f.write("I belong to District Tando Muhammad Khan");
f.close();
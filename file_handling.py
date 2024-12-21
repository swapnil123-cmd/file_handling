file=open('code.txt', 'w')
file.write("Coding is cool")
file.close()

file=open('code.txt', 'a')
file.write("\n Coding is cool.")
file.close()

file=open("code.txt")
print(file.read())
file.close()

file=open("code.txt",'r')
Count=0

Content=file.read()
CoList=Content.split("\n")

for i in CoList:
  if i:
    Count+=1
    
print("This is the number of lines ",Count)

first_file=input("Enter first file's name: ")
second_file=input("Enter second file's name: ")

file1=open(first_file,'a')
file2=open(second_file,'r')


file1.write(file2.read())

file1.close()
file2.close()





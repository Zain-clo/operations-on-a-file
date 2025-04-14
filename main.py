

main = open("main.txt","r")
print(main.readlines())

main.close()



main = open("main.txt","r") 
for line in main:
         print(line)
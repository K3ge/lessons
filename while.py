#while_loop

#while True:
 #   print("{}hello ko ko".format(a))
a = 20
b = 22

while a<b: #false
    print("{} hello ko ko".format(a))
    a+=1
print("Nothing do!")

#break and continue
for va in "winhtut":
    if va == "i":
        break
    print(va)
print("------ending--------")

for va in "winhtut":
    if va == "i":
        continue
    print(va)
print("-----ending---------")


ls=[10,99,30,40,50] #list
 #  0   1 2  3  4  
data=99
found=False#flag
index=0

while index< len(ls): #true
    if ls[index]==data:
        found = True
        break
    index += 1 
if  not found:
    ls.append(data)
print(ls) 

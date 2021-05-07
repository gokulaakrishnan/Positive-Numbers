Mylist= []
n= int(input("Enter number of elements in your input"))
print("Enter a number as your see hastag")

for i in range(0,n):
    inp= int(input('#'))
    
    Mylist.append(inp)
    
pos_list=[]
    
for i in Mylist:
    if i>0:
        pos_list.append(i)
        
print(pos_list)

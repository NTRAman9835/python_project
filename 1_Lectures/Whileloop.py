fruits=['apple','banana','mango','strawberry']
fruits_len=len(fruits)
index=0
while index<fruits_len:
    if fruits[index]=='orange':
        fruits_found=True
        print("Orange is available")
        break
    index+=1
else:
    print("orange is not available")
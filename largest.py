largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
            break
    try: 
        float(num)
    except:
        print('Invalid input')
        continue
        
  
    if largest is None :
        largest=a 
    elif a > largest :
        largest = a
    print("Maximum is", largest)
    
  
for num in [input] :        
    if smallest is None :
        smallest = num
    elif num < smallest :
        smallest = num
    print("Minimum is", smallest)
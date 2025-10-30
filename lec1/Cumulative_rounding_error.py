def add_and_substract(iterations):
    result=1
    for i in range (iterations):
        result +=1/3
    for i in range (iterations):
        result -=1/3
    return result
print("\n Cumulative Rounding error:")
print(f"1+1/3 - 1/3={1+1/3 -1/3} ")
print(f"add_and_substract(100):{add_and_substract(100)}")  
print(f"add_and_substract(1000):{add_and_substract(1000)}")  
print(f"add_and_substract(10000):{add_and_substract(10000)}")
    
    
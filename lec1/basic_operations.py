import math
#for exploring the "math" module
#help(math)
#print(dir(math))


#Simple Arithmetic
print("2 + 3=",2+3)
print("2 - 3=",2-3)
print("2 * 3=",2*3)
print("2 / 3=",2/3)
print("2 ** 3=",2**3)

#Order of operations with parentheses
print("(3 * 4) / (2**2 + 4/2) =",(3 * 4) / (2**2 + 4 / 2))

#Using Math module Functions
print("Square root of 9 =",math.sqrt(9))#√9 = 3
print("Cos(pie/3) =",math.cos(math.pi/3))#cos(π/3) = 0.5
print("e^log(10)=",math.exp(math.log(10)))#eln(10)=10
print("e^log10(10)=",math.exp(math.log(10,10)))#elog10​(10)=e1

#special values
print("1 / infinity=",1/math.inf)
print("2 * infinity=",2*math.inf)
print("infinity / infinity =",math.inf/math.inf)

#Complex number
print("Complex Number 2+5j=",2+5j)
print("ANother way to represent=",complex(2,5))


input_data = open("input.txt","r")
data = input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
n = a * b 
if n == c:
    print("YES")
else:
    print("NO")
n = str(n)
output_data = open("output.txt","w")
output_data.write(n)
input_data.close()
output_data.close()

#are how many of blocks there
x = []

y = []

len_for_blocks = int(input("how many of blocks on each item?  : "))

print(len_for_blocks)

#gets blocks of x

i = 0

while i < len_for_blocks:
    x.append(input("enter num for X: "))
    i += 1

x = list(map(int, x))

i = 0

#gets blocks of y

while i < len_for_blocks:
    y.append(input("enter num for Y: "))
    i += 1

y = list(map(int, y))

i = 0
    







xy = [] 

i = 0 

while i < len_for_blocks:
  xy.append(x[i] * y[i])
    
  i += 1

i = 0 

xx = []
while i < len_for_blocks:
    xx.append(x[i]**2)
    i += 1


i = 0
yy = []
while i < len_for_blocks:
    yy.append(y[i]**2)
    i += 1


#here we get ⨊ for x
total_x = 0

for item in x:
    total_x = total_x + item
    
    
#here we get ⨊ for x

total_y = 0

for item in y:
    total_y = total_y + item


#here we get ⨊ for xy

total_xy = 0

for item in xy:
    total_xy = total_xy  + item



#here we get ⨊ for x**2

total_xx = 0 

for item in xx:
    total_xx = total_xx + item


    
#here we get ⨊ for y**2
total_yy = 0 
for item in yy:

    total_yy = total_yy + item

r = (len_for_blocks*(total_xy))-(total_x * total_y) 

r = round(r / round((((len_for_blocks*total_xx) - (total_x)**2)*((len_for_blocks*total_yy) - (total_y)**2))**0.5, 2),2)


print("the answer is : " + str(r))
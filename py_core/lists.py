gips = [55, 23, 23, 11, 54]
print (gips, end="\n")
for i in range(0,5):
    print (gips[i])

for i in range(0, len(gips)):
    print (gips[i])

for i in range(len(gips)):
    print (f"{i} is {gips[i]}")

print("-----------------------")

count = 0
for i in gips:
    if i % 2 == 0:
        count = count + 1
        print (i)
print (count)
print("-----------------------")
for i in range(len(gips)-1, -1, -1):
    print (gips[i], end=" ")

print("-----------------------")

my_list = [-51, 86, 1245, 4434, 5000, 100, 150, 250]
print (max(my_list))
largest = my_list[0]
for i in my_list:
    if i > largest:
        largest = i
print (largest)
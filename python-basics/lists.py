office= ["Michael", "Jim", "Pam", "Oscar", "Toby", "Kevin", "Dwight", "Dwight"]
print(office[1])
print(office.count("Dwight"))
print(office[0])
print(office[-1])
print(office[1:4])
print(office[0:3])
print(office[4:])
office[3]= "Angela"
print(office)
office.append("Creed")
office.insert(3, "Ryan")
print(office)
office.remove("Angela")
print(office)
office.pop()
print(office)
office.pop(2)
print(office)
print(office.index("Toby"))
office.sort()
print(office)

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(number_grid[0][0])
print(number_grid[1][1])
for row in number_grid:
    print(row)
for row in number_grid:
    for item in row:
        print(item)
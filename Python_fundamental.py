# SECTION ONE


#1 Adding "Fish" to the end, append( )
market = ["Yam", "Tomato", "Onion"]
market.append("Fish")
print(market)



# 2. Inserting 85 at index 1, insert( )
grades = [80, 90, 70]
grades.insert(1, 85)
print(grades)



#3. Removing the first "Phone", remove( )
gadgets = ["Laptop", "Phone", "Tablet", "Phone"]
gadgets.remove("Phone")
print(gadgets)



#4. Empty the list, clear( )
colors = ["Red", "Blue", "Green"]
colors.clear()
print(colors)


#5. Count "Yes", count( )
votes = ["Yes", "No", "Yes", "Yes", "No"]
votes.count("Yes")
print(votes.count("Yes"))



#6. Slice ["c", "d", "e"], 
alphabets = ["a", "b", "c", "d", "e", "f"]
alphabets[2:5]
print(alphabets)


#7. Reverse list, reverse( )
students = ["Kofi", "Ama", "Yaw"]
students.reverse()
print(students)


#8. Extend list, extend( )
list_a = [1, 2]
list_b = [3, 4]
list_a.extend(list_b)
print(list_a)


#9. Pop "Tamale", pop ( )
cities = ["Accra", "Kumasi", "Tamale"]
removed_city = cities.pop(2)
print(cities)



#10. Find index of "Ruler", index ( )
items = ["Pen", "Ruler", "Eraser"]
items.index("Ruler")
print(items.index("Ruler"))






# SECTION TWO


# 1. Tuple immutability error
#student_info = ("Araba", 20)
#student_info[1] = 21



# 2. Convert tuple → list → tuple
tup = (1, 2, 3)
temp = list(tup)
temp.append(4)
tup = tuple(temp)
print(tup)



# 3. Count 10
data = (10, 20, 10, 30, 10)
data.count(10)
print(data.count(10))



#4. Index of "Blue"
colors = ("Red", "Blue", "Green")
colors.index("Blue")
print(colors.index("Blue"))



#5. Tuple unpacking
coords = (5.6, -0.1)
lat, lon = coords



# 6. Nested structure
nest = []
nest.append((5, 10))
len(nest)
print(nest)



# 7. Slice last two
numbers = (10, 20, 30, 40, 50)
numbers[-2:]
print(numbers[-2:])



# 8. Extend with tuple
my_list = [1, 2]
my_list.extend((3, 4))
print(my_list)



# 9. Delete tuple
#del my_tup



# 10. Type check
x = (5)
y = (5,)
type(x)
type(y)
print(type(x))
print(type(y))
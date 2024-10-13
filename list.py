hobbies=[]
hobbies.append("playing football")
hobbies.append("reading")
hobbies.append("playing piano")
hobbies.append("drawing")
hobbies.append("programming")
print(hobbies)


#remove items
hobbies.remove("drawing")
print(hobbies)

#modifying 
hobbies[0]="sewing"
print(hobbies)

#pop an item
hobbies.pop(2)
print(hobbies)

#insert items
hobbies.insert(3,"gardening")
print(hobbies)

numbers=[57,96,74,29,41,65,30]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

print(len(numbers))


for item in numbers:
    print(item)
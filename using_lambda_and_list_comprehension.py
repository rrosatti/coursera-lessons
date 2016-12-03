my_list = []
for i in range(0, 50):
	my_list.append(i)

# getting even numbers using list comprehension
even_numbers = [n for n in my_list if (n%2) == 0]
print even_numbers


# using lambda
add_three = lambda x : x + 3

for n in even_numbers:
	print add_three(n), 

print ['a', 'b', 'c'] + [1, 2, 3]

# # handling errors and exceptions
# try:
#     file = open("Data_file.txt")
#     a_dic = {'key':'value'}
#     print(a_dic['key1'])
# except FileNotFoundError:
#     file = open("Data_file.txt", "w")
#     file.write("something is here")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError

# # ex
# height = float(input("Height : "))
# weight = int(input("Weight : "))
# if height > 3:
#     raise ValueError("Human height should not be over 3 M")
# else:
#     BMI = weight / height ** 2
#     print(BMI)


# Challenge 1
fruits = ["Apple", "Pear", "Orange"]
def make_pie (index):
    try:
        fruit = fruits[index]
    except IndexError:
        print('Fruit Pie')
    else:
        print(fruit + " pie")

make_pie(4)

# Challenege 2
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0
for post in facebook_posts:
    try: 
        total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes += 0

print(total_likes)



















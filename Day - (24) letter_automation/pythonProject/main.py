# # read a file
# with open('y_file.txt', mode = 'r') as file:
#     content = file.read()
#     print(content)
#
# # write to the file, this mode deleted
# # the previous content and writes new content to it
# with open('my_file.txt', mode='w') as file:
#     file.write('Tannaz')
#
# # adds text to the ends of the text line, doesn't delete the previous text
# with open('my_file.txt', mode='a') as file:
#     file.write('end of the line ')
#
# # in case od new line
# with open('my_file.txt', mode='a') as file:
#     file.write('\n new line and end of the line ')

# Mail Merging Project
# automated inviting letter

# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names_files:
    names = names_files.readlines()

with open('Input/Letters/starting_letter.txt') as letter_file:
    letter_content = letter_file.read()

for name in names:
    stripped_names = name.strip()
    new_letter = letter_content.replace(PLACEHOLDER, name)
    with open(f"Output/ReadyToSend/letter_for_{stripped_names}.txt", mode='w') as completed:
        completed.write(new_letter)































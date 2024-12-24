
user_input = input("Please enter a string: ")


frame_width = 30


border = '*' * frame_width


padding = (frame_width - len(user_input)) // 2


center_line = ' ' * padding + user_input + ' ' * (frame_width - len(user_input) - padding)


print(border)
print(center_line)
print(border)

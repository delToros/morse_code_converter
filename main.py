from morse_code import morse_code_dict


user_input = input('Please enter what you wish to translate to morse code.'
                   '\nEnglish letter, symbols .,!?-/@(), 0-9\n').lower()

user_input_list = [*user_input]
# print(user_input_list)

morse_output = [ morse_code_dict[item] if item != " " else "/" for item in user_input_list]

print(' '.join(morse_output))



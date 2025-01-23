# Cindy Kuang 
# Homework 7 Problem 1
# March 20, 2024
# This program reads a command txt.file 
# It uses the key given in the first line of the command file 
# and depending on whether line two specifies "encrypt" or "decrypt" mode 
# It then performs the translation on the text file given in line 3 of the command file
# and writes it in the file given in line 4 of the command file.  

from cipher import translate

def decryption_program(command):

    # Set up alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Set up directory pathway
    directory_path = "command_files_for_testing/"

    # Open command file
    command_file_name = directory_path + command
    command_file = open(command_file_name, 'r')
    
    # Read from command file
    with command_file as com: 
        key_file_name = directory_path + com.readline().strip()
        program_mode = str(com.readline().strip())
        input_file_name = directory_path + com.readline().strip()
        output_file_name = directory_path + com.readline().strip()

    # Open files and create key
    key_file = open(key_file_name, 'r')
    key = key_file.readline()
    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')

    # Set up translation function based on mode 
    if program_mode == "encrypt":
        to_letters = key
        from_letters = alphabet
    elif program_mode == "decrypt":
        from_letters = key 
        to_letters = alphabet 
    else:
        print("Error, mode not set as encrypt or decrypt")
        exit()

    # Extract lines from input file in order, translate them, and then write
    # them into the output file
    input_line = input_file.readline()
    with output_file as file:
        while input_line != '':
            processed_text_line = translate(from_letters, to_letters, input_line)
            file.write(processed_text_line)
            input_line = input_file.readline()

    # Close all files
    command_file.close()
    key_file.close()
    input_file.close()
    output_file.close()

def main():
    decryption_program('commands_test.txt')

main()





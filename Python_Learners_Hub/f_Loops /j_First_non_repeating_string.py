def first_non_repeating_char_index (string): 
    check_str = string.upper()
    for i in range(len(string)):
        if check_str.count(check_str[i]) == 1:
            print("Unique character is:",string[i],"and its index is",i)
    return

string = input("Enter the string to find the first non repeating character: \n")
first_non_repeating_char_index(string)

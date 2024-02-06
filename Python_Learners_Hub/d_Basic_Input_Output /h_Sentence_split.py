sentence = input("Enter the sentence to split the sentence into words at the delimiter \" \" (space): \n")
# Approach 1st
# for i in range(0, len(sentence)):
#     if sentence[i] != " ":
#         print(sentence[i],end="")
#     if sentence[i] == " ":
#         print()
#         i+=1

# Approach 2nd
sen = sentence.split(" ")
for i in sen:
    print(i)        

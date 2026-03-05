str = "Ibad Khan";
print(len(str));  # function to find the length of the string.
print(str);       
print(str[0:4]) # string slicing
print(str[0:len(str)]); # this too is valid for the last index 
print(str[0:])   # this too is valid to reach till the last index


# String functions
check= str.endswith("an")  # check if string ends with an and return true 
print(check);

print(str.capitalize());   # capitilize first character of the string.

print(str.replace("I","i"))    # replace letters in the string.

print(str.find("Khan"))     # return first index of first occurence.

print(str.count("a"));      # count the occurence of the substring.
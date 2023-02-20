def most_frequent(string):
    # Create an empty dictionary to store the frequency of each character
    freq_dict = {}
  
    # Count the frequency of each character in the string
    for char in string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
  
    # Sort the characters in the dictionary by frequency
    sorted_chars = sorted(freq_dict, key=freq_dict.get, reverse=True)
  
    # Print the characters in decreasing order of frequency
    for char in sorted_chars:
        print(char, freq_dict[char])
    #use most_frequent("mississippi") to get the values

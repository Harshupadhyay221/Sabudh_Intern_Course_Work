def most_common_word(text):
    # Convert the text to lowercase to make the search case-insensitive
    text = text.lower()
    
    # Use regex to find all words (alphanumeric sequences)
    words = re.findall(r'\b\w+\b', text)
    
    # Use Counter to count the frequency of each word
    word_counts = Counter(words)
    
    # Find the word with the maximum count
    most_common = word_counts.most_common(1)[0]
    
    return most_common[0]
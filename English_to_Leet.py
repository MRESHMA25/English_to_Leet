# Reshma Sri Murakonda
# 101282055

import string

# Changes = changing words into short forms (Acronyms)
# Homoglyphs = changing letters to symbols
changes = {
    'LAUGHING OUT LOUD': 'LOL',
    'AS SOON AS POSSIBLE': 'ASAP',
    'I DONT KNOW': 'IDK',
    'TO BE HONEST': 'TBH'
}
homoglyphs = {'O': '0', 'S': '5', 'A': '@', 'M': '^^'}

def remove_punctuation(text):
    return ''.join(char for char in text if char not in string.punctuation)

def to_uppercase(text):
    return ''.join(chr(ord(char) - 32) if 'a' <= char <= 'z' else char for char in text)

def replace_with_acronyms(text):
    words = text.split()
    i = 0
    while i < len(words):
        for length in range(4, 0, -1):  # Check for phrases up to 4 words long
            phrase = ' '.join(words[i:i+length])
            if phrase in changes:
                words[i] = changes[phrase]
                del words[i+1:i+length]
                break
        i += 1
    return ' '.join(words)

def replace_with_homoglyphs(text):
    return ''.join(homoglyphs.get(char, char) for char in text)

def main():
    user_input = input("Enter a string/message: ")
    
    # Step 1: Remove punctuation
    no_punctuation = remove_punctuation(user_input)
    print("After removing punctuation:", no_punctuation)
    
    # Step 2: Convert to uppercase
    uppercase = to_uppercase(no_punctuation)
    print("After converting to uppercase:", uppercase)
    
    # Step 3: Replace with acronyms
    with_acronyms = replace_with_acronyms(uppercase)
    print("After replacing with acronyms:", with_acronyms)
    
    # Step 4: Replace with homoglyphs
    final_result = replace_with_homoglyphs(with_acronyms)
    print("Final result:", final_result)

if __name__ == "__main__":
    main()

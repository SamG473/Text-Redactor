

def is_banned(word: str, banned: list[str]) -> bool:
    """Return True if word is in the banned list, ignoring case."""
    for w in banned:
        if w.lower() == word.lower():
            return True
    return False 


def mask(word: str) -> str:
    """Return a string of "#" same length as the word."""
    return "#" * len(word)


def redact(text: str, banned: list[str]) -> str:
    """Replace each banned word in text with '#', leaving all non-letters unchanged."""
    current_word = ""
    result = []
    
    for letter in text:
        if letter.isalpha(): 
            current_word += letter 
        else: 
            if is_banned(current_word, banned):
                result.append(mask(current_word)) 
            else: 
                result.append(current_word)
            result.append(letter)
            current_word = ""

    if current_word:
        if is_banned(current_word, banned):
            result.append(mask(current_word))
        else: 
            result.append(current_word)
           
    return "".join(result)
              

if __name__ == "__main__":
    print(redact("The quick brown fox jumps over the lazy dog.", ["fox", "dog"]))

    




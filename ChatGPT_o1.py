import random
import re

# -----------------------------------------
# Helper Functions ("Fools")
# Each of these small functions performs
# a naive text transformation.
# -----------------------------------------

def remove_excess_punctuation(text: str) -> str:
    """
    Fool #1:
    Replace multiple punctuation marks (e.g., '!!!', '??')
    with a single version of the character.
    """
    # Replace any sequence of punctuation (non-word, non-space) with a single character
    return re.sub(r'([^\w\s])\1+', r'\1', text)

def inject_random_adjectives(text: str) -> str:
    """
    Fool #2:
    Insert random adjectives before certain nouns to create
    a silly transformation.
    """
    adjectives = ["strange", "mysterious", "ridiculous", "fascinating", "peculiar"]
    # We'll target a simple pattern of 'the <noun>' to prepend with a random adjective
    def repl(match):
        return "the {} {}".format(random.choice(adjectives), match.group(1))
    return re.sub(r'the\s+(\w+)', repl, text, flags=re.IGNORECASE)

def random_synonym_swap(text: str) -> str:
    """
    Fool #3:
    For demonstration, let's just swap some words with 'synonyms'
    from a small dictionary. 
    """
    synonyms = {
        "happy": ["glad", "joyful", "pleased"],
        "sad": ["unhappy", "sorrowful", "blue"],
        "big": ["large", "huge", "gigantic"],
        "small": ["tiny", "little", "miniature"]
    }
    
    words = text.split()
    for i, word in enumerate(words):
        base_word = re.sub(r'[^\w]', '', word.lower())
        if base_word in synonyms:
            # Randomly pick a synonym
            new_word = random.choice(synonyms[base_word])
            # Preserve original punctuation/capitalization if we want to be fancy
            # For simplicity, we just replace with the synonym
            words[i] = new_word
    
    return " ".join(words)

def shuffle_sentences(text: str) -> str:
    """
    Fool #4:
    Randomly shuffle sentences to create 'chaos'
    that might inadvertently yield insight.
    """
    # Split on sentence-ending punctuation, keeping delimiters.
    sentences = re.split(r'([.!?])', text)
    # The split will return fragments like ["Hello", ".", " How are you", "?", " ..."]
    # We can recombine them into sentences, ignoring empty strings.
    # A quick way is to zip each sentence body with its delimiter:
    chunked = ["".join(pair) for pair in zip(sentences[0::2], sentences[1::2])]
    # If there's a leftover chunk, append it:
    if len(sentences) % 2 != 0:
        chunked.append(sentences[-1])
    
    random.shuffle(chunked)
    return " ".join(chunked).strip()

def naive_summary(text: str) -> str:
    """
    Fool #5:
    Attempt to 'summarize' by taking the first half 
    of the sentences and ignoring the rest. 
    This is obviously a naive approach, but combined
    with prior 'fools' may yield something interesting.
    """
    sentences = re.split(r'([.!?])', text)
    # Reconstruct chunked sentences
    chunked = ["".join(pair) for pair in zip(sentences[0::2], sentences[1::2])]
    
    # Take half
    half = len(chunked) // 2
    selected = chunked[:half] if half else chunked
    return " ".join(selected).strip()

# -----------------------------------------
# The "Chain-of-Fools" Pipeline
# -----------------------------------------

def chain_of_fools(text: str) -> str:
    """
    Applies each 'foolish' transformation in sequence:
      1) Remove excess punctuation
      2) Inject random adjectives
      3) Swap some words with naive synonyms
      4) Shuffle sentences
      5) Naively summarize
    """
    step1 = remove_excess_punctuation(text)
    step2 = inject_random_adjectives(step1)
    step3 = random_synonym_swap(step2)
    step4 = shuffle_sentences(step3)
    result = naive_summary(step4)
    return result

# -----------------------------------------
# Example Usage
# -----------------------------------------
if __name__ == "__main__":
    input_text = (
        "The cat was big. The dog was happy! "
        "I was sad about the small outcome. "
        "But everyone felt relieved when the big storm ended!!! "
        "Ultimately, we all enjoyed the celebration."
    )
    
    output_text = chain_of_fools(input_text)
    print("Original Text:")
    print(input_text)
    print("\nChain-of-Fools Output:")
    print(output_text)


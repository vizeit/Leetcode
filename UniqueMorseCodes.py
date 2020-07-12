
def uniqueMorseRepresentations(words):
    mc = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    return len(set(''.join([mc[ord(c)-ord('a')] for c in w]) for w in words))
    
if __name__ == "__main__":
    print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
    
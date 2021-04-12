def is_pangram(sentence):
    sentence = sentence.lower()
    print (f"Sentence in lower case is {sentence}")

    search = 'a'

    while ord(search) <= ord('z'):
        found = False
        for i in sentence:
            if search == i:
                found = True
                search = chr(ord(search)+1)
                break
        if found == False:
            return False
    return True
        
        

    

    

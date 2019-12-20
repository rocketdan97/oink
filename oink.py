import string

class Oink(object):
    '''
    your pig came home from summer camp and you can't understand them
    '''    
    @classmethod
    def translate(cls,input_string):
        '''
        translate that crap your pig is saying into ENGLISH
        '''
        assert isinstance(input_string, str), "source must be a string"

        input_string = input_string.strip().split(' ')
        output_string = ""
        
        for word in input_string:
            
            if not word[0] in string.digits:
            
                if Oink.is_vowel(word[0]):
                    output_string = output_string + " " + \
                    (word + "way" if not word[-1] in string.punctuation \
                     else word[:-1] + "way" + word[-1]) 

                elif Oink.is_vowel(word[1]):
                    output_string = output_string + " " + \
                    (word[1:] + word[0] + "ay" if not word[-1] in string.punctuation \
                     else word[1:-1] + word[0] + "ay" + word[-1])

                # word begins with two consonants
                elif Oink.is_vowel(word[2]):
                    output_string = output_string + " " + \
                    (word[2:] + word[0:2] + "ay" if not word[-1] in string.punctuation \
                     else word[2:-1] + word[0:2] + "ay" + word[-1])
                
                # word begins with three consonants
                elif Oink.is_vowel(word[3]):
                    output_string = output_string + " " + \
                    (word[3:] + word[0:3] + "ay" if not word[-1] in string.punctuation \
                     else word[3:-1] + word[0:3] + "ay" + word[-1])
                    
                # I don't think any English words start with four consonants
                # I also can't think of any words that might SEEM to start with four consonants that could throw off the system
                else: output_string = output_string + " " + word
                
            else: output_string = output_string + " " + word 
                
        return output_string[1:]
            
    @classmethod
    def is_vowel(cls, letter):
        if letter.lower() in 'aeiou':
            return True
        return False

    def oink(self, source):
        return Oink.translate(source)
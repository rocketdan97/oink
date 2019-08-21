import string

class Oink(object):
    '''
    your kid came home from summer camp and you can't understand them
    '''    
    @classmethod
    def translate(cls,input_string):
        '''
        translate that crap your kid is saying into ENGLISH
        '''
        assert isinstance(input_string,str), "source must be a string"

        input_string = input_string.strip().split(' ')

        return ' '.join([
            (
                word[1:] + word[0]+"way" \
                if not \
                    word[-1] in string.punctuation \
                else \
                    word[1:-1] + word[0]+"way"+word[-1]
            ) \
            if \
                Oink.is_vowel(word[0]) \
            else (
                word[1:] + word[0]+"ay" \
                if not \
                    word[-1] in string.punctuation \
                else \
                    word[1:-1] + word[0]+"ay"+word[-1]
            ) \
            for word in input_string \
            if word[0] not in string.digits
        ])

    @classmethod
    def is_vowel(cls,letter):
        if letter.lower() in ['a','e','i','o','u']:
            return True
        return False
        
    def oink(self,source):
        return Oink.translate(source)

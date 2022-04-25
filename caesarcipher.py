# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 03:08:47 2021

@author: gocan
"""

#Caesar Cipher

alphabet = 'abcdefghijklmnopqrstuvwxyz'

input_text = 'hello'

output = ''
for char in input_text:
    alpha_index = alphabet.find(char)
    output = output + alphabet[alpha_index+3]
    print(output)
    
# What if cipher goes beyond alphabet.

def shift_amount(i):
    '''Will determine the shift taking into account the length of the alphabet'''
    return i%26

# Now test with shift > 26.

output_1 = ''
for char in input_text:
    alpha_index = alphabet.find(char)
    output_1 = output_1 + alphabet[shift_amount(alpha_index+30)]
    print(output_1)
    
# A complete function.

def encrypt(text,required_shift):
    out_string = ''
    text = text.lower()
    for char in text:
        if char not in alphabet:       # take into account for spaces
            out_string = out_string + char
        else:
            alpha_index = alphabet.find(char)
            out_string = out_string + alphabet[shift_amount(alpha_index + required_shift)]
    return out_string
       
new_string = 'Once upon'
shift = encrypt(new_string,5)
print(shift)

big_daddy_kane = 'I cant hold back the flow cause im the man with soul. Control in effect what the heck rock the discoteque.'
                    
encrypt_big_daddy_kane = encrypt(big_daddy_kane,10)
print(encrypt_big_daddy_kane)

print(encrypt(encrypt_big_daddy_kane,-10))







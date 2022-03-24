'''
The Caesar Cipher: decrypting a message

The reverse transformation should now be clear to you - let's just present you with the code as-is, without any explanations.

Look at the code in the editor. Check carefully if it works. Use the cryptogram from the previous program.
'''

# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)

import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'abc')
# pattern = re.compile(r'cba')
pattern = re.compile(r'coreyms\.com')


matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print(text_to_search[1:4])
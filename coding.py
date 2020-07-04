encoding = [
'utf-8',
'cp500',
'utf-16',
'GBK',
'windows-1251',
'ASCII',
'US-ASCII',
'Big5'
]

correct_encoding = '';

for enc in encoding:
    try:
        open('output.docx', encoding=enc).read()
    except (UnicodeDecodeError, LookupError):
        pass
    else:
        correct_encoding = enc
        print('Done!')
        break


print(correct_encoding)
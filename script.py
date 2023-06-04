string = input("enter harvard style citation: ")


opn_par_inx = string.index('(')
cls_par_inx = string.index(')')


author = string[:opn_par_inx].strip()



year = string[opn_par_inx+1:cls_par_inx].strip()



string = string[cls_par_inx+2:]

for i in range(len(string)):
    if string[i]=='.' and string[i+2]=='[':
        break

title = string[:i].strip()



colon_inx = string.index(':')

publisher = None

if len(string[i:colon_inx]) > 23:
    publisher = string[i+10:colon_inx-14].strip()


string = string[colon_inx+1:-1]
date = None
url = string
if '[' in url:
    sqr_opn = url.index('[')
    url = url[:sqr_opn].strip()
    date = string[sqr_opn+9:-1].strip()
else:
    url.strip()


if date:
    date = date.replace('.','')

print()
final = f'{author} {year}, {title}{", "+publisher if publisher else ""}{", viewed "+date if date else ""}, <{url}>'
print(f'Harvard australian style citation: ')
print(final)




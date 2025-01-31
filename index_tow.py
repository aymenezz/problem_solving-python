number=input('name:').strip()
split_one=number[:-4]
split=number[-4:]
split_tow=split_one.replace(split_one,len(split_one) * '#')
print(split_tow+split)



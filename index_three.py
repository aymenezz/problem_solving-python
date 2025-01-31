import string as st
alpha=[0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def alphabet_position(text):
    empty=[]
    # makeS=' '
    txt=text.lower()
    for i in txt:
        if i in alpha:
            index = alpha.index(i)
            empty.append(str(index))
            
        else:
            continue
    makeS =' '.join(empty)
    return makeS

print(alphabet_position("The sunset sets at twelve o' clock."))



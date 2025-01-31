emptyst1=[]
def descending_order(value):
   conveValue=str(value)
   conveList=list(conveValue)
   conveList.sort(reverse=True)
   result=int(''.join(conveList))
   return result

print(descending_order(12345))

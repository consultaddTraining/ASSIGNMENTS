
import marshal

data={'name':'vishal','age':25}

bytes = marshal.dumps(data)
print(data)
print(bytes) # This thing you are going to send

read = marshal.loads(bytes)
print(read)

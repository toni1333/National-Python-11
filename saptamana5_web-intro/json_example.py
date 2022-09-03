import json

x = '{"name":"John", "age": 30,"city": "New York" }'
y=json.loads(x)
# y=dict(x)
# print(type(y))
a= {"name":"John", "age": 30,"city": "New York"}
print(type(a))
b=json.dumps(a)
print(type(b))

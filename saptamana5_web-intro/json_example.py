# import json
#
# x = '{"name":"John", "age": 30,"city": "New York" }'
# y=json.loads(x)
# # y=dict(x)
# # print(type(y))
# a= {"name":"John", "age": 30,"city": "New York"}
# print(type(a))
# b=json.dumps(a)
# print(type(b))


# JSON - JavaScriptObjectNotation
import json
x = '{"name": "Ion", "age": 30, "city": "Iasi"}'
y = json.loads(x)
print(y, type(y),'1')

z = y
print(z, json.dumps(z), type(z))
a = ["mere", "pere"]
print(a, json.dumps(a), type(a))
a = "hello"
print(a, json.dumps(a), type(a))
a = 42
print(a, json.dumps(a), type(a))
a = 31.75
print(a, json.dumps(a), type(a))
a = True
print(a, json.dumps(a), type(a))
a = None
print(a, json.dumps(a), type(a))
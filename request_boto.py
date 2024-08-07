# f = open("requirements.txt", "r")

# for i in f:
#     print(i)
# #print(f.read())
# f.close()

# import os
# # if os.path.exists("requirements.txt"):
# #     f = open("requirements.txt", "r")
# #     print(f.read())
# #     f.close()
# # else:
# #     print("File not found")

# cw = os.getcwd()
# li = os.listdir()
# print(cw)
# print(li)
import requests
x = requests.get('https://httpbin.org/get')
r = requests.get('https://api.github.com/events')
a = requests.post('https://httpbin.org/post', data={'key': 'value'})
# print(x.text)
# print(r.text)
print(a.text)

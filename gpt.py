import requests
import os

if not os.path.exists("data"):
    os.system("touch data")

while True:
    with open("data","r")as history:
        his=history.read()
        api="http://kumosb.top:11451/sb?ask=这是作为我(user)和你(ai)的聊天记录: '"+his+"' 现在请你读取这些聊天记录并理解 如果聊天记录为空则说明我们还未开始聊天 请注意不要在回答过程中表现出你读取过这些聊天记录的样子 接下来请回答我的下一句话:"
    query = input("\n用户：")
    if query == "stop":
        os.system("rm data && touch data")
        break
    if query == "clear":
        os.system("clear")
        os.system("rm data && touch data")
        continue
    response=requests.get(api+query)
    with open("data","a")as file:
        file.write("user: %s\nai: %s\n"%(query,response.text))
    print("AI: \033[1;34m%s\033[0m"%response.text)

import requests
import os

if not os.path.exists("data"):
    os.system("touch data")

while True:
    with open("data","r")as history:
        his=history.read()
        api="http://kumosb.top:11451/sb?ask=我们之前已经有了如下的聊天内容: '"+his+"' 其中我是用户 而你是AI 现在请你读取这些聊天记录 如果聊天记录为空则说明我们还未开始聊天 否则请你理解这些聊天记录后回答我的下一句话 但请注意不要在回答过程中表现出你读取过这些聊天记录的样子:"
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
        file.write("用户:%s\n\nAI:%s"%(query,response.text))
    print("AI: \033[1;34m%s\033[0m"%response.text)

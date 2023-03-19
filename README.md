# gpt-cli

一个使用3.5版本API的可在终端对话且可读取历史的小东西!

![](https://github.com/wzk0/photo/blob/main/Screenshot_20230319_143710_com.termux.jpg?raw=true)

## 使用

clone此仓库:

```sh
git clone https://github.com/wzk0/gpt-cli
```

安装requests:

```
pip install requests
```

运行:

```
python3 gpt.py
```

`stop`-退出

`clear`-清除历史

## 原理

每次都将对话写入一个文件 每次请求时都读取一遍文件

话术:

```
我们之前已经有了如下的聊天内容: '%s' 其中我是用户 而你是AI 现在请你读取这些聊天记录 如果聊天记录为空则说明我们还未开始聊天 否则请你理解这些聊天记录后回答我的下一句话 但请注意不要在回答过程中表现出你读取过这些聊天记录的样子:
```

API: http://kumosb.top:11451/sb?ask=

使用: https://github.com/THUDM/ChatGLM-6B/raw/main/cli_demo.py

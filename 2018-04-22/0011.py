'''
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
'''
user_input = input("请输入一个词语：")
with open('filtered_words.txt') as fr:
    words = fr.readlines()
    count = 0
    for word in words:
        word = word.strip()
        if user_input == word:
            print("Freedom")
            count += 1
    if count == 0:
        print("Human Rights")


import re
user_input = input("请输入一个词语：")
with open('filtered_words.txt') as fr:
    words = fr.readlines()
    for word in words:
        word = word.strip()
        if re.search(word, user_input):
            result = re.sub(word, "*"*len(word), user_input)
            print(result)
text = ''' 
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 
Flat is better than nested. Sparse is better than dense. Readability counts.
Special cases aren't special enough to break the rules. Although practicality beats purity. 
Errors should never pass silently.
Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea. 
Namespaces are one honking great idea -- let's do more of those!

美丽胜过丑陋。
显式优于隐式。
简单比复杂更好。
复杂比复杂更好。
优于嵌套。
稀疏优于密集。
可读性很重要。
特殊情况不足以打破规则。
虽然实用性胜过纯洁。
错误不应该默默地传递。
除非明确沉默。
面对困惑，拒绝猜测的诱惑。
应该有一个 - 最好只有一个 - 明显的方法来做到这一点。
虽然这种方式起初可能并不明显，除非你是荷兰人。
现在比永远好。
虽然现在永远不会比*正确好。
如果实施很难解释，这是一个坏主意。
如果实现很容易解释，那可能是个好主意。
命名空间是一个很棒的主意 - 让我们做更多的事情吧！
'''

from collections import Counter         # 调用 Counter 计数器
import re   
count = int()     # 给函数添加⼀一个int类型变量count，用于限制输出元素的个数
#定义一个名为 stats_text_en 的函数，函数接受一个字符串 text 作为参数。
def stats_text_en(text, count):    # 增加变量 count 控制输出
    ''' Count the English words in the text '''

    # 为 mymodule 下 stats_word.py 中的三个函数添加参数类型检查,用 isinstance 来实现
    # 如果输⼊参数不为字符串类型则抛出 ValueError 错误，并包含完整的错误提示信息
    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型, 输入类型 %s' % type(text))
    
    elements = text.split()
    words = []
    symbols = ',.*-!'
     
    for element in elements:
        for symbol in symbols:  #遍历清理
            element = element.replace(symbol,'') #将元素中的符号去除
        if len(element) and element.isascii():   
             # 计算集合元素个数，长度大于0，算一个真正的单词
             # 并用 str 类型 的 isascii 的方法判断是否是英文单词
            words.append(element)     #将非单词的空白，符号等去除，append()本身就是可变序列

    count_en = {}     # 更换定义名称
    word_set = set (words) #set 剔除重复值，减少遍历次数

    for word in word_set: #减少遍历次数 
        count_en [word] = words.count(word)
    return Counter(count_en).most_common(count)
    # 按词频排序并用 count 控制输出
    #return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的 return 相当于返回 None。
    
  
#统计参数中每个汉字出现的次数
#定义一个名为 stats_text_en 的函数，函数接受一个字符串 text 作为参数。
def stats_text_cn(text, count):         #增加变量 count 控制输出
    ''' Count the Chinese words in the text '''    # 使用文档字符串说明

    if not isinstance(text,str):
        raise ValueError('参数必须是 str 类型, 输入类型 %s' % type(text))

    cn_characters = []
   
    for character in text:
        # unicode 的中文取值范围
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    count_cn = {}       # 换一个名称定义
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        count_cn [character] = cn_characters.count(character)
    return Counter(count_cn).most_common(count)

print('统计英文词频==>',stats_text_en(text,100))
print('统计中文词频==>',stats_text_cn(text,100))



#字符串


#首字母大写  capitalize()方法
str = 'this is a question'
print(str.capitalize())

#返回指定的宽度且居中字符串      center(width,fillchar)   width:字符串总宽度(总长度)    fillchar：左右填充字符  用''括起来
str1 = 'runoob'
print(str1.center(100,'|'))      #设置字符小于字符串宽度，则直接返回字符串，不进行填充设置  奇数会优先补右边    偶数会优先补左边
print(str1.center(50))           #左右填充默认为空格
#print(str1.center(30,'/|'))     #左右填充只能是单个字符，多个字符会报错


#用于统计字符串里某个字符出现的次数，可选搜索开始于结束范围   count(sub,start=0,end=len(string))
#  sub:搜索字符串     start: 开始搜索索引位置      end:结束索引位置
str2 = 'www.runoob.com'
print(str2.count('o'))          #输出字符串中所有个数
print(str2.count('o',0,10))

#编码格式解码bytes对象       bytes.decode(encoding='utf-8',errors='strict')       encode:指定编码格式
str  = '菜鸟教程'
str_utf8 = str.encode("utf-8")        #设置编码格式
str_gbk = str.encode("GBK")
print(str_utf8)                       #打印编码
print(str_gbk)
print(str_utf8.decode('utf-8','strict'))            #打印解码后的
print(str_gbk.decode('GBK','strict'))               #打印解码后的

#判断字符串是否以指定后缀结尾  返回True False    endswitch(suffix,start,end)   suffix:可以是一个字符串也可是一个元素
str3 = 'Runoob example....wow'
print(str3.endswith('w'))           #单个判断
print(str3.endswith('0',0,19))      #加上索引查询条件

#把字符串中的tab符号\t转换为空格      expandtabs(tabsize=8)      tabsize:指定转换字符串中的tab符号
str4 = 'runoob\t12345\tabc'
print(str4.expandtabs())            #默认转换后
print(str4.expandtabs(2))           #第一个有6个字符是2的3倍，填充2个空格   第二个5个，不是2的倍数，填充1个
print(str4.expandtabs(5))

#检测字符串中是否包含子字符串若没有则返回-1     find(str,beg,end) 返回查找值开始的索引位置   str:检索的字符串   beg:查找开始位置
str5 = 'Runoob example....wow'
print(str5.find('exam'))            #返回查找的字符串首个所在索引号
print(str5.find('exam',8))          #返回查找字符串首个所在索引号，且从索引从8开始查找  若没有则返回-1
print(str5.find('o',0,10))          #返回查找字符串首个所在索引号，且查找区间索引在0-10之间，若没有则返回-1

#检测字符串中是否包含子字符串，若不在会报异常       index(str,beg,end) 输出查找值开始的索引位置
str6 = 'Runoob example....wow'
print(str6.index('o'))                 #返回查找的字符串首个所在索引号
print(str6.index('o',5))               #返回查找字符串首个所在索引号，且从索引从5开始查找  若没有则会报异常
print(str6.index('o',5,30))            #返回查找字符串首个所在索引号，且查找区间索引在0-10之间，若查找没有则会报异常

# 检测字符是否由字母和数字组成,有汉字也会返回True       isalnum()  返回True或False
str7 = 'runoob2021'                 #字符串包含字母和数字
print(str7.isalnum())          #True
str7 = 'www.runoob.com'              #字符串中不包含数字
print(str7.isalnum())          #False

#检测字符串是否只由字母或文字组成                     isalpha()  返回True或False
str7 = 'runoob'                       #字符串只包含字母
print(str7.isalpha())            #True
str7 = 'runoob你好'                     #字符串中包含字母和汉字
print(str7.isalpha())            #True
str7 = 'runoob !!!'                     #字符串中包含字母和标点符号
print(str7.isalpha())            #False

#检测字符串是否只由数字组成，不接受非【0-9】元素         isdigit()  返回True或False
str8 = '123456'                        #字符串只包含数字
print(str8.isdigit())            #True
str8 = 'Runoob example....wow123'       #字符串包含字母和数字
print(str8.isdigit())            #False

#检测字符串是否由小写字母组成                         islower()  返回True或False
str9 = 'Runoob Example ...wow'            #字符串中包含大写字母
print(str9.islower())            #False
str9 = 'runoob example ...wow'            #字符串中不包含大写字母
print(str9.islower())            #True

#检测字符串中是否只有数字组成： Unicode 数字，全角数字（双字节），罗马数字，汉字数字。指数类似 ² 与分数类似 ½ 也属于数字
#                                               # isnumeric()  返回True或False
str10 = 'wow123'                           #字符串中包含字母和数字
print(str10.isnumeric())            #False
str10 = '1233454545'                       #字符串中只包含数字
print(str10.isnumeric())            #True

#检测字符串是否只由空字符组成,空白符包含：空格、制表符(\t)、换行(\n)、回车(\r）,不算空白格
#                                                #isspace()  返回True或False
str11 = '   '                              #字符串中显示为空
print(str11.isspace())              #True
str11 ='runoob'                            #字符串中显示有字符
print(str11.isspace())              #False

#检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写        istitle()   返回True或False
str12 = 'This Is Runoob'                   #字符串中字母首字母为大写
print(str12.istitle())              #True
str12 = 'This is Runoob'                   #字符串中部分字母首字母为大写，部分小写
print(str12.istitle())              #False

#检测字符串中所有字母是否都为大写                             isupper()   返回True或False
str13 = 'THIS IS RUNOOB'                   #字符串中所有字母都为大写
print(str13.isupper())              #True
str13 = 'THIS is Runoob'                   #字符串中字母有大写也有小写
print(str13.isupper())              #False


#用于将序列中的元素以指定的字符连接成一个新的字符串               join(str)   str:需要进行拼接的元素组
tr1 = '-'
tr2 = '*'
tr3 = ['r','u','n','o','o','b']
print(tr1.join(tr3))
print(tr2.join(tr3))

#返回对象（字符，元组，列表等）长度或项目个数                    len(s)   s:对象
tr2 = 'runoob'
print(len(tr2))
tr2 = [1,2,3,4,5,6,7,]
print(len(tr2))

#返回一个原字符串左对齐，根据规定长度填充在右边，默认填充为空        ljust(width,fillchar) width:宽度 fillchar：填充字符
tr3 = 'runoob is good'
print(tr3.ljust(30))                         #fillchar:默认为空时
print(tr3.ljust(30,'*'))                     #fillchar:填充字符为’*‘

#转换字符串中的所有大写转换为小写                                  lower()
tr4 = 'RunooB Is gooD'
print(tr4.lower())

#截掉字符串左边的空格或指定字符                                 lstrip(chars)    chars:指定字符
tr5 = '      this is runoob   9999'
print(tr5.lstrip())
tr5 = '888    this id runoob  8888'          #截掉指定左边的字符’8‘
print(tr5.lstrip('8'))

#用于创建字符映射转换表 ,两个字符串的长度必须相同，为一一对应的关系，根据索引号对应     ***
#                                            maketrans(intab,outtab) intab:原字符 outtab:替换字符
intab = 'aeiou'
outtab = '12345'
str = 'this is string example....wow'
trantab = str.maketrans(intab,outtab)
print(str.translate(trantab))

#返回字符串中最大字母,有大小写同在，小写字母最大          max(str)   str:字符串
str = 'runoob'
# str = '23543734'
print(max(str))

#返回字符串中最小字母,有大小写同在，大写字母最小           min(str)   str:字符串
str = 'RunooB'
print(min(str))

#将字符串中的old（旧字符串）替换成new（新字符串）         replace(old,new,max)   max:替换不超过max次
str = 'www.w3cschool.cc'
print(str.replace('w3cschool.cc','runoob.com'))

str = 'this is string is is is example'
print(str.replace('is','was',3))                  #不超过三次

#返回字符串最后一次出现的位置,若没有匹配项返回-1          rfind(str,beg,end) 返回最后一个位置的首个索引号，从右边开始查找
str1 = 'this is really a string example'
str2 = 'is'
print(str1.rfind(str2))
print(str1.rfind(str2,6))                          #索引从6开始往后查找
print(str1.rfind(str2,4,10))                       #索引从4开始到10 区间

#返回在字符串中左后出现的位置，若没有匹配则报异常           rindex(str,beg,end)
str1 = 'this is runoob wow'
print(str1.rindex('is'))
#print(str1.rindex('is',6))                           #索引从6开始查找，未查找到，开始报错
print(str1.rindex('is',0,4))                          #索引从0到4区间开始查找

#返回一个原字符串右对齐，根据规定长度填充在左边，默认填充为空       rjust(width,fillchar)  width:宽度  fillchar:填充
str = 'this is runoob wow'
print(str.rjust(50,'*'))                              #向左填充

#删除字符串末尾指定字符（默认为空格），根据字符串中最后一个           rstrip(chars)   chars:指定删除的字符
str = '    this is runoob wow    **'
print(str.rstrip())                                    #删除末尾空格
print(str.rstrip('*'))                                 #删除最后一个字符为*的字符

#通过指定的分割符对字符串进行分割，默认为空格，结果以函数的形式返回         split(str='',num)  str:分隔符：字符串中的字符  num:分割次数
str = 'this is runoob wow'
print(str.split())                                       #默认以字符串中的空格为分隔符
print(str.split('i'))                                    #以字符串中的i为分隔符  同时截掉‘i’
print(str.split('i',1))                                  #以字符串中的i分割，且只分割一次 ，同时截掉分割的i

#返回一个包含各行作为元素的列表                                splitlines(keepends)   keepends:返回True或False
str = 'ab c\n\nde fg\rkl\r\n'
print(str.splitlines())                                    #换行符为分割点
print(str.splitlines(True))                                #为True则保留换行符

#检查是否以指定的子字符串开头，                                startswitch(str,beg,end)   返回True或False
str = 'this is runoob wow'
print(str.startswith('this'))             #True               #以指定的this开头
print(str.startswith('r',8))              #True               #查询是否下标从8开始，是否为r字符开头
print(str.startswith('r',2,8))            #False              #查询是否下标在2到8区间开始的‘r'字符开头

#用于移除字符串头尾指定的字符,只能删除开头或结尾字符               strip(chars)    chars:指定的字符串
str = '**this is runoob wow *'
print(str.strip('*'))                                    #删除前后指定的*
str = '* this is runoob * wow'
print(str.strip('*'))                                    #只删除头部的*，尾部结尾为W

#用于对字符串大小写字母进行转换                                 swapcase()  字符串中大写转换为小写，小写转换为大写
str = 'ThiS Is RUnooB WOw'
print(str.swapcase())

#返回标题化字符串，所有单词的首字母转化为大写                      title()
str = 'thid is runoob wow'
print(str.title())
str = 'this is runoob 3wow'                             #非字母后的第一个字母会转换为大写
print(str.title())

#根据参数table给出的表转换字符串的字符，要过滤掉字符放到参数中         translate()
#str.translate(table)                                    table -- 翻译表，翻译表是通过 maketrans() 方法转换而来
#bytes.translate(table[, delete])                        deletechars -- 字符串中要过滤的字符列表
#bytearray.translate(table[, delete])
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)  # 制作翻译表
str = "this is string example....wow!!!"
print(str.translate(trantab))
# 制作翻译表
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# 转换为大写，并删除字母o
print(b'runoob'.translate(bytes_tabtrans, b'o'))

#将字符串中的小写字母转为大写字母                                upper()
str = 'this is runoob wow excuse me'
print(str.upper())

#返回指定长度字符串，原字符串右对齐，前面填充0                      zfill(width) 指定字符串的长度
str = 'this is runoob wow thank you'
print(str.zfill(39))

#检查字符串中是否包含十进制字符                                isdecimal()   返回True 或False
str = 'runoob2021'
print(str.isdecimal())                 #False
str = '3323'
print(str.isdecimal())                 #True



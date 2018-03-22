import random   

filename = '1.txt'  # 一个很大的文本文件
f = open(filename,'r')  
nums = 1000  # 随机选取1000行

currentLineNum = nums  
random_lines = [] 

for i in range(nums):
	line = f.readline()  
    random_lines.append(line)  # 前1000行 
  
  
while True:  
    currentLine = f.readline()  
    if currentLine == '': 
        break  
    currentLineNum = currentLineNum + 1  
    r = random.randint(1,currentLineNum)  # 生成随机数
    if r < nums:  
        random_lines[r - 1] = currentLine  

print(len(random_lines))


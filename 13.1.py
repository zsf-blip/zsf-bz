s=input("请输入要读取的文件路径")
fo=open(s,"r")
l=[]
for line in fo:
    print(line)
    l.append(line)
fo.close()
m=input("请输入要写入的文件路径")
fu=open(m,"w")
fu.writelines(l)

# 500G 特殊一行的数据文件
#1.
# f = open()
# f.read(4096)  # 过长文本 不能一下子一行读取，但可以分段读一次4096个字符

def myreadlines(f, newline):
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline)]
        chunk = f.read(4096*10)
        if not chunk:
            yield buf
            break
        buf += chunk

with open("input.txt") as f:
    for line in myreadlines(f,"{|}"):
        print(line)



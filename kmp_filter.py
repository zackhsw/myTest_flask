# coding=utf-8
def kmp_match(s, p):
    m = len(s);
    n = len(p)
    cur = 0  # 起始指针cur
    table = partial_table(p)
    while cur <= m - n:  # 只去匹配前m-n个
        for i in range(n):
            if s[i + cur] != p[i]:
                cur += max(i - table[i - 1], 1)  # 有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                break
        else:  # for 循环中，如果没有从任何一个 break 中退出，则会执行和 for 对应的 else
            # 只要从 break 中退出了，则 else 部分不执行。
            return True
    return False


# 部分匹配表
def partial_table(p):
    '''''partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]'''
    prefix = set()
    postfix = set()
    ret = [0]
    for i in range(1, len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i + 1] for j in range(1, i + 1)}
        ret.append(len((prefix & postfix or {''}).pop()))
    return ret


if __name__ == '__main__':
    import re
    kk = ['六六六', '毒杀芬', '二溴氯丙烷', '杀虫脒', '二溴乙烷', '除草醚', '艾氏剂', '狄氏剂', '汞制剂', '砷类', '铅类', '敌枯双',
     '氟乙酰胺', '甘氟', '毒鼠强', '氟乙酸钠',
     '毒鼠硅', '甲胺磷', '甲基对硫磷', '对硫磷', '久效磷', '磷胺', '苯线磷', '地虫硫磷', '甲基硫环磷', '磷化钙', '磷化镁',
     '磷化锌', '硫线磷', '蝇毒磷', '治螟磷', '特丁硫磷', '氯磺隆', '福美胂', '福美甲胂',
     '胺苯磺隆单剂', '甲磺隆单剂', '百草枯水剂','甲磺隆复配制剂', '胺苯磺隆复配制剂']
    kk = ' '.join(kk)
    print('kk---',kk,'\n',re.findall('甘氟',kk))
    print(partial_table("六六"))
    print(kmp_match(kk, "久*效磷"))

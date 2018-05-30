
sentence0 = [['a','b'],[3,4],[1,2,3],[12,3]]
sentence1 = [[5,'b'],[7,8]]

def print_count(l):
    count = 0
    for i in l:
        if isinstance(i, list):
            count += 1
            print_count(i)
    return count


print(print_count(sentence0))     //打印4
print(print_count(sentence1))     //打印2
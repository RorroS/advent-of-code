i1 = 236491
i2 = 713787

def dec(num):
    sorted_num = sorted(list(str(num)))
    num_lst = list(str(num))
    return sorted_num != num_lst


def adj(num):
    len_num = len(str(num))
    len_set = len(set(str(num)))

    return len_num != len_set

def has_trips(num):
    num_lst = list(str(num))
    
    for i in range(5):
        if num_lst[i] == num_lst[i+1] and (i == 0 or num_lst[i] != num_lst[i-1]) and (i == 4 or num_lst[i+1] != num_lst[i+2]):
            return False
    return True

p1_passwords = [i for i in range(i1, i2+1) if not dec(i) and adj(i)]
res1 = len(p1_passwords)
p2_passwords = [i for i in range(i1, i2+1) if not dec(i) and not has_trips(i)]
res2 = len(p2_passwords)

print("p1:", res1, "\np2:", res2)

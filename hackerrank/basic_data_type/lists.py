if __name__ == '__main__':
    my_list = []
    N = int(input())
    step = 0
    
    while step < N:
        action = input().split()
        if action[0] == 'insert':
            ind = int(action[1])
            ins_num = int(action[2])
            my_list.insert(ind, ins_num)
        elif action[0] == 'print':
            print(my_list)
        elif action[0] == 'remove':
            rem_num = int(action[1])
            my_list.remove(rem_num)
        elif action[0] == 'append':
            appe_num = int(action[1])
            my_list.append(appe_num)
        elif action[0] == 'sort':
            my_list.sort()
        elif action[0] == 'pop':
            my_list.pop(-1)
        elif action[0] == 'reverse':
            my_list.reverse()
        step += 1
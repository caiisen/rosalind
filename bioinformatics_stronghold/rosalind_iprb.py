def cal_offspring_prb(parent1, parent2):
    '''return offspring genotype probability'''
    AA = parent1[0] * parent2[0]
    Aa = parent1[0] * parent2[1] + parent1[1] * parent2[0]
    aa = parent1[1] * parent2[1]
    offspring = [AA, Aa, aa]
    return offspring

def cal_randomly_selection(parent_list):
    offspring = []
    raw_list = parent_list[:]
    for parent1 in raw_list:
        del parent_list[0]
        if len(parent_list) == 0:
            break
        else:
            for parent2 in parent_list:
                offspring.append(cal_offspring_prb(parent1, parent2))
    return offspring

with open('rosalind_iprb.txt', 'r') as input_file:
    content = input_file.read().strip().split()
    parent_list = []
    for i in range(int(content[0]), 0, -1):
        parent_list.append([1, 0])
    for i in range(int(content[1]), 0, -1):
        parent_list.append([0.5, 0.5])
    for i in range(int(content[2]), 0, -1):
        parent_list.append([0, 1])
    
    offspring = cal_randomly_selection(parent_list)
    a = 0
    b = 0
    c = 0
    for i in offspring:
        a = a + i[0]
        b = b + i[1]
        c = c + i[2]
    print((a + b) / (a + b + c))
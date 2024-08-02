import json
import os
import pickle
def create_folder_if_not_exists(file_path):
    # 获取文件夹路径
    folder_path = os.path.dirname(file_path)

    # 检查文件夹是否存在，如果不存在则创建
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"文件夹已创建: {folder_path}")
    else:
        print(f"文件夹已存在: {folder_path}")

def get_max(lists):
    max = -1
    p = []
    for i in range(0, len(lists)):
        if lists[i] >= max:
            max = lists[i]
    for i in range(0, len(lists)):
        if lists[i] == max:
            p.append(i)
    return max, p


def get_min(lists):
    min = 1000
    p = []
    for i in range(0, len(lists)):
        if lists[i] <= min:
            min = lists[i]
    for i in range(0, len(lists)):
        if lists[i] == min:
            p.append(i)
    return min, p


def get_sum(lists):
    sum = 0
    for i in range(0, len(lists)):
        sum += lists[i]
    return sum


def get_normaldata(data):
    min, p_min = get_min(data)
    max, p_max = get_max(data)
    lists = []

    for d in data:
        if max != min:
            x = (d - min) / (max - min)
            lists.append(x)
        else:
            lists.append(1)
    return lists


def Tarantula(anf, anp, akf, akp):
    try:
        return (akf / akf + akp) / ((akf / (akf + akp)) + (akp / (akp + anp)))  # Tarantula 16->27 ?????
    except:
        return 0
def Dice(anf, anp, akf, akp):
    return 2*akf/(akf+akp+anf)
def Hamann(anf, anp, akf, akp):
    return (akf+anp-akp+anf)/(anf+anp+akf+akp)
def Hamming(anf, anp, akf, akp):
    return akf+anp
def Wong1(anf, anp, akf, akp):
    return akf

def OP2(anf, anp, akf, akp):
    return akf - akp / (akp + anp + 1)  # OP2 提升5 30->35


def GP13(anf, anp, akf, akp):
    if akp + akf == 0:
        return 0
    else:
        return akf * (1 + (1 / ((2 * akp) + akf)))

def Dstar(anf, anp, akf, akp):
    return (akf ** 3 / (anf + akp))

def Ochiai(anf, anp, akf, akp):
    if akf != 0 and (((akf + anf) * (akf + akp)) ** 0.5) != 0:
        return akf / (((akf + anf) * (akf + akp)) ** 0.5)  # Ochiai 29->33
    else:
        return 0


def Jaccard(anf, anp, akf, akp):
    # if anf + anp == 0 or anf + akp == 0:
    #     return 999
    # elif akf + akp == 0 or akf + anp == 0:
    #     return 0
    # else:
    #     return (akf * anp) / (((akf + akp) * (anf + anp) * (akf + anp) * (anf + akp)) ** 0.5)
    sus = 0
    try:
        sus = akf / (akf + anf + anp)
        return sus
    except:
        return sus

def method_calculate(anf, anp, akf, akp, name):
    if name == 'Tarantula':
        return Tarantula(anf, anp, akf, akp)
    if name == 'OP2':
        return OP2(anf, anp, akf, akp)
    if name == 'GP13':
        return GP13(anf, anp, akf, akp)
    if name == 'Ochiai':
        return Ochiai(anf, anp, akf, akp)
    if name == 'Jaccard':
        return Jaccard(anf, anp, akf, akp)
    if name == 'Dstar':
        return Dstar(anf, anp, akf, akp)
    if name == 'Dice':
        return Dice(anf, anp, akf, akp)
    if name == 'Hamann':
        return Hamann(anf, anp, akf, akp)
    if name == 'Wong1':
        return Wong1(anf, anp, akf, akp)
    if name == 'Hamming':
        return Dstar(anf, anp, akf, akp)



if __name__ == '__main__':

    cal_names = ['Dstar']
    dataset = ['tcas']


    for data_value in dataset:

        with open(f'Data/{data_value}.json', 'r') as rf:
            datas = json.load(rf)
        num_flag = 0
        for calcu_name in cal_names:
            data_num = 0
            mbfl_num = 0
            prmbfl_num = 0

            for data in datas:

                num_flag += 1

                ans = data['ans']
                # print(ans)
                data_name = data['proj']
                method = data['methods']
                lines = data['lines']
                mutation = data['mutation']
                ftest = data['ftest']
                rtest = data['rtest']

                len_method = len(data['methods'])
                len_lines = len(data['lines'])
                len_mutation = len(data['mutation'])
                len_ftest = len(data['ftest'])
                len_rtest = len(data['rtest'])
                print(len_method, len_lines, len_mutation, len_rtest, len_ftest)
                len_total = len_lines + len_rtest + len_ftest + len_mutation + len_method
                print("GET %s MESSAGE FINISHED!" % data_name, end='\n\n')

                method2method = {}
                method2lines = data['edge2']
                mutation2lines = data['edge12']
                lines2rtest = data['edge10']
                lines2ftest = data['edge']
                mutation2rtest = data['edge13']
                mutation2ftest = data['edge14']
                print("GET EDGES FINISHED!", end='\n\n')
                try:
                    # 获得关联矩阵信息
                    print(f'''--------------{data_name}-------------''')
                    # matrix = []
                    f = open(f'Killed_Matrix/{data_value}/{data_name}_matrix.pkl', 'rb')
                    matrix = pickle.load(f)
                    # lines = f.readlines()
                    # for line in lines:
                    #     line = line.replace(' \n', '')
                    #     line = line.split(' ')
                    #     matrix.append(line)
                    # for mmm in matrix:
                    #     for mm in mmm:
                    #         print(mm,end=' ')
                    #     print('')
                    print(matrix)

                    # 获得方法对应的语句信息
                    with open(f'PR_Value/{data_value}/{data_name}_PR.txt', 'r') as pr_f:
                        lines = pr_f.readlines()
                    lists = lines[0]
                    lists = lists.replace('\n', '')
                    lists = lists.split(' ')
                    method_len = eval(lists[0])
                    statement_len = eval(lists[1])
                    mutation_len = eval(lists[2])
                    rtest_len = eval(lists[3])
                    ftest_len = eval(lists[4])
                    totle_len = method_len + statement_len + mutation_len + rtest_len + ftest_len

                    # print(lists)
                    # print(PR)
                except:
                    print('------------------------------errrrrr')
                    continue

                # 得到方法对应的变异体信息（每个方法对应一个变异体信息列表）

                # 方法对应的 语句信息：
                method2statements = []
                for x in range(0, method_len):
                    method2statement = []
                    for y in range(method_len, method_len + statement_len):
                        if matrix[x][y] == 1:
                            method2statement.append(y - method_len)
                    method2statements.append(method2statement)
                # print('method2statements', method2statements)

                # 语句对应的 变异体信息：
                statement2mutations = []
                for x in range(method_len, method_len + statement_len):
                    statement2mutation = []
                    for y in range(method_len + statement_len, method_len + statement_len + mutation_len):
                        if matrix[x][y] == 1:
                            statement2mutation.append(y - method_len - statement_len)
                    statement2mutations.append(statement2mutation)
                # print('statement2mutations', statement2mutations)

                # 变异体杀死的 正确测试用例：
                mutation2rtests = []
                for x in range(method_len + statement_len, method_len + statement_len + mutation_len):
                    mutation2rtest = []
                    for y in range(method_len + statement_len + mutation_len,
                                   method_len + statement_len + mutation_len + rtest_len):
                        if matrix[x][y] == 1:
                            mutation2rtest.append(y - method_len - statement_len - mutation_len)
                    mutation2rtests.append(mutation2rtest)
                # 变异体杀死的 错误的测试用例：
                mutation2ftests = []
                for x in range(method_len + statement_len, method_len + statement_len + mutation_len):
                    mutation2ftest = []
                    for y in range(method_len + statement_len + mutation_len + rtest_len,
                                   method_len + statement_len + mutation_len + rtest_len + ftest_len):
                        # print(x,y)
                        try:

                            if matrix[x][y] == 1:
                                mutation2ftest.append(y - method_len - statement_len - mutation_len - rtest_len)
                        except:
                            # print(method_len + statement_len + mutation_len + rtest_len + ftest_len)
                            break
                    mutation2ftests.append(mutation2ftest)

                # 方法对应的 变异体：
                method2mutations = []
                sus_ms = []
                for x in range(0, method_len):
                    sus_m = 0
                    method2mutation = []
                    method2statement = method2statements[x]
                    # print(method2statement)
                    for y in method2statement:
                        # print(y)
                        p_statement = int(y)
                        # print(statement2mutations[p_statement])
                        for p in statement2mutations[p_statement]:
                            if p not in method2mutation:
                                method2mutation.append(p)

                    # 已得到该方法对应的变异体信息
                    # 接下来要对该方法的所有变异体，依次进行 四参数 的计算
                    # 首先是变异体的杀死信息

                    method2rtest = []
                    method2ftest = []

                    for m2m in method2mutation:
                        p_mutation = int(m2m)
                        # print(mutation2rtests[p_mutation])
                        for p in mutation2rtests[p_mutation]:
                            if p not in method2rtest:
                                method2rtest.append(p)
                        for p in mutation2ftests[p_mutation]:
                            if p not in method2ftest:
                                method2ftest.append(p)
                        akf = len(method2ftest)
                        anf = ftest_len - akf
                        akp = len(method2rtest)
                        anp = rtest_len - akp
                        sus = method_calculate(anf, anp, akf, akp, calcu_name)
                        if sus > sus_m:
                            sus_m = sus
                    sus_ms.append(sus_m)
                    # method2statement.extend(statement2mutations[p_statement])
                    method2mutations.append(method2mutation)
                # print('method2mutations:', method2mutations)
                # break

                maxsus_method, maxsus_p = get_max(sus_ms)

                print("怀疑度最大为方法：", maxsus_p, "  ", maxsus_method)
                # print(PR[:method_len])
                # print(method_len)
                print(ans)
                data_name2 = data_name + calcu_name

                filepath = f'{data_value}_SUS\MBFL\{data_name2}_sus.txt'
                create_folder_if_not_exists(filepath)
                with open(filepath, 'w') as anf:
                    anf.write(str(sus_ms))


                # print(type(d))
                with open(f'PR_Value/{data_value}/{data_name}_PR.txt', 'r') as pr_f:
                    lines = pr_f.readlines()
                lists = lines[0]
                lists = lists.replace('\n', '')
                lists = lists.split(' ')
                method_len = eval(lists[0])
                statement_len = eval(lists[1])
                mutation_len = eval(lists[2])
                rtest_len = eval(lists[3])
                ftest_len = eval(lists[4])
                totle_len = method_len + statement_len + mutation_len + rtest_len + ftest_len
                Pr = lines[1]
                Pr = Pr.replace(" \n", '')
                Pr = Pr.split(' ')
                PR = []
                for pr in Pr:
                    PR.append(float(pr))

                pr_list = (PR[:method_len])

                max_PR, PR_p = get_max(pr_list)
                sus_s2 = []
                pr_sum = get_sum(pr_list)
                for x in range(0, method_len):
                    # print(f'a:{a},d:{d},method:{calcu_name},{data_name}')
                    #
                    # print('PR:',pr_list[x],'   pr_sum:',pr_sum)
                    if pr_sum == 0:
                        sus = sus_ms[x]
                    else:
                        sus = (1 + pr_list[x] / pr_sum) * sus_ms[x]
                    # if a == 0.8 and d == 0.8:
                    # print(PR)
                    # print(pr_list)
                    # print('sus_mbfl:',sus_ms[x])
                    # print('sus_PR:',sus)

                    # time.sleep(10000)
                    # else:
                    #     continue
                    sus_s2.append(sus)
                pr_maxsus, pr_p = get_max(sus_s2)

                print("PR方法怀疑度最大为方法：", pr_p, "  ", pr_maxsus)
                # print(sus_s,sus_s2)

                ans = data['ans']
                # print(data_name, "错误方法为：", ans)
                data_num += 1


                filepath = f'{data_value}_SUS\MBFL_G\{data_name2}.txt'
                create_folder_if_not_exists(filepath)
                with open(filepath, 'w') as anf:

                    anf.write(str(sus_s2))


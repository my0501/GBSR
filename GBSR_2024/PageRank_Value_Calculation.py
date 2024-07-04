import json
import os
import pickle

import numpy as np

np.set_printoptions(suppress=True)
def create_folder_if_not_exists(file_path):
    # 获取文件夹路径
    folder_path = os.path.dirname(file_path)

    # 检查文件夹是否存在，如果不存在则创建
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"文件夹已创建: {folder_path}")
    else:
        print(f"文件夹已存在: {folder_path}")

def getPR(A, x_0, min_delta):
    count = 0
    while (True):
        np.set_printoptions(precision=6)
        y = np.dot(A, x_0)
        x_1 = np.dot(1 / max(y), y)
        e = max(np.abs(x_1 - x_0))
        if (e < min_delta):
            return x_0

        x_0 = x_1
        count = count + 1
        # print(e)


def get_PR(file_path):
    dic = []

    # with open(file_path, 'r') as f:
    #     data = f.readlines()
    #
    #     for d in data:
    #         di = []
    #         d1 = list(d.split(' '))
    #         d1.remove('\n')
    #         dic.append(d1)


    with open(file_path, 'rb') as f:
        dic = pickle.load(f)
        # print(data)

    len_total = 0

    for i in dic:
        len_total = len(i)
        # print(len(i), i)
    matrix = np.array(dic)
    matrix = matrix.astype(float)
    # print(matrix)
    M = matrix
    x_0 = np.ones((len_total,))
    # 计算有向图的一般转移矩阵A
    d = 0.85
    E = np.ones((len_total, len_total))
    A = np.dot(d, M) + np.dot((1 - d) / len_total, E)
    min_delta = 0.0000001  # 精度
    PR = getPR(A, x_0, min_delta)
    return PR


if __name__ == '__main__':
    with open('../Data/Lang.json', 'r') as rf:
        datas = json.load(rf)
        print("GET JSON FILE FINISHED!", end='\n\n')
    flag = 0
    for data in datas:
        flag += 1
        # if flag < 18:
        #     continue
        data_name = data['proj']
        method = data['methods']
        lines = data['lines']
        mutation = data['mutation']
        ftest = data['ftest']
        rtest = data['rtest']
        print(data_name)
        len_method = len(data['methods'])
        len_lines = len(data['lines'])
        len_mutation = len(data['mutation'])
        len_ftest = len(data['ftest'])
        len_rtest = len(data['rtest'])
        pr_s = ''
        print(len_method, len_lines, len_mutation, len_rtest, len_ftest)
        pr_s += (str(len_method) + " " + str(len_lines) + " " + str(len_mutation) + " " + str(len_rtest) + " " + str(
            len_ftest) + '\n')
        filepath = f'F_FIN_matrix\Lang\{data_name}_matrix.pkl'
        try:
            FIN_matrix_PR = get_PR(filepath)
        except:
            continue
        filepath = f'P_FIN_matrix\Lang\{data_name}_matrix.pkl'
        try:
            FIN_matrix_PR2 = get_PR(filepath)
        except:
            continue
        # print(FIN_matrix_PR.round(6))
        PR_value = []
        for p in range(len_method + len_lines + len_mutation):
            PR_value.append(float(FIN_matrix_PR[p] - 1.0 * FIN_matrix_PR2[p]))
            # pr_s += (str(FIN_matrix_PR[p] - 1.0 * FIN_matrix_PR2[p]) + ' ')
        # for pr in FIN_matrix_PR.round(6):
        #     pr_s += (str(pr) + ' ')
        # print(len_method + len_lines + len_mutation)
        # print(len(PR_value))
        original_array = np.array(PR_value)
        normalized_array = (original_array - np.min(original_array)) / (np.max(original_array) - np.min(original_array))
        # print(len(normalized_array))

        for nor in normalized_array:
            pr_s += str(nor) + ' '
        pr_s += '\n'

        ans_path = f'PR_Value\Lang\{data_name}_PR.txt'
        create_folder_if_not_exists(ans_path)
        with open(ans_path, 'w') as anf:
            anf.write(pr_s)

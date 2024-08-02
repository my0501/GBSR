import json
import os

import numpy as np
import pickle

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


def get_matrix(len1, len2, edges, flag=1, change=0):
    matrix = np.zeros((len1, len2))
    for edge in edges:
        dot1 = int(edge[0])
        dot2 = int(edge[1])
        # print(dot1, dot2)
        matrix[dot1][dot2] = 1
    if change == 0:
        each_j = []
        for j in range(len1):
            sum = 0
            for i in range(len2):
                sum += matrix[j][i]
            each_j.append(sum)
        for j in range(len1):
            for i in range(len2):
                if each_j[j] != 0:
                    matrix[j][i] = flag * matrix[j][i] / each_j[j]
        return matrix
    else:
        each_j = []
        for j in range(len2):
            sum = 0
            for i in range(len1):
                sum += matrix[i][j]
            each_j.append(sum)
        for j in range(len2):
            for i in range(len1):
                if each_j[j] != 0:
                    matrix[i][j] = flag * matrix[i][j] / each_j[j]
        return matrix


def integration(M1, M2, M3, M4, M4_1, M5, M5_1, L1, L2, L3, L4, L5):
    # M1 ~ M5 : method-method ; method - lines ; mutation - lines ; lines - r/f tests ; mutation - r/f tests ;
    # L1 ~ L5 : method ; lines ; mutations ; r tests; t tests

    len_total = L1 + L2 + L3
    P_len = len_total + L4
    F_len = len_total + L5
    # print(len_total)

    matrix_P = np.zeros((P_len, P_len))
    matrix_F = np.zeros((F_len, F_len))
    matrix = np.zeros((len_total, len_total))

    for i in range(L1):
        for j in range(L1):
            node1 = i
            node2 = j
            # matrix[node1][node2] = M1[i][j]
            matrix_P[node1][node2] = M1[i][j]
            matrix_F[node1][node2] = M1[i][j]

    for i in range(L1):
        for j in range(L2):
            node1 = i
            node2 = j + L1
            # matrix[node1][node2] = M2[i][j]
            # matrix[node2][node1] = M2[i][j]

            matrix_P[node1][node2] = M2[i][j]
            matrix_P[node2][node1] = M2[i][j]

            matrix_F[node1][node2] = M2[i][j]
            matrix_F[node2][node1] = M2[i][j]

    for i in range(L3):
        for j in range(L2):
            node1 = i + L1 + L2
            node2 = j + L1
            # matrix[node1][node2] = M3[i][j]
            # matrix[node2][node1] = M3[i][j]

            matrix_P[node1][node2] = M3[i][j]
            matrix_P[node2][node1] = M3[i][j]

            matrix_F[node1][node2] = M3[i][j]
            matrix_F[node2][node1] = M3[i][j]
    # print(L2, L4)
    for i in range(L2):
        for j in range(L4):
            node1 = i + L1
            node2 = j + L1 + L2 + L3
            # print(node1, node2)
            # print(i , j )
            # matrix[node1][node2] = M4[i][j]
            # matrix[node2][node1] = M4[i][j]

            matrix_P[node1][node2] = M4[i][j]
            matrix_P[node2][node1] = M4[i][j]

    for i in range(L3):
        for j in range(L4):
            node1 = i + L1 + L2
            node2 = j + L1 + L2 + L3
            # matrix[node1][node2] = M5[i][j]
            # matrix[node2][node1] = M5[i][j]

            matrix_P[node1][node2] = M5[i][j]
            matrix_P[node2][node1] = M5[i][j]

    for i in range(L2):
        for j in range(L5):
            node1 = i + L1
            node2 = j + L1 + L2 + L3
            # print(node1, node2)
            # print(i , j )
            # matrix[node1][node2] = M4_1[i][j]
            # matrix[node2][node1] = M4_1[i][j]

            matrix_F[node1][node2] = M4_1[i][j]
            matrix_F[node2][node1] = M4_1[i][j]

    for i in range(L3):
        for j in range(L5):
            node1 = i + L1 + L2
            node2 = j + L1 + L2 + L3
            # matrix[node1][node2] = M5_1[i][j]
            # matrix[node2][node1] = M5_1[i][j]

            matrix_F[node1][node2] = M5_1[i][j]
            matrix_F[node2][node1] = M5_1[i][j]

    return matrix_P, matrix_F


def m2m_matrix(length, data):
    print(data)
    matrix = np.zeros((length, length))
    # for d in data:
    #     ll = len(d[1])
    #     # print(ll)
    #     if ll != 0:
    #         for j in d[1]:
    #             matrix[d[0]][j] = 1.0 / ll
    #             print(f'matrix[{d[0]}][{j}]', matrix[d[0]][j])
    # print(matrix)
    return matrix


if __name__ == '__main__':
    m2m_data = {}
    # with open('../Data/tcas_M2M.txt', 'r') as M_f:
    #     mf = M_f.readlines()
    # for m2m in mf:
    #     name = m2m.split(' * ')[0]
    #     M2M = m2m.split(' * ')[1]
    #     M2M = eval(M2M)
    #
    #     m2m_data[name] = M2M

    with open('Data/tcas.json', 'r') as rf:
        datas = json.load(rf)
        print("GET JSON FILE FINISHED!", end='\n\n')
    num_flag = 0
    for data in datas:

        num_flag += 1
        # if num_flag != 4:
        #     continue

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

        matrix = np.zeros((len_total, len_total))
        # print(len_total)
        # print(matrix.shape)

        # try:
        #     this_m2m_data = m2m_data[data_name]
        # except:
        #     print('err----', num_flag)
        #     continue

        # methed-method 矩阵 建立
        method2method_matrix = m2m_matrix(len_method, 0)
        # --------------------------
        # --------------------------

        # method-lines 矩阵 建立
        method2lines_matrix = get_matrix(len_method, len_lines, method2lines)

        # print(method2lines_matrix)

        # mutation-lines 矩阵 建立
        mutation2lines_matrix = get_matrix(len_mutation, len_lines, mutation2lines, change=1)
        # print(mutation2lines_matrix)

        # lines-rtest 矩阵 建立
        lines2rtest_matrix = get_matrix(len_lines, len_rtest, lines2rtest, -1)
        # print(lines2rtest_matrix)

        # line-ftest 矩阵 建立
        lines2ftest_matrix = get_matrix(len_lines, len_ftest, lines2ftest)
        # print(lines2ftest_matrix)

        # mutation-rtest 矩阵 建立
        mutation2rtest_matrix = get_matrix(len_mutation, len_rtest, mutation2rtest, -1)
        # print(mutation2rtest_matrix)

        # mutation-ftest 矩阵 建立
        mutation2ftest_matrix = get_matrix(len_mutation, len_ftest, mutation2ftest)
        # print(mutation2ftest_matrix)

        print('------rrrrrrrr--------')
        P_matrix, F_matrix = integration(method2method_matrix, method2lines_matrix, mutation2lines_matrix,
                                         lines2rtest_matrix, lines2ftest_matrix, mutation2rtest_matrix,
                                         mutation2ftest_matrix, len_method, len_lines, len_mutation, len_rtest,
                                         len_ftest)
        print('------ffffffff--------')

        # f_matrix = integration(method2method_matrix,method2lines_matrix,mutation2lines_matrix, lines2ftest_matrix, mutation2ftest_matrix, len_method, len_lines,len_mutation, len_ftest)

        P_file_path = f'''F_FIN_matrix\\tcas\{data_name}_matrix.pkl'''
        F_file_path = f'''P_FIN_matrix\\tcas\{data_name}_matrix.pkl'''
        create_folder_if_not_exists(P_file_path)
        create_folder_if_not_exists(F_file_path)

        # print(r_matrix)

        # r_matrix.to_pickle(path=file_path)
        # print(f_matrix)
        # str_rmatrix = ''
        # for i in r_matrix.round(6):
        #     for j in i:
        #         str_rmatrix = str_rmatrix + str(j) + ' '
        #     str_rmatrix = str_rmatrix + '\n'
        with open(P_file_path, 'wb') as wf:
            # wf.write(str_rmatrix)
            pickle.dump(P_matrix, wf)
        with open(F_file_path, 'wb') as wf:
            # wf.write(str_rmatrix)
            pickle.dump(F_matrix, wf)
        print('---finished!-----')
        # str_fmatrix = ''
        # for i in f_matrix:
        #     for j in i:
        #               str_fmatrix = str_fmatrix + str(j) + ' '
        #     str_fmatrix = str_fmatrix + '\n'
        # with open(ffile_path, 'w') as wf:
        #     wf.write(str_fmatrix)
        #
        #

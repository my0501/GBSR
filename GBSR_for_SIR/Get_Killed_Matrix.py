import json
import os
import pickle

import numpy as np
def create_folder_if_not_exists(file_path):
    # 获取文件夹路径
    folder_path = os.path.dirname(file_path)

    # 检查文件夹是否存在，如果不存在则创建
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"文件夹已创建: {folder_path}")
    else:
        print(f"文件夹已存在: {folder_path}")

if __name__ == '__main__':

    with open('Data/tcas.json', 'r') as rf:
        datas = json.load(rf)
        print("GET JSON FILE FINISHED!", end='\n\n')
    num_flag = 0
    for data in datas:
        num_flag += 1
        # if num_flag != 1:
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
        print(len_method,len_lines,len_mutation,len_rtest,len_ftest)
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

        matrix = np.zeros((len_total,len_total))
        # print(len_total)
        # print(matrix.shape)

        for edge in method2lines:
            dot1 = int(edge[0])
            dot2 = int(edge[1])
            dot1 = dot1
            dot2 = dot2 + len_method
            # print(dot1,dot2)
            matrix[dot1][dot2] = 1
            matrix[dot2][dot1] = 1


        for edge in mutation2lines:
            dot1 = int(edge[0])
            dot2 = int(edge[1])
            dot1 = dot1 + len_method + len_lines
            dot2 = dot2 + len_method
            # print(dot1,dot2)
            matrix[dot1][dot2] = 1
            matrix[dot2][dot1] = 1


        # print(len(lines2rtest))
        for edge in lines2rtest:
            dot1 = int(edge[0])
            dot2 = int(edge[1])
            dot1 = dot1 + len_method
            dot2 = dot2 + len_method + len_lines + len_mutation
            # print(dot1,dot2)
            matrix[dot1][dot2] = 1
            matrix[dot2][dot1] = 1
        # print("-------------------------")
        for edge in lines2ftest:
            dot1 = int(edge[0])
            dot2 = int(edge[1])
            # print(dot1, dot2)
            dot1 = dot1 + len_method
            dot2 = dot2 + len_method + len_lines + len_mutation + len_rtest
            # print(dot1, dot2)
            matrix[dot1][dot2] = 1
            matrix[dot2][dot1] = 1

        for edge in mutation2rtest:
            dot1 = int(edge[0])
            dot2 = int(edge[1])
            dot1 = dot1 + len_method + len_lines
            dot2 = dot2 + len_method + len_lines + len_mutation
            # print(dot1, dot2)
            matrix[dot1][dot2] = 1
            matrix[dot2][dot1] = 1

        for edge in mutation2ftest:
            dot1 = int(edge[0])
            dot2 = int(edge[1])
            dot1 = dot1 + len_method + len_lines
            dot2 = dot2 + len_method + len_lines + len_mutation + len_rtest
            # print(dot1, dot2)
            matrix[dot1][dot2] = 1
            matrix[dot2][dot1] = 1


        
        matrix = matrix.astype(int)
        print(matrix)
        file_path = f'''Killed_Matrix\\tcas\{data_name}_matrix.pkl'''
        create_folder_if_not_exists(file_path)
        with open(file_path, 'wb') as wf:
            pickle.dump(matrix,wf)

import pickle
import json

# Step 1: Load the pickle file
with open('tcas.pkl', 'rb') as pkl_file:
    data = pickle.load(pkl_file)

# Step 2: Convert the data to JSON and save it
with open('tcas.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=1)  # 使用 indent 参数美化输出f
print(len(data))
for d in data:
    if d['proj'] == 'tcas8':
        print("Proj_name:", d['proj'])
        print("Methhod_id:", d['methods'])
        print("method, statement:", d['edge2'])
        print("statement, rtest:", d['edge'])
        print("statement, ftest:", d['edge10'])
        print("mutation, statement:", d['edge12'])
        print("mutation, rtest:", d['edge13'])
        print("mutation, ftest:", d['edge14'])
        print(d['rtest'])
        print(d['ftest'])
        print(len(d['rtest']), len(d['ftest']), len(d['mutation']), len(d['lines']))
        # for dd in d:
        # print(dd)
import numpy as np

with open('../F_FIN_matrix/tcas/tcas8_matrix.pkl', 'rb') as f2:
    data2 = pickle.load(f2)

with open('../P_FIN_matrix/tcas/tcas8_matrix.pkl', 'rb') as f2:
    data3 = pickle.load(f2)

A = np.array(data2)

# 将矩阵中所有非零元素转换为1，保持0不变
A_binary = (A != 0).astype(int)
B = np.array(data3)

# 将矩阵中所有非零元素转换为1，保持0不变
B_binary = (B != 0).astype(int)


def pagerank(M, num_iterations=100, d=0.85):
    """ 计算 PageRank 值
    参数:
        M : numpy array, 表示网页链接的方阵（邻接矩阵）
        num_iterations : 迭代次数
        d : 阻尼因子, 通常设为 0.85
    返回:
        numpy array, 各节点的 PageRank 值
    """
    N = M.shape[0]
    v = np.random.rand(N, 1)
    v = v / np.linalg.norm(v, 1)
    M_hat = (d * M + (1 - d) / N)

    for i in range(num_iterations):
        v = M_hat @ v

    return v


# 示例矩阵
M = np.array(A_binary)
# print(M)
# 转换成随机转移概率矩阵
N = M.shape[0]
M = M / np.sum(M, axis=0, keepdims=True)

# 计算 PageRank 值
pagerank_values = pagerank(M)
print("PageRank Values:\n", pagerank_values)

# # print(data2)
F_list = [[0.01490847],
          [0.00536369],
          [0.00242426],
          [0.00242426],
          [0.00637739],
          [0.00646261],
          [0.00242426],
          [0.00242426], ]
P_list = [[0.01658571],
          [0.00543695],
          [0.00247339],
          [0.00247339],
          [0.00604352],
          [0.00604352],
          [0.00247339],
          [0.00247339]]
for i in range(len(F_list)):
    print(F_list[i][0] - P_list[i][0])
with open('../P_FIN_matrix/tcas/tcas8_matrix.pkl', 'rb') as f2:
    data3 = pickle.load(f2)
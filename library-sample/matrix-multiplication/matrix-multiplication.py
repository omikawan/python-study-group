"""
◆forループの速度検証用スクリプト
1. for文を利用した行列積計算スクリプト
2. numpy.dotを利用した行列積計算スクリプト
"""

import numpy as np
from numpy.random import rand
import timeit
import time
# 処理時間測定 下記を利用
# https://qastack.jp/programming/5478351/python-time-measure-function
def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('■実行時間" {:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))

        return ret
    return wrap

# 1. for文を利用した行列積計算スクリプト
@timing
def sample_for(a,b,c):
	for i in range(N):
		for j in range(N):
			for k in range(N):
				c[i][j] += a[i][k] * b[k][j]
	return c

# 2. numpy.dotを利用した行列積計算スクリプト
@timing
def sample_dot(a, b):
	return np.dot(a, b)


if __name__ == "__main__":

	N = 200
	a = np.array(np.random.randint(1, 10,(N, N)))
	b = np.array(np.random.randint(1, 10,(N, N)))
	c = np.array([[0] * N for _ in range(N)])

	print("■sample_for")
	print(sample_for(a,b,c))
	print("")
	print("■sample_dot")
	print(sample_dot(a,b))
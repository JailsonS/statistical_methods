import math, random
from collections import Counter
from matplotlib import pyplot as plt


def vector_add(v, w):
    '''soma elementos correspondentes'''
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    '''subtrai elementos correspondentes'''
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    '''soma todos os vetores'''
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

def scalar_multiply(n, v):
    '''n é número, v é vetor'''
    return [n * v_i for v_i in v]

def vector_mean(vectors):
    '''calcula a média dos vetores'''
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    ''' soma dos produtos '''
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    '''v_1 * v_1 + ... + v_n * v_n'''
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    '''(v_1-w_1) ** 2 + ... + (v_n-w_n) ** 2'''
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return magnitude(vector_subtract(v, w))

def mean(x):
    return sum(x) / len(x)

def median(v):
    ''' encontra o valor mais ao meio de v '''
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        '''se for ímpar, retorna o valor do meio'''
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

def data_range(x):
    '''amplitude, 0 é igual a dados concentrados'''
    return max(x) - min(x)

def de_mean(x):
    '''desloca x ao subtrair sua média'''
    x_mean = mean(x)
    return [x_i - x_mean for x_i in x]

def variance(x):
    '''presume que x tem ao menos 2 elementos'''
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def covariance(x, y):
    '''
    covariância positiva grande significa que x tende a ser grande quando y é grande e pequeno quando y é pequeno
    covariância negativa grande significa que x tende a ser pequeno quando y é grande vice-versa
    '''
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        '''se não houver amplitude, a correlação é 0'''
        return 0;

def random_kid():
    return random.choice(['boy', 'girl'])

def scatter_graph(v, w, title, ylabel, xlabel):
    plt.scatter(v, w)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()

'''
num_friends = [100, 49, 51, 40, 25, 60, 35, 48, 52, 49]
daily_minutes = [10, 4, 5, 4.2, 2.1, 6, 3.5, 4.8, 5.2, 4.9]

friends_count = Counter(num_friends)
outlier = num_friends.index(100) # index of outlier

num_firends_good = [x for i, x in enumerate(num_friends)
                        if i != outlier]

daily_minutes_good = [x for i, x in enumerate(daily_minutes)
                        if i != outlier]
'''

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)
for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == 'girl':
        older_girl += 1
    if older == 'girl' and younger == 'girl':
        both_girls += 1
    if older == 'girl' or younger == 'girl':
        either_girl += 1

print(both_girls / older_girl)
print(both_girls/ either_girl)
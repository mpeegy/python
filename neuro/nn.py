# encoding=utf8
import random

class NN:
    def __init__(self, threshold, size):
        """
        Установим начальные параметры.
        """
        self.threshold = threshold
        self.size = size
        self.init_weight()

    def init_weight(self):
        """
        Инициализируем матрицу весов случайными данными.
        """

        self.weights = [[random.randint(1, 10) for i in xrange(self.size)] for j in xrange(self.size)]

    def check(self, sample):
        """
        Считаем выходной сигнал для образа sample. Если vsum > self.threshold то можно предположить, что в sample есть образ чайки.
        """

        vsum = 0
        for i in xrange(self.size):
            for j in xrange(self.size):
                vsum += self.weights[i][j] * sample[i][j]

        if vsum > self.threshold:
            return True
        else:
            return False

    def teach(self, sample):
        """
        Обучение нейронной сети.
        """

        for i in xrange(self.size):
            for j in xrange(self.size):
                self.weights[i][j] += sample[i][j]

nn = NN(20, 6)


# Обучаем нейронную сеть.

tsample1 = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
nn.teach(tsample1)

tsample2 = [
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]
nn.teach(tsample2)

tsample3 = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
]
nn.teach(tsample3)

tsample4 = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
]
nn.teach(tsample4)

# Проверим что может нейронная сеть.

# Передадим образ чайки, который примерно похож на тот, про который знает персептрон. 
wsample1 = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

print u"чайка" if nn.check(wsample1) else u"НЛО"

# Передадим неизвестный образ. 
wsample2 = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

print u"чайка" if nn.check(wsample2) else u"НЛО"

# Передадим образ чайки, который примерно похож на тот, про который знает персептрон. 
wsample3 = [
    [0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

print u"чайка" if nn.check(wsample3) else u"НЛО"

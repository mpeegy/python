from numpy import exp, array, random, dot
 
class NeuralNetwork():
    def __init__(self):
        # Задаем порождающий элемент для генератора случайных чисел, чтобы он генерировал одинаковые числа при каждом запуске программы
        random.seed(1)
 
        # Мы моделируем единственный нейрон с тремя входящими связями и одним выходом. Мы задаем случайные веса в матрице размера 3 x 1, где значения весов варьируются от -1 до 1, а среднее значение равно 0.
        self.synaptic_weights = 2 * random.random((3, 1)) - 1
 
    # Функция сигмоиды, график которой имеет форму буквы S.
    # Мы используем эту функцию, чтобы нормализовать взвешенную сумму входных сигналов.
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))
 
    # Производная от функции сигмоиды. Это градиент ее кривой. Его значение указывает насколько нейронная сеть уверена в правильности существующего веса.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)
 
    # Мы тренируем нейронную сеть методом проб и ошибок, каждый раз корректируя вес синапсов.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            # Тренировочный набор передается нейронной сети (одному нейрону в нашем случае).
            output = self.think(training_set_inputs)
 
            # Вычисляем ошибку (разницу между желаемым выходом и выходом, предсказанным нейроном).
            error = training_set_outputs - output
 
            # Умножаем ошибку на входной сигнал и на градиент сигмоиды. В результате этого, те веса, в которых нейрон не уверен, будут откорректированы сильнее. Входные сигналы, которые равны нулю, не приводят к изменению веса. 
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))
 
            # Корректируем веса.
            self.synaptic_weights += adjustment
 
    # Заставляем наш нейрон подумать.
    def think(self, inputs):
        # Пропускаем входящие данные через нейрон. 
        return self.__sigmoid(dot(inputs, self.synaptic_weights))
 
 
if __name__ == "__main__":
 
    #Инициализируем нейронную сеть, состоящую из одного нейрона.
    neural_network = NeuralNetwork()
 
    print ("Random starting synaptic weights: ")
    print (neural_network.synaptic_weights)
 
    # Тренировочный набор для обучения. У нас это 4 примера, состоящих из 3 входящих значений и 1 выходящего значения. 
    training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_set_outputs = array([[0, 1, 1, 0]]).T
 
    # Обучаем нейронную сеть на тренировочном наборе, повторяя процесс 10000 раз, каждый раз корректируя веса.
    neural_network.train(training_set_inputs, training_set_outputs, 10000)
 
    print ("New synaptic weights after training: ")
    print (neural_network.synaptic_weights)
 
    # Тестируем нейрон на новом примере.
    print ("Considering new situation [1, 0, 0] -> ?: ")
    print (neural_network.think(array([1, 0, 0])))

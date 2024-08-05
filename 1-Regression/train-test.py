import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.title('Dados Originais')
plt.scatter(x, y)
plt.show()

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

plt.title('Training Data')
plt.scatter(train_x, train_y)
plt.show()

plt.title('Testing Data')
plt.scatter(test_x, test_y)
plt.show()

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 5))

myline = numpy.linspace(0, 6, 100)

plt.title('Training Line Data')
plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

r2_train = r2_score(train_y, mymodel(train_x))

print('r2 train', r2_train)

r2_test = r2_score(test_y, mymodel(test_x))

print('r2 test', r2_test)

print('How much money will a buying customer spend, if she or he stays in the shop for 5 minutes?', mymodel(5))

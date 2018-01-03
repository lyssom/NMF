import numpy
import matplotlib.pyplot as plt


a = numpy.array(['movie1','movie2','movie3','movie4'])
b = numpy.array([5,3,0,1])
c = numpy.array([4,0,0,1])
d = numpy.array([1,1,0,5])
e = numpy.array([1,0,0,4])
f = numpy.array([0,1,5,4])
b1 = numpy.array([5.009498,2.89408548,0,0.99737194])
c1 = numpy.array([3.95179612,0,0,0.99603612])
d1 = numpy.array([1.09158713,0.76276788,0,4.96216115])
e1 = numpy.array([0.95403406,0,0,3.97222875])
f1 = numpy.array([0,1.31145877,4.88605227,4.03794756])
b2 = numpy.array([5.009498,2.89408548,5.20753816,0.99737194])
c2 = numpy.array([3.95179612,2.28885757,4.26450394,0.99603612])
d2 = numpy.array([1.09158713,0.76276788,4.68305239,4.96216115])
e2 = numpy.array([0.95403406,0.65649527,3.82024358,3.97222875])
f2 = numpy.array([2.09552606,1.31145877,4.88605227,4.03794756])






# plt.scatter(b,a,c='b')
# plt.scatter(c,a,c='b')
# plt.scatter(d,a,c='b')
# plt.scatter(e,a,c='b')
# plt.scatter(f,a,c='b')
# plt.scatter(b1,a,c='r')
# plt.scatter(c1,a,c='r')
# plt.scatter(d1,a,c='r')
# plt.scatter(e1,a,c='r')
# plt.scatter(f1,a,c='r')
plt.scatter(b2,a,c='r')
plt.scatter(c2,a,c='r')
plt.scatter(d2,a,c='r')
plt.scatter(e2,a,c='r')
plt.scatter(f2,a,c='r')
plt.show()
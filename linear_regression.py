
import numpy as np
import csv

def compute_cost(theta, X, y):
	m = X.shape[0]
	h = X * theta
	return np.sum(np.square((h - y))) / (2 * m)

def linear_regression(theta, X, y, alpha):
	# reduce theta by alpha, and distance
	# h = X * theta
	m = X.shape[0]
	# hyp_update = (h - y).transpose() * X
	# print "hyp update", hyp_update
	# delta = (alpha / m) * np.sum(hyp_update)
	# return theta - delta

	J = (X * theta) - y # not cost function, partial
	theta[0,0] = theta[0,0] - ((alpha/m) * np.sum(J) )
	theta[1:,0] = theta[1:,0] - ((alpha/m)  * np.sum( X[:,1:].transpose() * J) )

	return theta

def gradient_decent(theta, X, y, alpha, iter):
	new_theta = theta
	for i in range(iter):
		new_theta = linear_regression(new_theta, X, y, alpha)
		# print
		# print "theta", new_theta
		# print "cost", compute_cost(new_theta, X, y)

	print
	print "End", new_theta
	print "end cost", compute_cost(new_theta, X, y)


def parse_data(file):
	# take in csv file then return matrix 
	arr = []
	with open(file, 'rb') as csvfile:
		file = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in file:
			# print row[0].split(',')
			arr.append(row[0].split(','))

	return np.matrix(arr, dtype=float)

# def main():
X = parse_data('x_data.txt')
y = parse_data('y_data.txt')
# X = parse_data('test_x.txt')
# y = parse_data('test_y.txt')


theta = np.matrix([
	[0],
	[0]
	], dtype=float)
alpha = .01
iterations = 50000
m = X.shape[0]

'''
    J =  (X*theta) - y
    theta(1) = theta(1) - alpha * sum(J) / m
    theta(2:end,:) = theta(2:end,:) - (alpha/m) * (sum(X(:,2:end)' * J)) '''




# print theta 
# X = np.matrix(X, dtype=float)
# y = np.matrix(y, dtype=float)
	
gradient_decent(theta, X, y, alpha, iterations)

# print linear_regression(theta, X, y, alpha)











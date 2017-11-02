
import numpy as np
import csv

def compute_cost(theta, X, y):
	m = X.shape[0]
	h = X * theta
	return np.sum(np.square((h - y))) / (2 * m)

def linear_regression(theta, X, y, alpha):
	# reduce theta by alpha, and distance
	new_theta = np.matrix(np.zeros(theta.shape))
	m = X.shape[0]
	J = (X * theta) - y # not cost function, partial
	new_theta[0,0] = theta[0,0] - ((alpha/(m)) * np.sum(J) )
	new_theta[1:,0] = theta[1:,0] - ((alpha/(m))  * np.sum( X[:,1:].transpose() * J) )
	return new_theta

def lr_gradient_decent(theta, X, y, alpha, iter):
	#linear regression gradient decent
	lowest_cost = compute_cost(theta, X, y)
	new_theta = theta
	for i in range(iter):
		new_theta = linear_regression(new_theta, X, y, alpha)
		print
		print "theta", new_theta
		new_cost =  compute_cost(new_theta, X, y)
		print "new cost", new_cost
		lowest_cost = new_cost if new_cost < lowest_cost else lowest_cost


	print
	print "End", new_theta
	print "end cost", compute_cost(new_theta, X, y)
	print "lowest cost", lowest_cost

def parse_data(file):
	# take in csv file then return matrix 
	arr = []
	with open(file, 'rb') as csvfile:
		file = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in file:
			# print row
			# print row[0].split(',')
			arr.append(row[0].split(','))

	return np.matrix(arr, dtype=float)

# def main():
# X = parse_data('x_data.txt')
# y = parse_data('y_data.txt')

X = parse_data('x_data_3.txt')
y = parse_data('y_data_3.txt')

theta = np.matrix(np.zeros((np.size(X,1),1), dtype=float)) #initialize Theta 0
# theta = np.matrix([
# 	[0],
# 	[0],
# 	[0]
# 	], dtype=float)
alpha = .01
iterations = 50

lr_gradient_decent(theta, X, y, alpha, iterations)

# print compute_cost(theta, X, y)
# print linear_regression(theta, X, y, alpha)











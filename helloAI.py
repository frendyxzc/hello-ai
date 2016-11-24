#!/usr/bin/python
import sys
import random

# speed of correction
correction = 0.01;

# init weights
weights = [0 for i in range(3)];
for weight in weights:
	weight = random.randint(-2, 2);


def forecast(data):
	sum = 0;
	for index in range(len(weights)):
		sum += weights[index] * data[index];

	if sum >= 0:
		return 1;
	else:
		return -1;


def train(data, expectation):
	guess = forecast(data);
	error = expectation - guess;
	
	for index in range(len(weights)):
		weights[index] += correction * error * data[index];
		

def trainPerceptron():
	for index in range(500):
		x = random.randint(-500, 500);
		y = random.randint(-500, 500);
		bias = 1;
		data = [x, y, bias];
		
		if x > 0:
			train(data, 1);
		else:
			train(data, -1);
			
	for index in range(len(weights)):
		print "weights[" + bytes(index) + "] = " + bytes(weights[index]);
	

if __name__=="__main__":
	trainPerceptron();
	
	data = [int(sys.argv[1]), int(sys.argv[2]), 1];
	print forecast(data);
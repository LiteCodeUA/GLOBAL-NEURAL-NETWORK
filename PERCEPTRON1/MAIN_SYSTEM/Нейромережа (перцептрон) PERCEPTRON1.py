import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[0,1,0],
                            [0,1,1],
                            [1,1,0],
                            [0,0,1]])
training_outputs = np.array([[0,0,1,0]]).T

np.random.speed(100)

synaptic_weights = 4 * np.random.random((3,1)) - 1
print("RIW:")
print("syn_weights")

#1  
for i in range(10000000000):
input_layer = training_inputs
outputs = sigmoid( np.dot(input_layer, synaptic_weights) )

err = training_outputs - outputs
adjustments = np.dot( input_layer.T, err * (outputs * (1 - outputs)) )

synaptic_weights += adjustments

print("weight after training:")
print("Loading...")
print("calculate...")

print("answer:")
print(outputs)

#training 1

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[1+1],
                            [1+2],
                            [2+1],
                            [2+2]])
training_outputs = np.array([[2,3,3,4]]).T

np.random.speed(100)

synaptic_weights = 4 * np.random.random((3,1)) - 1
print("RIW:")
print("syn_weights")

print("weight after training:")
print("Loading...")
print("calculate...")

print("answer:")
print(outputs)

#training 2

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[33-22],
                            [100-50],
                            [1-1],
                            [1000-7]])
training_outputs = np.array([[11,50,0,993]]).T

np.random.speed(100)

synaptic_weights = 4 * np.random.random((3,1)) - 1
print("RIW:")
print("syn_weights")

print("weight after training:")
print("Loading...")
print("calculate...")

print("answer:")
print(outputs)

#training 3

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[12*2],
                            [24/2],
                            [64/2],
                            [3*25],
                            [5*5]])
training_outputs = np.array([[24,12,32,75,25 ]]).T

np.random.speed(100)

synaptic_weights = 5 * np.random.random((3,1)) - 1
print("RIW:")
print("syn_weights")

print("weight after training:")
print("Loading...")
print("calculate...")

print("answer:")
print(outputs)

#training 4

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[90*2],
                            [5/2]])
training_outputs = np.array([[180,2.5 ]]).T

np.random.speed(100)

synaptic_weights = 2 * np.random.random((3,1)) - 1
print("RIW:")
print("syn_weights")

print("weight after training:")
print("Loading...")
print("calculate...")

print("answer:")
print(outputs)

#training 5

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[-2+2],
                            [-4-2],
                            [-4+2],
                            [25-30],
                            [10-15]])
training_outputs = np.array([[0,-6,-2,-5,-5 ]]).T

np.random.speed(100)

synaptic_weights = 10 * np.random.random((3,1)) - 1
print("RIW:")
print("syn_weights")

print("weight after training:")
print("Loading...")
print("calculate...")

print("answer:")
print(outputs)

#training 6

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[2*2],
                            [-4*2],
                            [1 - 1],
                            [1000-1000],
                            [157-123]])
training_outputs = np.array([[4,-8,0,0,34 ]]).T

np.random.speed(100)

synaptic_weights = 10 * np.random.random((3,1)) - 1
print("RIW:")
print("syn_weights")

print("weight after training:")
print("Loading...")
print("calculate...")

print("answer:")
print(outputs)

#training 7

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[і 1],
                            [i 10],
                            [i 100],
                            [i 1000],
                            [i 10000]])
training_outputs = np.array([[info 1,info 10,info 100,info 1000,info 10000 ]]).T

np.random.speed(100)

synaptic_weights = 10 * np.random.random((3,1)) - 1
print("RIW:")
print("syn_weights")

print("weight after training:")
print("Loading...")
print("calculate...")

print("answer:")
print(outputs)

#training 7

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[PLS 1],
                            [PLS 10],
                            [PLS 100],
                            [PLS 1000],
                            [PLS 10000]])
training_outputs = np.array([[info 11,info 1010,info 100100,info 10001000,info 1000010000 ]]).T

np.random.speed(100)

synaptic_weights = 5 * np.random.random((3,1)) - 1
print("RIW:")
print("syn_weights")

print("weight after training:")
print("Loading...")
print("calculate...")

print("answer:")
print(outputs)

#training 8

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[control 1/1],
                            [control 10/10],
                            [control 15/15/15],
                            [control 2/2/2/2],
                            [control 10/20/30]])
training_outputs = np.array([[c_result == 2/2,info c_result == 20/20,c_result == 30/30/30,c_result == 4/4/4/4,c_result == 20/40/60 ]]).T

np.random.speed(100)

synaptic_weights = 10 * np.random.random((3,1)) - 1
print("RIW:")
print("syn_weights")

print("weight after training:")
print("Loading...")
print("calculate...")

print("answer:")
print(outputs)

#training 9

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[replace 1],
                            [replace 10],
                            [replace 100],
                            [replace 1000],
                            [replace 10000]])
training_outputs = np.array([[info 10000,info 1000,info 100,info 10,info 1]]).T

np.random.speed(100)

synaptic_weights = 15 * np.random.random((3,1)) - 1
print("RIW:")
print("syn_weights")

print("weight after training:")
print("Loading...")
print("calculate...")

print("answer:")
print(outputs)

#training 10

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[W 1],
                            [W 10],
                            [W 100],
                            [W 1000],
                            [W 10000]])
training_outputs = np.array([[weight == w1,,weight == w10,,weight == w100,,weight == w1000,weight == w10000 ]]).T

np.random.speed(100)

synaptic_weights = 100 * np.random.random((3,1)) - 1
print("RIW:")
print("syn_weights")

print("weight after training:")
print("Loading...")
print("calculate...")

print("answer:")
print(outputs)











                            
                            

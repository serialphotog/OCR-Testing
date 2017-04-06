import argparse

from tf_neural_network import TFNeuralNetwork 

def main():
	# Handle command line arguments
	parser = argparse.ArgumentParser(description="Neural Network Tester")
	parser.add_argument("-v", action="store_true", dest="verbose", 
		help="Enables verbose output.")
	args = parser.parse_args()

	# Start the testing
	neural_network = TFNeuralNetwork([784, 200, 10], verbose=args.verbose)
	neural_network.train()

if __name__ == '__main__':
	main()

from numpy import *

def run():
    collected_data = get_from_text("coll_data.csv", delimiter = ',')
    
    # a hyperparameter
    learning_rate = 0.0001 #how fast should the model converge
    init_b = 0
    init_m = 0
    # for slope formula y = mx + b
    iteration_count = 1000
    
    print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(init_b, init_m, computed_error(init_b, init_m, collected_data)))

    [b, m] = gradient_descent_run(collected_data, init_b, init_m, learning_rate)

    print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(init_b, init_m, computed_error(init_b, init_m, collected_data)))
if __name__ == "__main__":
    run()


from numpy import *

def run():
    collected_data = get_from_text("coll_data.csv", delimiter = ',')
    
    # a hyperparameter
    learning_rate = 0.0001 #how fast should the model converge
    init_b = 0
    init_m = 0
    # for slope formula y = mx + b


if __name__ == "__main__":
    run()

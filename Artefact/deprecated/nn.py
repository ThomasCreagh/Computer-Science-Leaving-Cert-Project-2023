class NN:
    def __init__(self, input):
        self.input = input
        self.input_l = len(input)
        self.input_h = len(input[0])
        self.layers = list()
        # self.weights =

    def add_layer(self, layer):
        self.layers.append(layer)

    def forward_prop(self):
        pass

    def sigmoid():
        pass


"""
each layer has weights and biases
Fore each layer the input is multiplyed by weights and biases are added

https://www.youtube.com/watch?v=aircAruvnKk

layers =  [   [   [1,2],
                  [3,4]  ],
              [   [5,6],
                  [7,8]  ]   ]

layer = [   [1,2],
            [3,4]  ]

{all nodes between 0 and 1}

First layer input is the grid [00, 01, 10, 11, .., etc] (input layer)

2x Hidden layer 16 neurons (exparament?)

Last layer output is the amount of columns there are in the grid (output layer)
"""

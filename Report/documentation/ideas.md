# Report
- [+] website
- [+] Flowchart (diagrams.net)
- [ ] Conclusion and what i would do differently

# Artifact
- [+] Game
- [x] Copying Code = Reduced Marks

# Game
- [+] Rules
- [+] Change game and get stratagies
- [+] Algorithmic Game
- [+] Simple Game
- [ ] Detailed Test Case Table
- [ ] How to improve?
- [+] Comment
- [+] Abstract rules
    - You can slot from the top
    - The symbols stack on top of each other
    - Each person goes one after another
    - The game is over when a player gets 4 symbols in a row
- [+] Validation

# AI
- [x] Use ai?
- Framework?
    - Do i use a libarary such as tensorflow?
        - I would have to find a libarary that can store the models data (weights and biases)
    - Or do i make it from scratch using maths?
        - I can either use backpropagation or random propagation
        - If i made it from scratch i could show my csv file usage, by storing all the weights and biases values inside the csv file
        - rn im not sure exactly how backpropagation works, so i need to figure that out
        - random propagation would be so much slower than backpropagation but im just not sure if backpropagation works with the model I am making
        - Good links
            - [https://en.wikipedia.org/wiki/Evolutionary_algorithm]
            - [https://towardsdatascience.com/math-neural-network-from-scratch-in-python-d6da9f29ce65]
            - [https://developer.ibm.com/articles/neural-networks-from-scratch/]
            - [https://medium.com/swlh/neural-network-from-scratch-in-python-fcd6faef9f35]
            - [https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6]
            - [https://www.freecodecamp.org/news/building-a-neural-network-from-scratch/]
- Try to use a Genarational Neural Network
    - Input data:
        - The input of the data is matrix of the board that is ([black spaces], X's and O's)
        - The size of the data could vary based on the dimentions of the board

    - For training data
        - How too:
            - [x] Evaluate the fitness of each individual in the population (time limit, sufficient fitness achieved, etc.)
            - [x] Select the fittest individuals for reproduction. (Parents)
            - [x] Breed new individuals through crossover and mutation operations to give birth to offspring.
            - [x] Replace the least-fit individuals of the population with new individuals.
            
            - Abstraction:
                - The way I am going to abstract the genarational neural network
                - I am going to make a maker and a class of the nn
                - Then calculate fitness and get top 5% of nns and copy each one 20% of times and each one is slightly changed (genes)
                - Fitness:
                    - How to calculate fitness
                        - Varibles:
                            - Moves to finish
                            - Did they win
        - Score is how well the nn did
        - Use Time and a bool which accounts for it the nn won or not
        - What do I play the nn agaist?
            - Humans? (me?) => that would take a lonnnng time to gather sufficient data
            - Random number generation? => this might not get the nn that far.
            - Itself? Not sure what would happen tbh
        - Do I use back propagation??
- Measure the output of the genarational net

# Analytics
- [x] Possible firebase
- [x] Possible AI
- [+] Random inputs
- [+] Run every game
- [+] How many types of wins
- [+] Number of moves per game
- [+] Data Analytics
- [ ] Changing Model Varibles
- [+] Unit Testing
- [ ] Use the 4 corner stones of computer science
- [+] Abstraction
- [+] Probability
- [+] Change 1 Varible

# Research
- [ ] Stratagies in Games eg. xs & os stratagies, game of life
- [ ] Hard Logic vs Fuzzy Logic -> connect 4 uses fuzzy logic not hard logic
- [ ] How to use Machine Learning to solve games
- [ ] Definition of Abstraction

# Total Proj
- [ ] Research
- [+] Game
- [+] Testing Game
- [x] AI
- [x] Testing AI
- [+] Analytics
- [ ] Report
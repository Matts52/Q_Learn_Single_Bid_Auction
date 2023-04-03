# Single State Q-Learning Algorithm for Sealed Bid Auction's

This program intends to apply a simple single state Q-Learning algorithm to learn the optimal bid for different single sealed bid auctions with customizable parameters. Below, the following components of the program will be described:

1. The Game
2. The Algorithm
3. Customizable Parameters
   - Game Parameters
   - Algorithm Parameters
   - Agent Parameters
4. Auction Types
   - Traditional > First-Price Sealed Bid Auction
   - Reverse > Second-Price Sealed Bid Auction
   - Loser Pays
5. Output
6. Future Directions

__________________________

## 1. The Game

The game implemented here is a two-player sealed bid auction for an item. Essentially, we have our automated agent who is trying to optimize their bid to gain the highest possible utility. The other player with which our agent repeatedly plays against is one who determines their bid based on a normal distribution dictated by input parameters. Additionally, the values of the item being bid on is determined in random normal fashion again based on user input parameters.

**One important rule is that our agent wins all ties between itself and the other player.**

## 2. The Algorithm

I employ a simple, model-free reinforcement algorithm to learn the optimal bidding strategy. Essentially, a table of action values are iteratively updated until convergence on an optimal distribution of action choices. The updating algorithm is as such. The algorithm can be fully described here https://en.wikipedia.org/wiki/Q-learning. In our case, we only have one state, the initial state where no bids have been selected. Also, our reward function is going to be based on the derived utility of the agent rather than the absolute winnings of the game.

As an additional note, epsilon annealling is applied in this algorithm so that exploration is reduced as we head towards a convergence state.

## 3. Customizable Parameter Definitions

Game Parameters:
- <ins>Auction Type:</ins> The style of auction to be played by the agents. This will determine how winnings are distributed from each round of the game

Algorithm Parameters:
- <ins>Rounds:</ins> The numbers of times you would like the agent to play the auction, a higher number will lead to more desirable convergence properties
- <ins>Alpha:</ins>  The learning rate of the algorithm, essentially how much our agent updates its choices with each round of the auction
- <ins>Gamma:</ins> The discount factor of the algorithm, how much does the agent prefer future rewards as opposed to current ones. For desirable properties, it is advised this is placed at 0.5
- <ins>Epsilon:</ins> The exploration rate of the alorithm, or the rate at which the algorithm explores the action space initially
  
Agent Parameters:
- <ins>Risk Aversion:</ins> A multiplier which scales the losing outcomes experienced by the agent linearly to make losing outcomes more drastic to experienced utility
- <ins>Risk Loving:</ins> A multiplier which scales the winning outcomes experienced by the agent linearly to make winning outcomes more drastic to experienced utility
- <ins>Other Mean:</ins> The mean value of the normal distribution with which the other player selects their bid
- <ins>Other Std:</ins> The standard deviation value of the normal distribution with which the other player selects their bid
- <ins>Value Mean:</ins> The mean value of the normal distribution describing the value of the item being bid on
- <ins>Value Std:</ins> The standard deviation of the normal distribution describing the value of the item being bid on


## 4. Auction Types

- <ins>Traditional:</ins> This is a typical auction where the winner pays the amount they bid, winnings are determined by the value of the item being bid on minus the winning bid
- <ins>Reverse:</ins> This is essentially a "Second-Price" auction in this case, where the winner pays the amount of the second highest bid (or losing bidder in this case). Thus, the winnings for the winner is the value of the item being bid on minus the value of the losing bid
- <ins>Loser Pays:</ins> This is an unconventional auction where the loser pays for the winning bid and does not win the item being bid on, this the winnings for the winner is the entirety of the value of the item being bid on


## 5. Output

The current state of the program outputs three metrics and four graphs. 

The three metrics are:
1. The average value of the winnings for our agent through all rounds played. 
2. The average utility derived by our agent through all rounds played
3. The optimal bid for the agent to play based on the ending convergence of the Q-Learning iterative algorithm

The four charts are:
1. A histogram of the distribution of winning values from all rounds
2. A histogram of the distribution of derived utility from all rounds
3. The ending L1-normalized Q-values for all of the possible bids (higher amounts mean the bid is more optimal to play)
4. An overlaid histogram of all of the bids played by our agent compared to the bids played by the other agent


## 6. Future Directions

Some interesting future directions to possibly explore are:

- Different or more complex utility functions for our agent
- Multiple other players rather than a single other players
- Different reinforcement algorithms for optimal choice convergence
- Functionality to run the simulation multiple times to make population inference
- More complex other player bidding strategies
- Different auction types




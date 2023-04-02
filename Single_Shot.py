import numpy as np
import matplotlib.pyplot as plt
import random


def value_rand_norm(mu, sigma):
    def inner_func():
        return min(max(int(np.random.normal(mu, sigma)), 0), 10)
    return inner_func



def other_player_rand_norm(mu, sigma):
    def inner_func():
        return min(max(int(np.random.normal(mu, sigma)), 0), 10)
    return inner_func




def basic_agent_utility(risk_aversion=1.0, risk_loving=1.0):
    def inner_func(reward):
        if reward < 0:
            return risk_aversion * reward
        else:
            return risk_loving * reward
    return inner_func





def reverse_auction(agent_bid, other_bid, value):
    if agent_bid < other_bid:
        return 0  # Penalty for bidding lower than the other player
    else:
        return value - other_bid  # Reward for winning the auction



def traditional_auction(agent_bid, other_bid, value):
    if agent_bid < other_bid:
        return 0  # Penalty for bidding lower than the other player
    else:
        return value - agent_bid  # Reward for winning the auction



def loser_pays_traditional(agent_bid, other_bid, value):
    if agent_bid < other_bid:
        return -1 * other_bid  # Penalty for bidding lower than the other player
    else:
        return value  # Reward for winning the auction



def loser_pays_reverse(agent_bid, other_bid, value):
    if agent_bid < other_bid:
        return -1 * agent_bid # Penalty for bidding lower than the other player
    else:
        return value  # Reward for winning the auction




def learn_the_game(alpha, gamma, epsilon, other_player_func, agent_utility_func, value_func, game, num_rounds, visual=False, results=False):

    # Define the action space
    action_space = [x for x in range(0, 11)]

    #Init the Q table with zeroes
    Q = np.zeros((1, len(action_space)))

    state, next_state = 0, 0 #since we only have a starting bid of zero each time, always 0

    rewards = []
    utilities = []
    
    eps_step = epsilon/num_rounds

    # Loop until convergence
    for i in range(num_rounds):

        # Choose an action based on actor policy and epsilon-greedy exploration
        if np.random.rand() < epsilon:
            action = np.random.choice(action_space)
        else:
            action = np.argmax(Q[state])

        # generate the other player's move based on the inputted function
        other_action = other_player_func()

        # determine underlying value of the item
        value = value_func()

        # Simulate the game to get the reward and next state
        reward = game(action, other_action, value)
        rewards.append(reward)
        
        #calculate the agent utility as the maximization parameter
        utility = agent_utility_func(reward)
        utilities.append(utility)

        # Update the Q-table
        Q[state, action] = Q[state, action] + alpha * (utility + gamma * np.max(Q[next_state]) - Q[state, action])
    
        #anneal the epsilon
        epsilon -= eps_step
    
    #normalize our Q parameter
    np_Q = np.array(Q[0])
    normed_out = np_Q/np.linalg.norm(np_Q)
    mean_winnings = np.mean(rewards)
    mean_utility = np.mean(utilities)
    opt_choice = np.argmax(Q)
    
    if visual:
        plt.hist(rewards)
        plt.show()
        #plt.hist(utilities)
        #plt.show()
        plt.step([x for x in range(11)], normed_out)
        plt.show()

    if results:
        # Print the final Q-table
        print("Optimal Choice: ", opt_choice)
        print("Mean Winnings: ", mean_winnings)
        print("Mean Utility: ", mean_utility)
        print("Normalized Q-table: ")
        for i in range(len(normed_out)):
            print(" Key:", i, "Value:", normed_out[i])
    
    return (mean_winnings, mean_utility, normed_out, opt_choice)




if __name__ == '__main__':

    # Set the random seed to 42
    #np.random.seed(52)

    mean_winnings, mean_utilities, q_tables, opt_choices = [], [], [], []

    #define the other player's betting function
    other_func = other_player_rand_norm(6, 1)
    agent_func = basic_agent_utility(risk_aversion=3.0, risk_loving=1.0)
    value_func = value_rand_norm(8,1)
    game_to_play = traditional_auction

    Q_sim = learn_the_game(alpha=0.8, gamma=0.5, epsilon=0.3, other_player_func=other_func, 
                       agent_utility_func=agent_func, value_func=value_func,  game=reverse_auction, num_rounds=10000, 
                       visual=False, results=True)


    #for i in range(100):
    #
    #    Q_sim = learn_the_game(alpha=0.8, gamma=0.5, epsilon=0.3, other_player_func=other_func, 
    #                   agent_utility_func=agent_func, value_func=value_func,  game=reverse_auction, num_rounds=1000, 
    #                   visual=False, results=False)
    #
    #    mean_winnings.append(Q_sim[0])
    #    mean_utilities.append(Q_sim[1])
    #    q_tables.append(Q_sim[2])
    #    q_means = np.mean(q_tables, axis=0)
    #    opt_choices = Q_sim[3]
    #
    ##print(q_means)
    #
    #plt.hist(mean_winnings)
    #plt.show()
    #plt.hist(opt_choices)
    #plt.show()


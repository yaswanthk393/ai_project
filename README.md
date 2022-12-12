# ai_project
# Tic Tac Toe Implementation using Multi Agents
# Introduction

 Tic Tac Toe is a game with 9 Boxes, the player gets a winning point when all the 3 Consecutive Blocks in a Row, Column or Diagonal are identical.

# Implementation
   
 we are going to perform with multiple Agents like Alpha-Beta and Min-Max Algorithms from Adverserial Search and Q-learning from Reinforcement Learning. Here every Agent tries to make a Optimal move by checking the Number of Moves, Number of nodes expanded and the time taken for game completion.


# Objectives

Design Adversarial Search Algorithm and Reinforcement Agents to solve Tic Tac Toe game.

Design of 3 Artificial Intelligence Agents
 1.Q learning Technique
 2.Min-Max Algorithm
 3.Alpha-Beta Pruning

Plays Tic Tac Toe game multiple times among them to find the efficient Algorithm.

The player who gets the three consecutive symbols in a row or column or diagonally gains a winning point.

Comparing the efficiency of three algorithms by calculating the corresponding performance metrics and to find out which performs better either adversarial search or Reinforcement Learning.

# Approaches
The first Approach is Q-Learning from Reinforcement Learning. 

The Second approach we used is from Adversarial Search.
           1.Min-Max Algorithm
           2.Alpha-Beta Pruning.
           
Technology Stack

1.Python 3

![](https://github.com/KalpanaChamala/Tic-Tac-Toe-Project/blob/main/tic%20tac%20toe/Image.png)


# Brief Description of Agents

# Min-Max Algorithm

  a.It's a recursive/backtracking algorithm that's utilized in decision-making and game theory.

  b.It gives the player the best move by presuming the opponent is likewise playing well.

  c.Recursion is used to search through the Game Tree.

  d.This Algorithm is commonly employed in games such as Chess, Tic Tac Toe, and other two-player games.

  e. To explore the entire game, our algorithm uses a Depth-First Search. It goes all the way down to the terminal node and  ther ecurses back up.
  
  ![](https://github.com/KalpanaChamala/Tic-Tac-Toe-Project/blob/main/tic%20tac%20toe/min%20max.jpeg)

            


# Alpha-Beta 

    Alpha-beta pruning is a search technique that always tries to reduce the number of nodes in its search tree that are 
determined by the min max algorithm. It is a two-player game with an adversarial search method. When applied to a min max tree,it produces the same moves as min-max, but prunes out those branches that have no bearing on the final decision.

![](https://github.com/KalpanaChamala/Tic-Tac-Toe-Project/blob/main/tic%20tac%20toe/alpah%20beta.png)

         

# Q-Learning   

    Q-Learning is a prominent reinforcement learning method based on the Bellman Equation, in which the agent tries to learn the 
       policies that provide the optimal behaviors to take in order to maximize the rewards. These best moves are learned from previous experiences.
    It is always used to represent the quality of actions taken at each state, with the agent's purpose being to maximize the
       value of "Q."    
       
   ![](https://github.com/KalpanaChamala/Tic-Tac-Toe-Project/blob/main/tic%20tac%20toe/q%20learning.jpeg)

 # Reinforcement Learing
 
   It's a machine learning technique that allows the agent to learn by trial and error in an interactive environment, using 
input from its own actions and experiences.  

![](https://github.com/KalpanaChamala/Tic-Tac-Toe-Project/blob/main/tic%20tac%20toe/reinforcemt.png)

       

 # Deliverables

  a.User Documentation model which gives details about the Tic Tac Toe game implementation using Min-Max, Alpha-Beta and         Reinforcement Learning Agents.

  b.Algorithms developed for AI Agents using Python Programming Language(.py files)

  c.Github Repository link for Python code and related files.

  d.Youtube video Demonstrating project implementation and slides
        
 # Evaluation Methodolgy

  a.Project is evaluated based on the implementation of all the AI agents.

  b.Calculate the number of wins of the corresponding agent through which it plays multiple times one on one to find the efficient Agent.

  c.A comparison table given for the three agents based on the Tic Tac Toe moves and corresponding score and also the win rate. 

  d.Time and space complexity comparison for the three agents implemented.

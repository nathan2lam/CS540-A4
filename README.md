Page Replacement Algorithms

This Python program simulates three page replacement algorithms: LRU (Least Recently Used), FIFO (First In, First Out), and Optimal.

Description

The program utilizes deque from the collections module to represent page frames.
Each algorithm (lru_page_faults, fifo_page_faults, optimal_page_faults) takes a reference string and the number of frames as inputs.
Detailed comments within each function explain the algorithm steps and data structures used.
The sample input consists of a reference string [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5] and a frame number 4.
This input simulates page replacement algorithms for the given reference string and frame limit.

# Students-Graph
This project takes a .csv file and turns the data into a graph, using the argparse library to modify edges' criteria in the command line.

An example of code use, according to the following instruction at the command prompt:
- Instruction: python3 main.py -n "math or writing" -p "math score",0 "writing score",0 -a -tn 10
- Detailing:
     -n "math or writing" : name of the file where the graph image will be saved;
     -p "math score",0 "writing score",0 : pairs of attributes and thresholds to consider to form edges;
     -a : means that the joining of edges must be considered (that is, all edges that connect nodes with the same "math score" (with threshold 0) + all edges that connect nodes with the same "writing score" (with threshold 0);
     -tn 10 : the 10 edges with the highest degree of the graph must be shown in the table.
     - other files (graph_functions, csv_functions, table_functions) contain the functions used in the main.py file.

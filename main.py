from igraph import *
from igraph.drawing import graph
import csv
import argparse
from graph_functions import *
from csv_functions import *
import matplotlib.pyplot as plt
from table_functions import *

###############################################################
#                                                             #
#    Passando dados para a linha de comando com o argparse    #
#                                                             #
###############################################################
def pair(s):
    try:
        a, t = map(str, s.split(','))
        return a, t
    except:
        raise argparse.ArgumentTypeError("Pairs must be: atribute,threshold (no space in between)")
parser = argparse.ArgumentParser(description="STUDENTS GRAPH")
parser.add_argument('-n', '--name', help="Archive name", required=True, metavar='', type=str)
parser.add_argument('-p', '--pairs', help="Pairs: atribute, threshold", required=True, dest="pairs", type=pair, nargs='+')
parser.add_argument('-tn', '--tableNumber', type=int, help="Number of edges on table", required=True)
group = parser.add_mutually_exclusive_group()
group.add_argument('-a', '--all', action='store_true', help='all edges with given atributes')
group.add_argument('-o', '--only', action='store_true', help='only edges of pairs with all given atributes in common')
args = parser.parse_args()

# Estruturas usadas:
descr = []              #guarda os campos do dicionário
person = dict()         #cada pessoa é um dicionário
students = []           #lista de pessoas (dicionários)
line_count = 0          #quantidade de linhas do csv
g = Graph()             #grafo com as informações do csv          
g_colors = []           #cores dos edges
v_colors = []           #cores dos vértices (azul para homem, rosa para mulher)


if __name__ =='__main__':
    line_count = import_csv(descr, person, students)
    graph_info(g, line_count, descr, students, v_colors)
    if args.only:
        find_edges_pairs(args.pairs, students, g, g_colors)
    elif args.all:
        find_edges_all(args.pairs, students, g, g_colors)
    else:
        print("choose between -o or -a")

    # Configurações de plot:
    visual_style = {}
    visual_style["vertex_size"] = 10
    visual_style["vertex_color"] = v_colors
    visual_style["edge_color"] = g_colors
    visual_style["vertex_label"] = g.vs["ID"]
    visual_style["vertex_label_size"] = 10
    visual_style["vertex_label_dist"] = 1.5
    visual_style["edge_width"] = 0.1
    visual_style["layout"] = "mds"
    visual_style["bbox"] = (3000, 3000)
    visual_style["margin"] = 10
    name = args.name+".pdf"
    plot(g, name, **visual_style)
    plot_ordered(g, args.tableNumber, pairsTOatributes(args.pairs), students)


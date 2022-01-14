from igraph import *

#------ Cores dos edges --------
dic_colors = {'gender': 'green', 
'race/ethnicity':'yellow',
'parental level of education':'blue',
'lunch' : 'red',
'test preparation course' : 'purple',
'math score': 'pink',
'reading score' : 'grey',
'writing score' : 'orange'}

###############################################################
#                                                             #
#                       Criando um grafo                      #
#                                                             #
###############################################################
# Objetivo: passar as informações do csv para um grafo (somente vértices)
def graph_info(graph, line_count, description, students, v_colors):
    graph.add_vertices(line_count-1) #Cada linha representa um vértice (exceto a primeira)

    #------------ Colocando as descrições  ----------
    for d in description:
        j=0
        graph[d] = []
        graph["ID"] = []
        for s in students:
            if d=="gender":
                if students[j][d] == "male":
                    v_colors.append('blue')
                else:
                    v_colors.append('pink')
            graph["ID"].append(students[j]["ID"])
            graph[d].append(students[j][d])
            j += 1
        graph.vs[d] = graph[d] #verificar se precisa desse g.vs mesmo
        graph.vs["ID"] = graph["ID"]




###############################################################
#                                                             #
#                     Encontrando os edges                    #
#                                                             #
###############################################################
#------------ Função booleana -------------
# Objetivo: dado um atributo, um threshold, o índice de dois vértices e a lista
# de estudantes, retornar true se o os dois vértices formarem um edge de acordo
# com o atributo dado
def is_edge(info, threshold, i, j, students):
    edge=0
    if ((i, j) != (j, i)):
        if info.isdigit() and (int(students[i][info]) - threshold <= int(students[j][info])) and (int(students[i][info]) + threshold >= int(students[j][info])):
            edge=1
        elif students[i][info] == students[j][info]:
            edge=1
    return edge
    

#------------ Encontrando os edges (LISTA) -------------
# Objetivo: dada uma lista de pares (atributo, threshold), adicionar ao grafo os edges 
# que unem vértices cujos atributos estão dentro do threshold dado (as cores dos edges
# são dadas pelo dicionário de cores definido acima (dic_colors))               

def find_edges_pairs(pairs, students, g, g_colors):
    n = len(pairs)
    s = len(students)
    for i in range(0, s): #percorre os estudantes
        for j in range(0, s): #para formar uma dupla de estudantes
            flag_end=0 #se algum dos requisitos não for atendido, para de analisar a dupla
            cont=0 #para percorrer os atributos
            while not flag_end and cont!=n:
                if is_edge(pairs[cont][0], int(pairs[cont][1]), i, j, students):
                    cont += 1
                    if cont==n: #todos os requisitos foram atendidos
                        g.add_edge(i, j)
                        g_colors.append(dic_colors[pairs[cont-1][0]])
                else:
                    flag_end=1



#------------ Encontrando os edges (LISTA) -------------
# Objetivo: dada uma lista de pares (atributo, threshold), adicionar ao grafo os edges 
# que unem vértices cujos atributos estão dentro do threshold dado (as cores dos edges
# são dadas pelo dicionário de cores definido acima (dic_colors))               

def find_edges_all(pairs, students, g, g_colors):
    n = len(pairs)
    s = len(students)
    for i in range(0, s): #percorre os estudantes
        for j in range(0, s): #para formar uma dupla de estudantes
            for cont in range(0, n):
                if is_edge(pairs[cont][0], int(pairs[cont][1]), i, j, students):
                    g.add_edge(i, j)
                    g_colors.append(dic_colors[pairs[cont][0]])


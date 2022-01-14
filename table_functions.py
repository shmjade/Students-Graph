from os import name
import matplotlib.pyplot as plt
import pandas as pd

def pairsTOatributes(pairs):
    atributes=[]
    cont=0
    for p in pairs:
        atributes.append(pairs[cont][0])
        cont+=1
    return atributes

def plot_ordered(graph, n, atributes, students):
    for i in range(0, len(students)):
        students[i]['Degree'] = graph.degree(i)
    df = pd.DataFrame(students)
    # Ordenar pelo grau do vértice (degree):
    new_df = df.sort_values(by='Degree', ascending=False, ignore_index=True)
    rank=[]
    data=[]
    columns = ["ID", "Degree"]
    for a in atributes:
        columns.append(a)
    for i in range(0, n):
        rank.append(i+1)
        new = [new_df["ID"][i], new_df["Degree"][i]]
        for a in atributes:
            new.append(new_df[a][i])
        data.append(new)
    fig, ax = plt.subplots() 
    ax.set_axis_off() 
    table = ax.table( 
        cellText = data,  
        rowLabels = rank,  
        colLabels = columns, 
        rowColours =["palegreen"] * n,  
        colColours =["palegreen"] * n, 
        cellLoc ='center',  
        loc ='upper center')         
    ax.set_title('Edges\' degrees', 
                fontweight ="bold") 
    plt.show()


def plot_table(graph, n):
    rank=[]
    data=[]
    for i in range(0, n):
        rank.append(i+1)
        data.append([graph.vs["ID"][i], graph.degree(i)])
    columns = ("ID", "Degree")
    fig, ax = plt.subplots() 
    ax.set_axis_off() 
    table = ax.table( 
        cellText = data,  
        rowLabels = rank,  
        colLabels = columns, 
        rowColours =["palegreen"] * n,  
        colColours =["palegreen"] * n, 
        cellLoc ='center',  
        loc ='upper center')         
    ax.set_title('Edges\' degrees', 
                fontweight ="bold") 
    plt.show() 
    plt.savefig("table.pdf")
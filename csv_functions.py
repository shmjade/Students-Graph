import csv
#----- Leitura do arquivo para um dicionário:
def import_csv(description, dictionary, listOfDictionaries):
    line_count=0
    with open('StudentsPerformance.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if line_count == 0:
                {", ".join(row)}
                for r in row:
                    {", ".join(r)}
                    description.append(r) #guarda os campos do dicionário (da 1ª linha do csv)
                line_count += 1
            #----- Criando um dicionário -------
            dictionary["ID"] = line_count #Chave única dos alunos
            for i in description:
                dictionary[i] = row[i] #atribui a informação de cada pessoa em um dicionário
            #----- Adicionando à lista de dicionários ------
            listOfDictionaries.append(dictionary.copy()) #adiciona à lista de estudantes
            line_count += 1
        #print(f'Processed {line_count} lines.')
    return line_count

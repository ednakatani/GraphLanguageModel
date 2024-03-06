import networkx

FILE = "dataset/MA/domCasmurro.txt"

def read_file(file):
    with open(file, "r", encoding="UTF8") as f:
        data = f.read()
    return data


def create_graph(data):

    graph = networkx.Graph()
    hashtable = {}
    '''
    hashtable = { 
        "word1": 0,
        "word2": 1,
        ...
        "wordN": n-1,
    }
    '''

    return graph, hashtable


def create_nodes(word, graph, hashtable):

    if word not in hashtable:
        hashtable[word] = len(hashtable)
        graph.add_node(hashtable[word])
    
    return graph, hashtable


def populate_graph(data, graph, hashtable):

    ## For each word, create a node. This word will be the key of the dictionary.
    ## The value of the dictionary will be the node index.

    previous_word = None
    point_present = False
    end_of_sentence = False

    for word in data.split():

        word = word.lower()

        if "." in word:
            point_present = True

        #remove characters that are not letters
        word = ''.join(e for e in word if e.isalnum())

        if len(word) == 0:
            continue

        graph, hashtable = create_nodes(word, graph, hashtable)

        
        if not end_of_sentence:
        
            if previous_word is not None:
                if graph.has_edge(hashtable[previous_word], hashtable[word]):
                    graph[hashtable[previous_word]][hashtable[word]]['weight'] += 1
                else:
                    graph.add_edge(hashtable[previous_word], hashtable[word], weight=1)
            
            previous_word = word
        
        else:
            previous_word = word
            end_of_sentence = False
        
        if point_present:
            end_of_sentence = True
            point_present = False
            

    return graph, hashtable







f = read_file(FILE)

to_remove = ["'", '"', ",", "(", ")", "[", "]", "{", "}", ":", ";", "\n", "\t", "\r", "!", "?", ".", "’", "‘", "“", "”", "—", "–", "…", "-"]

for char in to_remove:
    f = f.replace(char, " ")

g, h = create_graph(f)
g, h = populate_graph(f, g, h)

#plot graph
"""import matplotlib.pyplot as plt
plt.figure(figsize=(20,20))
networkx.draw(g, with_labels=True,)
plt.show()"""

#export graph
networkx.write_gexf(g, "graph.gexf")

#export hashtable
with open("hashtable.txt", "w") as f:
    f.write(str(h))


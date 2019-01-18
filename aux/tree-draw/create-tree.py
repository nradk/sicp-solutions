# Output a DOT file with a graph description for the execution tree of
# "count-change". For solution to Exercise 1.14

import os

nodes = set()
edges = set()

def first_denomination(kinds_of_coins):
    if kinds_of_coins == 1:
        return 1
    elif kinds_of_coins == 2:
        return 5
    elif kinds_of_coins == 3:
        return 10
    elif kinds_of_coins == 4:
        return 25 
    else:
        return 50

def cc(amount,kinds_of_coins):
    if amount == 0:
        return 1
    elif amount < 0 or kinds_of_coins == 0:
        return 0
    else:
        this = "(cc %s %s)" % (amount,kinds_of_coins)
        left = "(cc %s %s)" % (amount,kinds_of_coins - 1)
        right = "(cc %s %s)" % (amount - first_denomination(kinds_of_coins),
                kinds_of_coins)
        nodes.add(left)
        nodes.add(right)
        edges.add((this,left))
        edges.add((this,right))
        return cc(amount,kinds_of_coins - 1)\
            + cc(amount - first_denomination(kinds_of_coins), kinds_of_coins)

def count_change(amount):
    nodes.add("(count-change %s)" % amount)
    nodes.add("(cc %s 5)" % amount)
    edges.add(("(count-change %s)" % amount, "(cc %s 5)" % amount))
    return cc(amount,5)

print(count_change(11))

dot = "digraph G {\n"
dot += "\tgraph [layout=dot rankdir=TD]\n" 
dot += "\tnode [shape=plaintext fontname=Inconsolata]\n\n" 
for node in nodes:
    dot += "\t\"" + node + "\"\n"
dot += "\n"
for edge in edges:
    dot +=  "\t\"" + edge[0] + "\" -> \"" + edge[1] + "\"\n";
dot += "\n}\n"

f = open("./tree.dot","w+")
f.write(dot)
f.close()

os.system("dot -Tpng tree.dot -otree.png")

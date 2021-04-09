# all topological graphs must be Directed Acyclic Graphs (DAG)

def topological_order(graph, start):

    def helper(passed, options):
        if options:
            for i, item in enumerate(options):
                passed_new = passed.copy() + [item]
                options_new = options[:i] + options[i+1:]
                if item in graph:
                    items_considered = passed_new + options_new
                    options_new.extend(it for it in graph[item] if it not in items_considered)
                helper(passed_new, options_new)
        else:
            orderings.append(passed)

    orderings = []

    helper([start], graph[start])

    return orderings


graph = {'a': ['b', 'c', 'd', 'e', 'f'],
         'b': ['c', 'f'],
         'c': ['d'],
         'e': ['d', 'f']
         }
start = 'a'

orderings = topological_order(graph, start)

for x in range(1, len(orderings)):
    print(*orderings[x])
print(len(orderings))

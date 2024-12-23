from collections import defaultdict

f = open("input.txt", 'r')
f = f.read().strip()
f = f.split("\n")

DICT = defaultdict(set)

for link in f:
    a,b = link.split("-")

    DICT[a].add(b)
    DICT[b].add(a)
        
res = []


# algorithm BronKerbosch2(R, P, X) is
#     if P and X are both empty then
#         report R as a maximal clique
#     choose a pivot vertex u in P U X
#     for each vertex v in P \ N(u) do
#         BronKerbosch2(R U {v}, P ⋂ N(v), X ⋂ N(v))
#         P := P \ {v}
#         X := X U {v}


def BronKerbosch2(R, P, X):
    if not P and not X:
        CLIQUES.append(R)
        return

    pivot = next(iter(P | X))
    for v in P - DICT[pivot]:
        BronKerbosch2(R | {v}, P & DICT[v], X & DICT[v])
        P.remove(v)
        X.add(v)


CLIQUES = []
BronKerbosch2(set(), set(DICT.keys()), set())
largest_clique = max(CLIQUES, key=len)
print(','.join(sorted(largest_clique)))




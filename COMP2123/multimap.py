#Use normal dict object but make each value a list

from collections import defaultdict
md = defaultdict(list)
md[1].append("a")
md[1].append("b")
md[2].append("c")
md[2].append("d")
print(md[1], md[2])

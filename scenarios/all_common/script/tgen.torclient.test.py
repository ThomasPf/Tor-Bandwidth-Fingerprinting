import networkx as nx

G = nx.DiGraph()

G.add_node("start", serverport="8888", peers="localhost:8888")
G.add_node("transfer", type="get", protocol="tcp", size="50 MiB")
G.add_node("pause", time="1")

G.add_edge("start", "transfer")
G.add_edge("transfer", "pause")
G.add_edge("pause", "start")

nx.write_graphml(G, "../tgen.torclient.test.graphml.xml")

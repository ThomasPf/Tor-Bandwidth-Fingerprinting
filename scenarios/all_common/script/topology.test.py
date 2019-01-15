import networkx as nx

G = nx.Graph()

G.add_node("c", type="client", ip="0.0.0.0", geocode="EU", bandwidthup=10240, bandwidthdown=10240, packetloss=0.0)
G.add_node("r1", type="relay", ip="0.0.0.1", geocode="EU", bandwidthup=10240, bandwidthdown=10240, packetloss=0.0)
G.add_node("r2", type="relay", ip="0.0.0.2", geocode="EU", bandwidthup=10240, bandwidthdown=10240, packetloss=0.0)
G.add_node("r3", type="relay", ip="0.0.0.3", geocode="EU", bandwidthup=10240, bandwidthdown=10240, packetloss=0.0)
G.add_node("s", type="server", ip="0.0.0.4", geocode="EU", bandwidthup=10240, bandwidthdown=10240, packetloss=0.0)


G.add_edge("c", "r1", latency=50.0, jitter=0.0, packetloss=0.0)
G.add_edge("r1", "r2", latency=50.0, jitter=0.0, packetloss=0.0)
G.add_edge("r2", "r3", latency=50.0, jitter=0.0, packetloss=0.0)
G.add_edge("r3", "s", latency=50.0, jitter=0.0, packetloss=0.0)

nx.write_graphml(G, "../topology.test.graphml.xml")

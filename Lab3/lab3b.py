def parse_file(filename):
    graph = {}

    file = open(filename, "r")
    file.readline()  
    for line in file: 
        parts = line.strip().split('|')

        src, dst = parts[0], parts[1]
        metrics = parts[2].split(',')
        # get delay 
        delay = float(metrics[1].split('=')[1])
        if src not in graph:
            graph[src] = []
        graph[src].append((dst, delay))

    file.close()
    return graph

def find_route(source, dest, max_hops, visit, graph):
    #recurssion 
    if source == dest:
        return 0  #no delay added if reached etc 

    if max_hops == 0 or source in visit:
        return float('inf')  # stop search 

    visit.append(source)  # visited
    min_delay = float('inf')

    if source in graph: 
        neighbors = graph[source]
        for neighbor, delay in neighbors:
            path_delay = find_route(neighbor, dest, max_hops - 1, visit[:], graph)
            if path_delay != float('inf'):
                min_delay = min(min_delay, delay + path_delay)

    return min_delay

#user inp 
print("Enter the filename:")
filename = input().strip()

print("Enter the maximum number of hops:")
max_hops = int(input().strip())

print("Enter the source node:")
source = input().strip()

print("Enter the destination node:")
destination = input().strip()

#parse
graph = parse_file(filename)

shortest_delay = find_route(source, destination, max_hops, [], graph)

#display
if shortest_delay == float('inf'):
    print("No valid path found from", source, "to", destination, "within", max_hops, "hops.")
else:
    print("Best delay from", source, "to", destination, "within", max_hops, "hops:", shortest_delay)
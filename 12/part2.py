f=open('12/input.txt','r')
l=f.read().split("\n")

#Build a x,y coordinate dictionary with height as value
x=0
y=0
import string
height_dict={}
for l in l:
    for c in l:
        if c=="S":
            start_node=(x,y)
            height_dict[(x,y)]=0
        elif c=="E":
            end_node=(x,y)
            height_dict[(x,y)]=25
        else:
            height_dict[(x,y)]=string.ascii_lowercase.index(c)
        x+=1
    y+=1
    x=0

#Build a graph of all possible directions
graph_dict={}
directions=[(0,1),(1,0),(-1,0),(0,-1)]
for origin_c,origin_h in height_dict.items():
    graph_dict[origin_c]=[]
    for d in directions:
        dest_c=(origin_c[0]+d[0],origin_c[1]+d[1])
        if dest_c in height_dict.keys():
            dest_h=height_dict[dest_c]
            if dest_h-origin_h<=1:
                graph_dict[origin_c].append(dest_c)

#Apply the Dijkstra algorith to find shortest path
import heapq
def dijkstra(graph,node):
    distances={node:float('inf') for node in graph}
    distances[node]=0
    came_from={node:None for node in graph}
    queue=[(0,node)]
    
    while queue:
        current_distance,current_node=heapq.heappop(queue)
        # relaxation
        for next_node in graph[current_node]:
            distance_temp=current_distance+1
            if distance_temp<distances[next_node]:
                distances[next_node]=distance_temp
                came_from[next_node]=current_node
                heapq.heappush(queue,(distance_temp,next_node))
    return distances,came_from

#Find the shortest path of all "a" elevation points
min_dist=float('inf')
for coord,height in height_dict.items():
    if height==0:
        dist=dijkstra(graph_dict,coord)[0][end_node]
        if dist<min_dist:
            min_dist=dist

print(min_dist)
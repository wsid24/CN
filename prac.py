###############################################################
# YOUR ORIGINAL CONTENT (UNMODIFIED)
###############################################################

#Link State Routing Protocol using dijkstra algorithm 
def dijkstra(graph,start):
    
    dist={node:float('inf') for node in graph}
    dist[start]=0
    
    parent={node:None for node in graph}
    
    visited=set()
    
    while len(visited)<len(graph):
        curr=None
        for node in graph:
            if node not in visited:
                if curr is None or dist[node]<dist[curr]:
                    curr=node
                    
        visited.add(curr)
        
        for neigh,cost in graph[curr].items():
            if neigh not in visited:
                new_cost=dist[curr]+cost
                if new_cost < dist[neigh]:
                    dist[neigh]=new_cost
                    parent[neigh]=curr
              
    return dist,parent
    
    
def print_route(start,dist,parent):
    print("Routing table for router:",start)
    
    for node in dist:
        if node==start:
            continue
        path=[]
        
        temp=node
        while temp is not None:
            path.append(temp)
            temp=parent[temp]
        path=path[::-1]
        
        print(f"Cost for the {node}:", dist[node])
        print("Path:",path)
        
if __name__=="__main__":
    
    graph = {}

    n = int(input("Enter number of routers: "))
    
    print("\nEnter router names:")
    routers = []
    for _ in range(n):
        r = input().strip()
        routers.append(r)
        graph[r] = {}
    
    m = int(input("\nEnter number of links: "))
    
    print("\nEnter each link in the format: Router1 Router2 Cost")
    for _ in range(m):
        u, v, c = input().split()
        c = int(c)
        graph[u][v] = c
        graph[v][u] = c    
    
    start = input("\nEnter the source router: ")
    
    dist,parent=dijkstra(graph,start)
    print_route(start,dist,parent)




###############################################################
# Distance Vector Routing (UNMODIFIED)
###############################################################

INF = 999

n = int(input("Enter number of nodes: "))
print("Enter cost matrix (use 999 for no link):")
cost = [list(map(int, input().split())) for _ in range(n)]

dist = [row[:] for row in cost]

updated = True
while updated:
    updated = False
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[i][j] > cost[i][k] + dist[k][j]:
                    dist[i][j] = cost[i][k] + dist[k][j]
                    updated = True

print("\nFinal Distance Vector Tables:")
for i in range(n):
    print(f"Router {i}: ", dist[i])




###############################################################
# TCP HELLO PROGRAM (UNMODIFIED)
###############################################################

#server (hello_server.py)
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 5000))
server.listen(1)

print("Server waiting for connection...")

conn, addr = server.accept()
print("Connected with:", addr)

msg = conn.recv(1024).decode()
print("Client says:", msg)

conn.send("Hello from TCP Server!".encode())

conn.close()
server.close()

#client (hello_client.py)
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

client.send("Hello from TCP Client!".encode())

msg = client.recv(1024).decode()
print("Server says:", msg)

client.close()

# -------------------------------------------------------------
# ⭐ HOW TO RUN TCP HELLO PROGRAM
# -------------------------------------------------------------
# 1. Open TWO terminals.
#
# TERMINAL 1 (Server):
#     python3 combined_network_codes.py
#     → Run until this server section executes
#     → It will show "Server waiting for connection..."
#
# TERMINAL 2 (Client):
#     python3 combined_network_codes.py
#     → Run until client section executes
#
# Server Output:
#     Client says: Hello from TCP Client!
#
# Client Output:
#     Server says: Hello from TCP Server!
#
# -------------------------------------------------------------



###############################################################
# TCP FILE TRANSFER (UNMODIFIED)
###############################################################

#file_server.py
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 6000))
server.listen(1)

print("Server waiting for connection...")

conn, addr = server.accept()
print("Connected with:", addr)

filename = "received_file.txt"
f = open(filename, "wb")

while True:
    data = conn.recv(1024)
    if not data:
        break
    f.write(data)

print("File received successfully:", filename)

f.close()
conn.close()
server.close()


#file_client.py
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 6000))

filename = "sample.txt"

with open(filename, "rb") as f:
    data = f.read()
    client.sendall(data)

print("File sent successfully!")

client.close()

# -------------------------------------------------------------
# ⭐ HOW TO RUN TCP FILE TRANSFER
# -------------------------------------------------------------
# 1. Create a file in same folder:
#       sample.txt
#
# 2. Open TWO terminals.
#
# TERMINAL 1 (Server):
#     python3 combined_network_codes.py
#
# TERMINAL 2 (Client):
#     python3 combined_network_codes.py
#
# After run, check:
#       received_file.txt
# It should contain same text as sample.txt
# -------------------------------------------------------------



###############################################################
# UDP FILE TRANSFER (UNMODIFIED)
###############################################################

# UDP SERVER
import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("0.0.0.0",8000))

print("Waiting for the connection.....")

filename='rec2.txt'

f=open(filename,'wb')

while True:
    data,addr=server.recvfrom(4096)
    if data==b"END":
        break
    f.write(data)
    
f.close()
print("Success")
server.close()


# UDP CLIENT
import socket 

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_addr=("127.0.0.1",8000)

filename="send.txt"

with open(filename,'rb') as f:
    chunk=f.read(4096)
    while chunk:
        client.sendto(chunk,server_addr)
        chunk=f.read(4096)
        
client.sendto(b"END",server_addr)

print("Success")
client.close()

# -------------------------------------------------------------
# ⭐ HOW TO RUN UDP FILE TRANSFER
# -------------------------------------------------------------
# 1. Create a file in same folder:
#       send.txt
#
# 2. Open TWO terminals.
#
# TERMINAL 1 (Server):
#     python3 combined_network_codes.py
#
# TERMINAL 2 (Client):
#     python3 combined_network_codes.py
#
# After run, check:
#       rec2.txt
# -------------------------------------------------------------



###############################################################
# UDP HELLO (UNMODIFIED)
###############################################################

#server
import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("0.0.0.0",8000))

print("waiting for the client")

msg,addr=server.recvfrom(4096)
print(msg.decode())

server.sendto("hello from the server".encode(),addr)

server.close()

#client
import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_addr=("127.0.0.1",8000)

client.sendto("hello from the client".encode(),server_addr)

msg,addr=client.recvfrom(4096)
print(msg.decode())

client.close()

# -------------------------------------------------------------
# ⭐ HOW TO RUN UDP HELLO
# -------------------------------------------------------------
# Terminal 1:
#     python3 combined_network_codes.py
#
# Terminal 2:
#     python3 combined_network_codes.py
#
# Output:
#   Client → "hello from the server"
#   Server → "hello from the client"
# -------------------------------------------------------------



###############################################################
# DNS LOOKUP (UNMODIFIED)
###############################################################

import socket

choice=input("Enter the 1 for URL to IP , and 2 for IP to URL:")

if choice=='1':
    url=input("Enter the URL:")
    try:
        ip=socket.gethostbyname(url)
        print("IP is :",ip)
    except:
        print("Invalid URL")
       
elif choice=='2':
    ip=input("Enter the IP:")
    try:
        url=socket.gethostbyaddr(ip)
        print("URL is :",url[0])
    except:
        print("Invalid IP")
else:
    print("Invalid choice")

###############################################################
# END OF ORIGINAL CONTENT + ADDED INSTRUCTIONS ONLY
###############################################################

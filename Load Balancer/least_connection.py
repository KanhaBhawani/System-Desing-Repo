class LeastConnectionLoadBalancer:
    def __init__(self):
        self.serverConnections : dict[str, int]  = {}
        self.maxConnections = 1000

    def addServer(self, server: str):
        if(server in self.serverConnections):
            print(f"server {server} already present...")
            return
        self.serverConnections[server] = 0
        print(f"server {server} added successfully!")

    def removeServer(self, server: str):
        if(server not in self.serverConnections):
            print(f"server {server} not present...")
            return
        # self.serverConnections.pop(server)
        del self.serverConnections[server]
        print(f"server {server} removed successfully!")

    def getServerWithLeastConnection(self)-> str:
        minConnections = self.maxConnections + 1 
        min_conn_server = None
        for server, conn in self.serverConnections.items():
            if(conn < minConnections):
                minConnections = conn
                min_conn_server = server
        if(minConnections == self.maxConnections):
            print(f"All the servers reached there maximum connections, please try again after sometime...")
            return
        if(min_conn_server != None):
            self.serverConnections[min_conn_server] += 1 # add the connection to the server...
        return min_conn_server


def leastConnectionExample():
    load_balancer = LeastConnectionLoadBalancer()
    load_balancer.addServer("server 1") 
    load_balancer.addServer("server 1") 
    # load_balancer.removeServer("server 1")
    load_balancer.addServer("server 2") 
    load_balancer.addServer("server 3") 

    for i in range(10):
        selectedServer = load_balancer.getServerWithLeastConnection()
        print(f"Request {i} routed to server {selectedServer}")

if __name__ == "__main__":
    leastConnectionExample()



import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class LeastConnectionLoadBalancer {
	private Map<String, Integer> serverConnections;

	public LeastConnectionLoadBalancer() {
		this.serverConnections = new HashMap<>();
	}

	public void addServer(String serverName) {
		// Add a server to the load balancer with 0 initial connections
		serverConnections.put(serverName, 0);
	}

	public String getServerWithLeastConnections() {
		// Find the server with the least active connections
		int minConnections = Integer.MAX_VALUE;
		String selectedServer = null;

		for (Map.Entry<String, Integer> entry : serverConnections.entrySet()) {
			if (entry.getValue() < minConnections) {
				minConnections = entry.getValue();
				selectedServer = entry.getKey();
			}
		}

		// Increment the connection count for the selected server
		if (selectedServer != null) {
			serverConnections.put(selectedServer, minConnections + 1);
		}

		return selectedServer;
	}
}

public class LeastConnectionLoadBalancerExample {
	public static void main(String[] args) {
		// Create a Least Connection load balancer
		LeastConnectionLoadBalancer loadBalancer = new LeastConnectionLoadBalancer();

		// Add servers to the load balancer
		loadBalancer.addServer("Server1");
		loadBalancer.addServer("Server2");
		loadBalancer.addServer("Server3");

		// Simulate requests and print the server to which each request is routed
		for (int i = 0; i < 10; i++) {
			String selectedServer = loadBalancer.getServerWithLeastConnections();
			System.out.println("Request " + (i + 1) + ": Routed to " + selectedServer);
		}
	}
}

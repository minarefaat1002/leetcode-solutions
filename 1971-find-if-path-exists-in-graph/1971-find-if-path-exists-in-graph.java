import java.util.*;

class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        HashMap<Integer,List<Integer>> graph = new HashMap<>();
        HashSet<Integer> visited = new HashSet<>();
        for( int[] edge : edges ){
            if(!graph.containsKey(edge[0])) graph.put(edge[0], new ArrayList<>());
            if(!graph.containsKey(edge[1])) graph.put(edge[1],new ArrayList<>());
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        return dfs(source,graph,destination,visited);
    }
    public boolean dfs(int vertex,HashMap<Integer,List<Integer>> graph,int destination,HashSet<Integer> visited){
        if(vertex == destination) return true;
        if(visited.contains(vertex)) return false;
        visited.add(vertex);
        for(int neighbour:graph.get(vertex)){
            if(dfs(neighbour,graph,destination,visited)) return true;
        }
        return false;
    }
}
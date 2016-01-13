
public class CoBFS {
	Digraph dg;
	private boolean[] marked;  // is there a path from sources to marked[i]
	private int[] distTo;      // distnace from sources to distTo[i]
	
	Queue<Integer> q;          // vertices to visit
	
	
	public CoBFS(Digraph G)
	{
		dg = G;
		marked = new boolean[G.V()];
		distTo = new int[G.V()];		
	}
	
	// init search with the list of source nodes
	public void startSearchFrom(Iterable<Integer> sources) {
		
		for(int v=0; v < distTo.length; v++) distTo[v] = Integer.MAX_VALUE;
		for(int v=0; v < distTo.length; v++) marked[v] = false;
		
		q= new Queue<Integer>();
		for (int s: sources) {
			marked[s]=true;
			distTo[s]=0;
			q.enqueue(s);
		}
	
	}
	
	public void startSearchFrom(int s) {
		
		for(int v=0; v < distTo.length; v++) distTo[v] = Integer.MAX_VALUE;
		for(int v=0; v < distTo.length; v++) marked[v] = false;
		
		q= new Queue<Integer>();
		
		marked[s]=true;	
		distTo[s]=0;
		q.enqueue(s);

	
	}
	
	// are there more vertices to visit?
	public boolean canContinueSearch() 
	{
		return !q.isEmpty();
	}
	
	public int getNext() {
		return q.dequeue();
	}
	
	// take next vertex to visit and extract all adjacent vertices
	// return the vertex visited
	public void continueSearch(int next) {
		
		for (int v : dg.adj(next)) {
			if (!marked[v]) {
				marked[v] = true;
				distTo[v] = distTo[next] + 1;
				q.enqueue(v);
			}
		}
				
	}	

	// have we reached ant of the destinations?
	public boolean isMarked(int d) {		
		return marked[d];
	}
	
	// what is the closer destination?
	public int distTo(int d) {		
		return distTo[d];
	}

	

}

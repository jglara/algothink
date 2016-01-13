


public class SAP {
	private Digraph dg;
	private CoBFS bfs1 ;		
	private CoBFS bfs2 ;
	
	// constructor takes a digraph (not necessarily a DAG) ...
	public SAP(Digraph G)
	{		
		if (G == null) throw new java.lang.NullPointerException();
		
		dg = new Digraph(G);
		bfs1 = new CoBFS(dg);		
		bfs2 = new CoBFS(dg);
		
	}

	// length of shortest ancestral path between v and w; -1 if no such path...
	public int length(int v, int w)
	{		
		if (v >= dg.V() || w>= dg.V()) throw new java.lang.IndexOutOfBoundsException();
		
		int ancestor = ancestor(v,w);
		
		if (ancestor != -1) {
			return bfs1.distTo(ancestor) + bfs2.distTo(ancestor);			
		} else {
			return -1; 
		}
	}
	
	private int runAncestorSearch()
	{
		int ancestor = -1;
		int ancestorLength = Integer.MAX_VALUE;
		while (bfs1.canContinueSearch() || bfs2.canContinueSearch()) {
			if (bfs1.canContinueSearch()) {
				int visited = bfs1.getNext();
				
				
				if (bfs2.isMarked(visited)) {					
					int visitedLength = bfs1.distTo(visited) + bfs2.distTo(visited);					
					if (visitedLength < ancestorLength) {
						ancestor = visited;
						ancestorLength = visitedLength;
					}
				} 
					
				if (bfs1.distTo(visited) < ancestorLength) {
					bfs1.continueSearch(visited);
				}

				
				
			}
			
			if (bfs2.canContinueSearch()) {
				int visited = bfs2.getNext();				
				
				
				if (bfs1.isMarked(visited)) {
					int visitedLength = bfs1.distTo(visited) + bfs2.distTo(visited);
					if (visitedLength < ancestorLength) {
						ancestor = visited;
						ancestorLength = visitedLength;
					}					
				} 
				
				if (bfs2.distTo(visited) < ancestorLength) {
					bfs2.continueSearch(visited);
				}

			}			
		}
		
		return ancestor;

	}

	// a common ancestor of v and w that participates in a shortest ancestral path; -1 if no such path
	public int ancestor(int v, int w)
	{		
		if (v >= dg.V() || w>= dg.V()) throw new java.lang.IndexOutOfBoundsException();
		
		bfs1.startSearchFrom(v);
		bfs2.startSearchFrom(w);		
				
		return runAncestorSearch();
		
	}

	// length of shortest ancestral path between any vertex in v and any vertex in w; -1 if no such path
	public int length(Iterable<Integer> v, Iterable<Integer> w)
	{
		int ancestor = ancestor(v,w);

		if (ancestor != -1) {
			return bfs1.distTo(ancestor) + bfs2.distTo(ancestor);			
		} else {
			return -1; 
		}
	}

	// a common ancestor that participates in shortest ancestral path; -1 if no such path
	public int ancestor(Iterable<Integer> v, Iterable<Integer> w)
	{
		for (int i: v) {
			if (i >= dg.V()) throw new java.lang.IndexOutOfBoundsException();
		}
		
		for (int i: w) {
			if (i >= dg.V()) throw new java.lang.IndexOutOfBoundsException();
		}
		
		bfs1.startSearchFrom(v);
		bfs2.startSearchFrom(w);
		
		return runAncestorSearch();
		
	}

	public static void main(String[] args) {
		In in = new In(args[0]);
	    Digraph G = new Digraph(in);
	    SAP sap = new SAP(G);
	    while (!StdIn.isEmpty()) {
	        int v = StdIn.readInt();
	        int w = StdIn.readInt();
	        int length   = sap.length(v, w);
	        int ancestor = sap.ancestor(v, w);
	        StdOut.printf("length = %d, ancestor = %d\n", length, ancestor);
	    }
	}

}

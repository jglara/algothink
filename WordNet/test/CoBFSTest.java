import static org.junit.Assert.*;

import org.junit.Test;


public class CoBFSTest {
	private String dag1 = "/home/ejogarv/git/algoii/WordNet/data/digraph1.txt";
	//private String dag2 = "/home/ejogarv/git/algoii/WordNet/data/digraph2.txt";
	

	@Test
	public void testSearch1() {	
		Digraph dg = new Digraph(new In(dag1));
		
		CoBFS bfs1 = new CoBFS(dg);		
		
		bfs1.startSearchFrom(3);
		
		while (bfs1.canContinueSearch()) {
			if (bfs1.isMarked(1)) break;
			bfs1.continueSearch(bfs1.getNext());
			
		}
		
		assertTrue(bfs1.isMarked(1));
		assertTrue(bfs1.distTo(1) == 1);
	}
	
	@Test
	public void testSearch2() {	
		Digraph dg = new Digraph(new In(dag1));
		
		CoBFS bfs1 = new CoBFS(dg);		
		
		bfs1.startSearchFrom(11);
		
		while (bfs1.canContinueSearch()) {
			if (bfs1.isMarked(1)) break;
			bfs1.continueSearch(bfs1.getNext());
			
		}
		
		assertTrue(bfs1.isMarked(1));
		assertTrue(bfs1.distTo(1) == 3);
	}
	
	@Test
	public void testSearch3() {
		Digraph dg = new Digraph(new In(dag1));
		
		CoBFS bfs1 = new CoBFS(dg);		
		CoBFS bfs2 = new CoBFS(dg);
		bfs1.startSearchFrom(3);
		bfs2.startSearchFrom(11);
		
		int ancestor = -1;
		while (bfs1.canContinueSearch() || bfs2.canContinueSearch()) {
			if (bfs1.canContinueSearch()) {
				int visited = bfs1.getNext();
				bfs1.continueSearch(visited);
				
				if (bfs2.isMarked(visited)) {
					ancestor = visited;
					break;
				}
			}
			
			if (bfs2.canContinueSearch()) {
				int visited= bfs2.getNext();
				bfs2.continueSearch(visited);
				
				if (bfs1.isMarked(visited)) {
					ancestor = visited;
					break;
				}
			}
			
		}
		
		assertTrue(ancestor == 1);
		assertTrue(bfs1.distTo(ancestor) == 1);
		assertTrue(bfs2.distTo(ancestor) == 3);
		
	}
}

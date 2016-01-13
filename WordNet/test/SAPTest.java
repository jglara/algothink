import static org.junit.Assert.*;

import org.junit.Test;

// Test SAP class
public class SAPTest {
	private String dag1 = "/home/ejogarv/git/algoii/WordNet/data/digraph1.txt";
	private String dag2 = "/home/ejogarv/git/algoii/WordNet/data/digraph2.txt";
	private String dag3 = "/home/ejogarv/git/algoii/WordNet/data/digraph3.txt";
	private String dag9 = "/home/ejogarv/git/algoii/WordNet/data/digraph9.txt";
	

	@Test
	public void testLengthIntInt() {
		Digraph dg = new Digraph(new In(dag1));
		SAP sap = new SAP(dg);
		
		assertEquals(4,sap.length(3, 11));		
		
		Digraph dg2 = new Digraph(new In(dag2));
		SAP sap2 = new SAP(dg2);
		
		assertEquals(2,sap2.length(3, 1));
	}
	
	@Test
	public void testLength3() {
		Digraph dg = new Digraph(new In(dag3));
		SAP sap = new SAP(dg);
		
								
		assertEquals(4,sap.length(12, 13));
	}

	@Test
	public void testAncestorIntInt() {
		Digraph dg = new Digraph(new In(dag1));
		
		SAP sap = new SAP(dg);
		
		assertEquals(1,sap.ancestor(3, 11));
		
		Digraph dg2 = new Digraph(new In(dag2));
		SAP sap2 = new SAP(dg2);
		
		assertEquals(3,sap2.ancestor(3, 1));
		
	}
	
	@Test
	public void testDigraph9() {
		Digraph dg = new Digraph(new In(dag9));
		
		SAP sap = new SAP(dg);
			
		
		assertEquals(4,sap.ancestor(7, 4));
		
	}

}

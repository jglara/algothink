import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;


public class WordNet {
	private HashMap<String, List<Integer>> nounSynsetMap = new HashMap<String, List<Integer>>();
	private HashMap<Integer, String> synsetMap = new HashMap<Integer, String>();
	private Digraph hypernyms;
	private SAP sap;

	// constructor takes the name of the two input files ...
	public WordNet(String synsetsFile, String hypernymsFile) {
		if ((synsetsFile == null) || (hypernymsFile == null)) throw new java.lang.NullPointerException();
		
		In in = new In(synsetsFile);
		
		int synsetsCount = 0;
		
		// Read all the synsets and store nouns in a map
		while (!in.isEmpty()) {
			String line = in.readLine();
			String[] fields = line.split(",");
			
			// read the synsetId
			Integer synsetId = Integer.parseInt(fields[0]);
			
			synsetMap.put(synsetId, fields[1]);
			
			// read the nouns related
			String[] nouns = fields[1].split(" ");
			
			for (int i=0; i< nouns.length; i++) {
				
				List<Integer> list = nounSynsetMap.get(nouns[i]);
				if (list == null) {
					nounSynsetMap.put(nouns[i], list = new ArrayList<Integer>());
				}
				list.add(synsetId);
				
			}
			
			synsetsCount ++; // each line is a synset
		}
		
		// Create a Digraph for hypernyms. vertices are the synsets
		hypernyms = new Digraph(synsetsCount);
		
		in = new In(hypernymsFile);
		while(!in.isEmpty()) {
			String line = in.readLine();
			
			String[] synsets = line.split(",");
			
			// add all the edges
			int fromEdge = Integer.parseInt(synsets[0]);
			for (int i =1; i < synsets.length; i++) {
				hypernyms.addEdge(fromEdge, Integer.parseInt(synsets[i]));
			}
		}
		
		// check it is a DAG
		Topological topo = new Topological(hypernyms);
		if (topo.hasOrder()) throw new java.lang.IllegalArgumentException();		
		
		sap = new SAP(hypernyms);
		
	}

	// returns all WordNet nouns
	public Iterable<String> nouns() {
		return nounSynsetMap.keySet();
	}

	// is the word a WordNet noun?
	public boolean isNoun(String word) {
		if (word == null) throw new java.lang.NullPointerException();
		return nounSynsetMap.containsKey(word);
	}

	// distance between nounA and nounB (defined below)
	public int distance(String nounA, String nounB) {
		if (!isNoun(nounA) || !isNoun(nounB)) throw new java.lang.IllegalArgumentException();
		
		List<Integer> synsetsA = nounSynsetMap.get(nounA);
		List<Integer> synsetsB = nounSynsetMap.get(nounB);
		
		return sap.length(synsetsA, synsetsB);
	}

	// a synset (second field of synsets.txt) that is the common ancestor of nounA and nounB
	// in a shortest ancestral path (defined below)
	public String sap(String nounA, String nounB)
	{
		if (!isNoun(nounA) || !isNoun(nounB)) throw new java.lang.IllegalArgumentException();
		
		List<Integer> synsetsA = nounSynsetMap.get(nounA);
		List<Integer> synsetsB = nounSynsetMap.get(nounB);
		
		int ancestor = sap.ancestor(synsetsA, synsetsB);
		
		return synsetMap.get(ancestor);
	}

	public static void main(String[] args) {
		WordNet wnet = new WordNet(args[0], args[1]);
			
		while (!StdIn.isEmpty()) {
	        String noun1 = StdIn.readString();
	        String noun2 = StdIn.readString();
	        String sap = wnet.sap(noun1, noun2);
	        int distance = wnet.distance(noun1, noun2);
	        	        
	        StdOut.printf("sap = %s. distance = %d\n", sap, distance);
	    }
	}
}

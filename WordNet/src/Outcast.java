
public class Outcast {
	private WordNet wnet;

	// constructor takes a WordNet object
	public Outcast(WordNet wordnet) {
		if(wordnet == null) throw new java.lang.NullPointerException();
		wnet = wordnet;

	}

	// constructor takes a WordNet object
	public String outcast(String[] nouns) {
		
		int[] distances = new int[nouns.length];
		for (int n=0; n<nouns.length; n++) {
			distances[n] = 0;
		}		
		
		for (int n=0; n<nouns.length; n++) {
			
			for (int m=0; m<nouns.length; m++) {
				distances[n] += wnet.distance(nouns[n], nouns[m]);
			}
			
		}
		
		// find the outcast
		int max=-1;
		String outcast="";
		for (int n=0; n<nouns.length; n++) {
			if (distances[n]>max) {
				max = distances[n];
				outcast = nouns[n];
			}
			
		}	
		return outcast;

	}


	public static void main(String[] args)  {
		WordNet wordnet = new WordNet(args[0], args[1]);
		Outcast outcast = new Outcast(wordnet);
		for (int t = 2; t < args.length; t++) {
			In in = new In(args[t]);
			String[] nouns = in.readAllStrings();
			StdOut.println(args[t] + ": " + outcast.outcast(nouns));
		}
	}

}

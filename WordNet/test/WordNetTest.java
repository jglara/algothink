import static org.junit.Assert.*;

import org.junit.Test;


public class WordNetTest {
	private String synsetsFile = "/home/ejogarv/git/algoii/WordNet/data/synsets.txt";
	private String hypernymsFile = "/home/ejogarv/git/algoii/WordNet/data/hypernyms.txt";

	@SuppressWarnings("unused")
	@Test
	public void testNouns() {
		WordNet wnet = new WordNet(synsetsFile, hypernymsFile);
		
		int count = 0;
		for (String noun : wnet.nouns()) {
			count ++;			
		}
		
		//System.out.println(count);
		assertEquals(119188, count);
		
	}

	@Test
	public void testIsNoun() {
		WordNet wnet = new WordNet(synsetsFile, hypernymsFile);
		
		assertTrue(wnet.isNoun("zucchini"));
		assertFalse(wnet.isNoun("cacaDeLaVaca"));
	}

}

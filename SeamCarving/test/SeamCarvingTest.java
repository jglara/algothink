import static org.junit.Assert.*;

import org.junit.Test;


public class SeamCarvingTest {
	String picture_1 = "/home/ejogarv/git/algoii/SeamCarving/data/3x7.png";
	String picture_2 = "/home/ejogarv/git/algoii/SeamCarving/data/6x5.png";
	String picture_3 = "/home/ejogarv/git/algoii/SeamCarving/data/4x6.png";
	
	
	@Test
	public void testEnergy() {
		Picture p = new Picture(picture_1);
		
		
		SeamCarver sc = new SeamCarver(p);
		double e = sc.energy(1,1);
		assertEquals(e, 86627.0, 0.1);
		
	}

	@Test
	public void testFindVerticalSeam() {
		
		Picture p = new Picture(picture_1);
		
		SeamCarver sc = new SeamCarver(p);
		
		int []seam =sc.findVerticalSeam();
		
		int []expected = {0,1,1,1,1,1,2};
		
		for (int i=0; i<expected.length; i++) {
			assertEquals(expected[i], seam[i]);
		}
		
		
	}
	
	
	@Test
	public void testEnergy_6_5() {
		
		Picture p = new Picture(picture_2);
		
		SeamCarver sc = new SeamCarver(p);
		
		double e = sc.energy(2, 1);
		assertEquals(51304.0, e, 0.1);	
		
		e= sc.energy(1,2);
		assertEquals(47908.0, e, 0.1);
		
	}
	
	@Test
	public void testEnergy_4_6() {
		
		Picture p = new Picture(picture_3);
		
		SeamCarver sc = new SeamCarver(p);
		
		double e = sc.energy(2, 1);
		assertEquals(30003.0, e, 0.1);		
		
	}
	
	@Test
	public void testFindHorizontalSeam() {
		
		Picture p = new Picture(picture_1);
		
		SeamCarver sc = new SeamCarver(p);
		
		int []seam =sc.findHorizontalSeam();
		
		int []expected = {3,2,1};
		
		for (int i=0; i<expected.length; i++) {
			assertEquals(expected[i], seam[i]);
		}
		
		
	}
	
//	@Test
//	public void testFindHorizontalSeam_6_5() {
//		
//		Picture p = new Picture(picture_2);
//		
//		SeamCarver sc = new SeamCarver(p);
//		sc.transposePciture();
//		
//		int []seam =sc.findHorizontalSeam();
//		
//		int []expected = {2,3,3,3,4};
//		
//		for (int i=0; i<expected.length; i++) {
//			assertEquals(expected[i], seam[i]);
//		}
//		
//		
//	}
	
	@Test
	public void testFindVerticalSeam_6_5() {
		
		Picture p = new Picture(picture_2);
		
		SeamCarver sc = new SeamCarver(p);
		
		int []seam =sc.findVerticalSeam();
		
		int []expected = {2,3,3,3,4};
		
		for (int i=0; i<expected.length; i++) {
			assertEquals(expected[i], seam[i]);
		}
		
		
	}
	
	@Test
	public void testRemoveVerticalSeam_6_5() {
		
		Picture p = new Picture(picture_2);
		
		SeamCarver sc = new SeamCarver(p);
		
		int []seam =sc.findVerticalSeam();
		
		int []expected = {2,3,3,3,4};
		
		for (int i=0; i<expected.length; i++) {
			assertEquals(expected[i], seam[i]);
		}
		
		sc.removeVerticalSeam(seam);
		
		assertEquals(6,sc.width());
		assertEquals(5,sc.height());
		
		assertEquals(205,sc.picture().get(3, 1).getRed());
		
		
	}

}

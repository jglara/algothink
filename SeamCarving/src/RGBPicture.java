import java.awt.Color;


public class RGBPicture {
	private int width;
	private int height;
	boolean isVertical;
	
	private class RGBColor {
		private final int red;
		private final int green;
		private final int blue;
		
		RGBColor(int r, int g, int b)
		{
			red=r;
			green=g;
			blue=b;			
		}
		
		int getRed() { return red;}
		int getGreen() {return green;}
		int getBlue() {return blue;}				
	}
	
	private RGBColor [][]colors;
	
	public RGBPicture(Picture picture)                
	{		
		
		width = picture.width();
		height= picture.height();
		colors = new RGBColor[height][width];
		isVertical = true;
		
		for (int row=0; row<picture.height();row++) {
			for (int col=0; col<picture.width(); col++) {
				colors[row][col]= new RGBColor(picture.get(col, row).getRed()
						,picture.get(col, row).getGreen()
						,picture.get(col, row).getBlue());
			}
		}
		 
	}
	
	public Picture getPicture()
	{
		Picture newPicture = new Picture(width(), height());
		for (int row=0; row<height();row++) {
			for (int col=0; col<width(); col++) {			
					newPicture.set(col, row, new Color(getRed(col,row),getGreen(col,row),getBlue(col,row)));
			}
		}
		
		return newPicture;
	}
	
	private RGBPicture(int h, int w) {
		width = w;
		height= h;
		colors = new RGBColor[height][width];
		
		
	}

	public RGBPicture transpose()                
	{		
		RGBPicture p = new RGBPicture(width, height);
		if (isVertical) {
			p.isVertical = false;

			for (int row=0; row<height();row++) {
				for (int col=0; col<width(); col++) {
					p.colors[col][row]= new RGBColor(colors[row][col].getRed(),
							colors[row][col].getGreen(),
							colors[row][col].getBlue());
				}
			}
		} else {
			p.isVertical = true;
			for (int col=0; col<width();col++) {
				for (int row=0; row<height(); row++) {
					p.colors[row][col]= new RGBColor(colors[col][row].getRed(),
							colors[col][row].getGreen(),
							colors[col][row].getBlue());
				}
			}
			
		}

		return p;		
	}
	
	public boolean isVertical() {
		return isVertical;
	}
	
	public void removeVerticalSeam(int[] seam)
	{
		if ((width() < 2) && (seam.length != width())) {
			throw new IllegalArgumentException();
		}
		
		for (int i=0; i<seam.length; i++) {
			if ((seam[i] <0) || (seam[i]>width()-1)) {
				throw new IllegalArgumentException();
			}
			
			if (i>0) {
				int diff =(seam[i] - seam[i-1]); 
				if ((diff > 1) || (diff < -1)) {
					throw new IllegalArgumentException();
				}
			}
		}
		
		
		for (int row=0; row<height();row++) {
			System.arraycopy(colors[row], seam[row]+1, colors[row], seam[row], width-seam[row]-1);
		}
		
	}

	// width of current picture
	public int width()     
	{
		return width;
	}

	// height of current picture
	public int height()
	{
		return height;
	}
	
	public int getRed(int col,int row) {
		return colors[row][col].getRed();
	}
	
	public int getBlue(int col,int row) {
		return colors[row][col].getBlue();
	}
	
	public int getGreen( int col,int row) {
		return colors[row][col].getGreen();
	}
	
	
	

}

public class SeamCarver {	
	
	private RGBPicture pict;
	
	// create a seam carver object based on the given picture
	public SeamCarver(Picture picture)                
	{		
		
		pict = new RGBPicture(picture);
		
	}
	
    // current picture
	public Picture picture()
	{
		return pict.getPicture();
	}
	
	// width of current picture
	public     int width()     
	{
		return pict.width();
	}
	
    // height of current picture
	public     int height()
	{
		return pict.height();
	}
	
	// energy of pixel at column x and row y
	public  double energy(int col, int row)     
	{
		if ((row < 0) || (row>height()-1 || col <0 || col > width()-1)) {
			throw new IndexOutOfBoundsException();
		}
			
		double []delta = new double[6];
		
		if ( (row>0) && (row+1<height()) && (col>0) && (col+1<width())) {
			delta[0] = getRed(col, row-1) - getRed(col, row+1);
			delta[1] = getGreen(col, row-1) - getGreen(col, row+1);
			delta[2] = getBlue(col, row-1) - getBlue(col, row+1);
			
			delta[3] = getRed(col-1, row) - getRed(col+1, row);
			delta[4] = getGreen(col-1, row) - getGreen(col+1, row);
			delta[5] = getBlue(col-1, row) - getBlue(col+1, row);
		} else {
			return 195075.0;
		}
			
		
		double energy=0;
		for (int i=0; i<6; i++) {
			energy += delta[i] * delta[i];
		}
		
		return energy;
		
	}
	
	private int getRed(int col, int row) {
		return pict.getRed(col, row);
	}
	
	private int getBlue(int col, int row) {
		return pict.getBlue(col, row);
	}
	
	private int getGreen(int col, int row) {
		return pict.getGreen(col, row);
	}
	private int getRow(int vertex) {
		return vertex / width();
	}
	private int getCol(int vertex) {
		return vertex % width();
	}
	
	private int getVertexNum(int col, int row) {
		return ((width()*row) + col);
	}
	
	private int getInitialVertexNum() {
		return (width() * height());
	}
	
	private int getFinalVertexNum() {
		return (width() * height())+1;
	}
	
	
    // sequence of indices for horizontal seam
	public int[] findVerticalSeam() 
	{
		if (!pict.isVertical()) {
			pict = pict.transpose();
		}
		
		return privfindVerticalSeam();
	}
	
	 // sequence of indices for horizontal seam
	private int[] privfindVerticalSeam() 	{
		int numVertex = width() * height()+2;
		IndexMinPQ<Double> pq = new IndexMinPQ<Double>(numVertex);
		int []edgeTo = new int[numVertex];
		double []dist = new double[numVertex];
		
		// set the distance to infinity
		for (int v=0; v<numVertex; v++){
			dist[v] = Double.POSITIVE_INFINITY;
		}
		int initialV = getInitialVertexNum(); 
		dist[initialV] = 0.0;
		
		// insert first row
		for (int col=0; col<width(); col++) {
			int v= getVertexNum(col, 0);
			pq.insert(v, energy(col, 0));
			dist[v] = 0;
			edgeTo[v] = initialV; 
		}
		
		// extract from the PQ, and relax each edge
		while(!pq.isEmpty()) {
			int v = pq.delMin();
			
			for (DirectedEdge e: getVerticalAdj(v)) {
				// relax edge v -> adjUp (energy)
				if (dist[e.to()] > dist[e.from()] + e.weight()) { // found a shortest path to e.to()
					dist[e.to()] = dist[e.from()] + e.weight();
					edgeTo[e.to()] = e.from();
					if (pq.contains(e.to())) {
						pq.decreaseKey(e.to(), dist[e.to()]);
					} else {
						pq.insert(e.to(), dist[e.to()]);
					}
				}				
			}			
		}
		
		// now get back from latest vertex to initial vertex
		int []seam = new int[height()];
		int v=getFinalVertexNum();
		for(int i = seam.length-1; i >=0; i--) {
			seam[i]=getCol(edgeTo[v]);
			v = edgeTo[v];
		}
		return seam;
				
		
	}
	
	private Iterable<DirectedEdge> getVerticalAdj(int v)
	{
		Queue<DirectedEdge> q = new Queue<DirectedEdge>();
		int vCol = getCol(v);
		int vRow = getRow(v);
		
		if (v == getFinalVertexNum()) {
			return q;
		} else if (v == getInitialVertexNum()) {
			return q;
		}
		
		if (vRow == height()-1) {
			// To the final vertex
			q.enqueue(new DirectedEdge(v, getFinalVertexNum(), 0.0));
		} else {
			
			if (vCol > 0) {
				int adjLeft = getVertexNum(vCol-1, vRow+1);
				double energyLeft = energy(vCol-1, vRow+1);
				q.enqueue(new DirectedEdge(v, adjLeft, energyLeft));
			}
			
			int adjCenter = getVertexNum(vCol, vRow+1);
			double energyCenter = energy(vCol, vRow+1);
			q.enqueue(new DirectedEdge(v,adjCenter, energyCenter));			
			
			if (vCol+1 < width()){
				int adjRight = getVertexNum(vCol+1, vRow+1);
				double energyRight = energy(vCol+1, vRow+1);
				q.enqueue(new DirectedEdge(v, adjRight, energyRight));
			}
			
		}
		
		return q;
	}
	
	
    // sequence of indices for vertical seam
	public int[] findHorizontalSeam()
	{
		
		if (pict.isVertical()) {
			pict = pict.transpose();
		}
		
		return privfindVerticalSeam();
	}
	
	// remove horizontal seam from current picture	
	public void removeHorizontalSeam(int[] seam)
	{
		if( seam == null ) {
			throw new IllegalArgumentException();
		}
		
		if (pict.isVertical()) {
			pict = pict.transpose();
		}
		
		removeVerticalSeam(seam);
		
	}
	
    // remove vertical seam from current picture
	public void removeVerticalSeam(int[] seam)
	{
		if( seam == null ) {
			throw new IllegalArgumentException();
		}
		
		if (!pict.isVertical()) {
			pict = pict.transpose();
		}
		pict.removeVerticalSeam(seam);
		
	}
}


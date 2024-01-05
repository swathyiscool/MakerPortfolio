/**
 * <pre>
 * Name: Saraswathy Amjith
 * Mrs. Kankelborg
 * Period 1
 * Project 2 Recursive Art Project Part 3: Art
 * Revision History:
 *
 * Class Description:
 * The following code uses:
 *  Use different parameters than Sierpinski (int n, double x, double y, double width, double length)). 
 *  Use different StdDraw methods than Sierpinski (ellipses and circles))
 *  Use recursive level for secondary purpose ( level dictates shirt color)
 */

public class Art
{
   /**
	* All other functions other than draw must be private.
	* You must have at least 2 other methods besides draw.
	* You may not alter the header of this method.
	*/
	
	/** 
	 * Takes an integer parameter of n then calls the recursive version of draw
     * of order n that fits a family of n humans into the frame. 
     */
	public static void draw(int n) {
		
		StdDraw.setYscale(0,100); // changes y scale
		StdDraw.setXscale(0,100); // changes x scale
		StdDraw.setPenColor(225, 233, 245); // sets background color
		StdDraw.filledRectangle(50,50,50,50); // creates a light blue background
		drawhelper(n,50,50,8,16); // calls the drawhelper method (the recursive method)
		
	}
		
    /**
     * Draws a family of order n, such that the largest human
     * is centered at (x, y) and is the specified width and length .
     */
	private static void drawhelper(int n, double x, double y, double width, double length) {
		
		if (n == 0) { // base case so that it will end recursion once n is 0
			
			return;
			
		} else { // recursive case
		
		// draws a human using n for color, x, y, width, length
		drawhuman(n,x,y,width,length); 
		// calls the recursive method for a smaller human to the right 
		drawhelper(n-1, x+width*2, y-length*0.8,width/1.4,length/1.4); 
		// calls the recursive method for a smaller human to the left 
		drawhelper(n-1, x-width*2, y-length*0.8,width/1.4,length/1.4); 
		
		}
		
	}
	/**
    * Draws a human  centered at (x, y) and is the specified width and length, with 
    * color of clothes depending on n.
    */
	private static void drawhuman(int n, double x, double y, double width, double length) {
		
		drawhair(x,y,width,length); // calls function to draw hair
		
		setclothescolor(n); // sets pen color for clothing
		StdDraw.filledEllipse(x,y,width,length); // creates the body ellipse
		
		drawface(x,y,width,length); // calls function to draw face
		
		// sets color to jean color blue and draws rectangle + thinner rectangle with 
		// with bg color to create illusion of pants.
		
	    StdDraw.setPenColor(37, 58, 89); 
	    StdDraw.filledRectangle(x, y-length*0.65, width*0.95, length/1.75);
	    StdDraw.setPenColor(225, 233, 245);
	    StdDraw.filledRectangle(x, y-length*0.85, width*0.05, length/2);
	    
	    // creates an array of x and y values for the hair tie polygons
	    double[] hairtiexcoords = {x+.8*width, x+.8*width+length/3, x+.8*width, x+.8*width+length/3};
	    double[] hairtieycoords = {y+length,y+length*1.4 ,y+length*1.4, y+length};
	    double[] hairtiexcoords2 = {x-1.2*width, x-1.2*width+length/3, x-1.2*width, x-1.2*width+length/3};
	    
	    // sets the clothescolor based on the recusion level value
		setclothescolor(n);
	   
		// draws two squares for the t shirt shoulders
	    StdDraw.filledSquare(x+width,y+length*.4, width/3);
	    StdDraw.filledSquare(x-width,y+length*.4, width/3);
	    
	    // draws the hair tie polygons
	    StdDraw.filledPolygon(hairtiexcoords, hairtieycoords);
	    StdDraw.filledPolygon(hairtiexcoords2, hairtieycoords);
	    
	    
	    
	}
	/**
	    * Draws hair of a human centered at (x, y) and is the specified width and length
	    */
	private static void drawhair(double x, double y, double width, double length) {

		int[] haircol = sethaircolor(); // gets a array of the rgb values of hair color randomly
		StdDraw.setPenColor(haircol[0], haircol[1], haircol[2]); // sets the pen color to above values^
		
		// rectangle for the bottom part of hair and a ellipse for top curved hair
		StdDraw.filledEllipse(x,y+length*1.2, width*1.3, width*1.2); 
		StdDraw.filledRectangle(x, y+length*0.8, width*1.3, width*0.75); 
		
	}
	/**
	    * Draws the face of a human centered at (x, y) and is the specified width and length
	    */
	private static void drawface(double x, double y, double width, double length) {
		// randomly gets the skin color
		int[] skincol = setskincolor();
		
		// creates the base face ellipse
		StdDraw.setPenColor(skincol[0], skincol[1], skincol[2]);
		StdDraw.filledEllipse(x,y+length,width,length/2);
		// draws the mouth circle
	    StdDraw.setPenColor(StdDraw.BLACK);
	    StdDraw.filledCircle(x, y+length*0.8, width/4);
	    // covers up half the mouth circle with a rectangle
	    StdDraw.setPenColor(skincol[0], skincol[1], skincol[2]);
	    StdDraw.filledRectangle(x, y+length*0.9, width/4, width/8);

	    // draws the eyes as points 
	    StdDraw.setPenColor(StdDraw.BLACK);
	    StdDraw.setPenRadius(0.002 * width);
	    StdDraw.point(x+width/2.7, y+length*1.1);
	    StdDraw.point(x-width/2.7, y+length*1.1);
	    
	    // draws two ellipses for the blush
	    StdDraw.setPenColor(235, 185, 217);
	    StdDraw.filledCircle(x+width/1.8, y+length*0.9,width/5);
	    StdDraw.filledCircle(x-width/1.8, y+length*0.9,width/5);
	    
	}
	/**
	    * returns a int array of rgb values for a  randomly selected skin color. 
	    */
	private static int[] setskincolor() {
		// set rgb values for a variety of skin colors in 
		// red, green, blue value arrays 
		int[] red = {163,222,102};
		int[] green = {108,182,47};
		int[] blue = {72,155,10};
		// randomly selects a number from 0,2 for the index of array
		int co = (int) (Math.floor(Math.random() * 3) );
		// creates an array with the randomly selected index values and returns it
		int[] colors = {red[co], green[co], blue[co]};
		return colors;
	}
	
	/**
	    * returns a int array of rgb values for a randomly selected hair color. 
	    */
	private static int[] sethaircolor() {
		// set rgb values for a variety of hair colors in 
		// red, green, blue value arrays 
		int[] red = {122, 46, 8, 176};
		int[] green = {44, 11, 2, 147};
		int[] blue = {27, 3, 1 , 97};
		// randomly selects a number from 0,3 for the index of array
		int co = (int) (Math.floor(Math.random() * 3));
		// creates an array with the randomly selected index values and returns it
		int[] colors = {red[co], green[co], blue[co]};
		return colors;
	}
	
	/**
	    * returns a int array of rgb values for a clothing color selected based on n. 
	    */
	private static void setclothescolor(int n) {
		// set rgb values for a variety of t shirt colors in 
		// red, green, blue value arrays 
		int[] red = {235, 123, 217, 84, 151, 151};
		int[] green = {73, 59, 100, 100, 204, 204};
		int[] blue = {116, 179, 197, 209, 153, 153};
		// assigns a color based on the n value 
		StdDraw.setPenColor(red[n%6],green[n%6], blue[n%6]);
	}
}

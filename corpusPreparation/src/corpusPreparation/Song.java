package corpusPreparation;

public class Song {
	
	// some metadata
	private String title;
	private int number_of_parts;
	private String key;
	private String album;
	private String author;
	private String date;
	
	// tonal step values
	private double i;
	private double ix;
	private double ii;
	private double iix;
	private double iii;
	private double iv;
	private double ivx;
	private double v;
	private double vx;
	private double vi;
	private double vix;
	private double vii;
	
	// chord step values
	private String ci;
	private String cix;
	private String cii;
	private String ciix;
	private String ciii;
	private String civ;
	private String civx;
	private String cv;
	private String cvx;
	private String cvi;
	private String cvix;
	private String cvii;
	
	public Song(String title, String album, String author, String date){
		
		this.title = title;
		this.album = album;
		this.author = author;
		this.date = date;
			
	}
	
	
	// setters
	public void setTitle(String title){
		this.title = title;
	}
	public void setNumberOfParts(int number_of_parts){
		this.number_of_parts = number_of_parts;
	}
	public void setKey(String key){
		this.key = key;
	}
	public void setAlbum(String album){
		this.album = album;
	}
	public void setAuthor(String author){
		this.author = author;
	}
	public void setDate(String date){
		this.date = date;
	}
	
	public void seti(double i){
		this.i = i;
	}
	public void setix(double ix){
		this.ix = ix;
	}
	public void setii(double ii){
		this.ii = ii;
	}
	public void setiix(double iix){
		this.iix = iix;
	}
	public void setiii(double iii){
		this.iii = iii;
	}
	public void setiv(double iv){
		this.iv = iv;
	}
	public void setivx(double ivx){
		this.ivx = ivx;
	}
	public void setv(double v){
		this.v = v;
	}
	public void setvx(double vx){
		this.vx = vx;
	}
	public void setvi(double vi){
		this.vi = vi;
	}
	public void setvix(double vix){
		this.vix = vix;
	}
	public void setvii(double vii){
		this.vii = vii;
	}
	
	public void setci(String ci){
		this.ci = ci;
	}
	public void setcix(String cix){
		this.cix = cix;
	}
	public void setcii(String cii){
		this.cii = cii;
	}
	public void setciix(String ciix){
		this.ciix = ciix;
	}
	public void setciii(String ciii){
		this.ciii = ciii;
	}
	public void setciv(String civ){
		this.civ = civ;
	}
	public void setcivx(String civx){
		this.civx = civx;
	}
	public void setcv(String cv){
		this.cv = cv;
	}
	public void setcvx(String cvx){
		this.cvx = cvx;
	}
	public void setcvi(String cvi){
		this.cvi = cvi;
	}
	public void setcvix(String cvix){
		this.cvix = cvix;
	}
	public void setcvii(String cvii){
		this.cvii = cvii;
	}
	
	// getters
	public String getTitle(){
		return title;
	}
	public int getNumberOfParts(){
		return number_of_parts;
	}
	public String getKey(){
		return key;
	}
	public String getAlbum(){
		return album;
	}
	public String getAuthor(){
		return author;
	}
	public String getDate(){
		return date;
	}
	
	public double geti(){
		return i;
	}
	public double getix(){
		return ix;
	}
	public double getii(){
		return ii;
	}
	public double getiix(){
		return iix;
	}
	public double getiii(){
		return iii;
	}
	public double getiv(){
		return iv;
	}
	public double getivx(){
		return ivx;
	}
	public double getv(){
		return v;
	}
	public double getvx(){
		return vx;
	}
	public double getvi(){
		return vi;
	}
	public double getvix(){
		return vix;
	}
	public double getvii(){
		return vii;
	}
	
	public String getci(){
		return ci;
	}
	public String getcix(){
		return cix;
	}
	public String getcii(){
		return cii;
	}
	public String getciix(){
		return ciix;
	}
	public String getciii(){
		return ciii;
	}
	public String getciv(){
		return civ;
	}
	public String getcivx(){
		return civx;
	}
	public String getcv(){
		return cv;
	}
	public String getcvx(){
		return cvx;
	}
	public String getcvi(){
		return cvi;
	}
	public String getcvix(){
		return cvix;
	}
	public String getcvii(){
		return cvii;
	}
}

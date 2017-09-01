package corpusPreparation;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.HashMap;


public class Main {
	
	static String target_dir = "input/album_files";
	
	static HashMap<Integer, Song> song_hash_map = new HashMap<Integer, Song>();
	
	public static void main(String[] args){
		
		int number_of_errors = 0;
		
		File dir = new File(target_dir);
		File[] files = dir.listFiles();
		
		init_song_hash_map("input/meta_data.csv");
		
		// load the songs from the album .csv files and set the data to the songs inside the hashmap
		
		try{
            BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream("output/corpus_data.csv"), "UTF-8"));
            writer.write("title; number_of_parts; key; album; author; date; i; i#; ii; ii#; iii; iv; iv#; v; v#; vi; vi#; vii; ci; ci#; cii; cii#; ciii; civ; civ#; cv; cv#; cvi; cvi#; cvii");
            writer.write("\n");
            
            for (File f : files){
    			if (!f.isFile())
    		        continue;
    			try {
    	            java.io.BufferedReader FileReader = new java.io.BufferedReader(new java.io.FileReader(f));
    	            
    	           
    	            String song_data="";
    	            
    	            // skip the first line because its the headline
    	            FileReader.readLine();
    	            
    	            while(null!=(song_data=FileReader.readLine())){ 
    	                String[] data = song_data.split(";");
    	                
    	                System.out.println(song_data);
    	                
    	                String title = data[0];
    	                int number_of_parts = Integer.parseInt(data[1]);
    	                String key = data[2];
    	                
    	                double i = Double.parseDouble(data[3]);
    	                double ix = Double.parseDouble(data[4]);
    	                double ii = Double.parseDouble(data[5]);
    	                double iix = Double.parseDouble(data[6]);
    	                double iii = Double.parseDouble(data[7]);
    	                double iv = Double.parseDouble(data[8]);
    	                double ivx = Double.parseDouble(data[9]);
    	                double v = Double.parseDouble(data[10]);
    	                double vx = Double.parseDouble(data[11]);
    	                double vi = Double.parseDouble(data[12]);
    	                double vix = Double.parseDouble(data[13]);
    	                double vii = Double.parseDouble(data[14]);
    	                
    	                String ci = data[15];
    	                String cix = data[16];
    	                String cii = data[17];
    	                String ciix = data[18];
    	                String ciii = data[19];
    	                String civ = data[20];
    	                String civx = data[21];
    	                String cv = data[22];
    	                String cvx = data[23];
    	                String cvi = data[24];
    	                String cvix = data[25];
    	                String cvii = data[26];
    	                
    	                System.out.println("HASHCODETEST ::: " + title.hashCode());
    	                System.out.println(title.replaceAll("\\p{C}", "?"));
    	                
    	                System.out.println("trying to get song.... " + title);
    	                Song song = song_hash_map.get(title.hashCode());
    	                
    	                song.setNumberOfParts(number_of_parts);
    	                song.setKey(key);
    	                
    	                song.seti(i);
    	                song.setix(ix);
    	                song.setii(ii);
    	                song.setiix(iix);
    	                song.setiii(iii);
    	                song.setiv(iv);
    	                song.setivx(ivx);
    	                song.setv(v);
    	                song.setvx(vx);
    	                song.setvi(vi);
    	                song.setvix(vix);
    	                song.setvii(vii);
    	                
    	                song.setci(ci);
    	                song.setcix(cix);
    	                song.setcii(cii);
    	                song.setciix(ciix);
    	                song.setciii(ciii);
    	                song.setciv(civ);
    	                song.setcivx(civx);
    	                song.setcv(cv);
    	                song.setcvx(cvx);
    	                song.setcvi(cvi);
    	                song.setcvix(cvix);
    	                song.setcvii(cvii);
    	                
    	                // write .csv
    	                                
    	                writer.write(song.getTitle() +  ";");
    	                writer.write(song.getNumberOfParts() +  ";");
    	                writer.write(song.getKey() +  ";");
    	                writer.write(song.getAlbum() +  ";");
    	                writer.write(song.getAuthor() +  ";");
    	                writer.write(song.getDate() +  ";");
    	                
    	                writer.write(song.geti() +  ";");
    	                writer.write(song.getix() +  ";");
    	                writer.write(song.getii() +  ";");
    	                writer.write(song.getiix() +  ";");
    	                writer.write(song.getiii() +  ";");
    	                writer.write(song.getiv() +  ";");
    	                writer.write(song.getivx() +  ";");
    	                writer.write(song.getv() +  ";");
    	                writer.write(song.getvx() +  ";");
    	                writer.write(song.getvi() +  ";");
    	                writer.write(song.getvix() +  ";");
    	                writer.write(song.getvii() +  ";");
    	                
    	                writer.write(song.getci() +  ";");
    	                writer.write(song.getcix() +  ";");
    	                writer.write(song.getcii() +  ";");
    	                writer.write(song.getciix() +  ";");
    	                writer.write(song.getciii() +  ";");
    	                writer.write(song.getciv() +  ";");
    	                writer.write(song.getcivx() +  ";");
    	                writer.write(song.getcv() +  ";");
    	                writer.write(song.getcvx() +  ";");
    	                writer.write(song.getcvi() +  ";");
    	                writer.write(song.getcvix() +  ";");
    	                writer.write(song.getcvii());
    	                
    	                writer.write("\n");
    	            }
    	           
    	        } catch (Exception e) {
    	            e.printStackTrace();
    	            number_of_errors ++;
    	        }finally{
    	        	
    	        }
            }
            
        writer.flush();
	    writer.close();
	    
		}catch(Exception e){
			number_of_errors ++;
			e.printStackTrace();
		}
		System.out.println("THIS IS THE ERROR COUNT : !!! " + number_of_errors);
	}
	
	public static void init_song_hash_map(String filepath){
		int song_counter = 0;
		//create one object for every song in the meta_data.csv and push into the hashmap
		try {
            java.io.BufferedReader FileReader = new java.io.BufferedReader(new java.io.FileReader(
            				new java.io.File(filepath)));
           
            String meta_data_line="";
           
            while(null!=(meta_data_line=FileReader.readLine())){ 
                String[] meta_data = meta_data_line.split(";");
                System.out.println("creating song object ... " + meta_data[0] + " HASHED: " + meta_data[0].hashCode());
                
                //delete invisible characters from the title-string
                String title = meta_data[0].replaceAll("\\p{C}", "");;
                String album = meta_data[1];
                String author = meta_data[2];
                String date = meta_data[3];
                
                Song song = new Song(title, album, author, date);
                song_hash_map.put(title.hashCode(), song);
              
                song_counter += 1;
            }
           
        } catch (Exception e) {
            e.printStackTrace();
        }
		System.out.println(song_counter + " songs created ...!");
	}
	
}

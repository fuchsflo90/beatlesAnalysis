beatles_vis.beatles_vis_model = function(){

	var that = {};
	var filtered_data = null;
	var unfiltered_data = null;
	var chartbar_data = [];
	var piechart_data = [];
	var all_data = {};
	var active_album, active_author;

	var init = function(){
		active_album = "all";
		active_author = "all";
		get_all_data();
	};

	var filter_by_author = function(author){
		d3.csv("data/corpus_data_v3.csv", function(data) {
			that.filtered_data = data.filter(function(row) {
        		return row['author'] == author;
    		})
    		$(that).trigger('filter_request_finished');
		});
	};

	var filter_by_album = function(album){
		d3.csv("data/corpus_data_v3.csv", function(data) {
			that.filtered_data = data.filter(function(row) {
        		return row['album'] == album;
    		});
		});
	};

	var get_all_data = function(){
		d3.csv("data/corpus_data_v3.csv", function(data){
			unfiltered_data = data;
			that.filtered_data = data;
			$(that).trigger('data_update_complete');
		});
	};

	var init_chart_data = function(filtered_data){

		that.chartbar_data = [];
		that.piechart_data = [];

		if(active_album != 'all')
			init_single_album_chart_data(filtered_data);
		else
			init_all_albums_chart_data(filtered_data);

		$(that).trigger('model_init_complete');
	};

	var update_chart_data = function(){

		if (active_album === 'all' && active_author === 'all'){
			that.filtered_data = unfiltered_data;
			$(that).trigger('data_update_complete');
			return;
		}
		if (active_album === 'all'){
			if(active_author == 'harrison' || active_author == 'lennon' || active_author == 'mccartney' || active_author == 'starkey'){
				that.filtered_data = unfiltered_data.filter(function(row) {
        			return row['author'].indexOf(active_author) >=0 ;
    			});
    			$(that).trigger('data_update_complete');
    			return;
			}else if(active_author == 'beatles'){
				that.filtered_data = unfiltered_data.filter(function(row) {
        			return row['author'].indexOf('harrison') >=0 || row['author'].indexOf('lennon') >=0 || row['author'].indexOf('mccartney') >=0 || row['author'].indexOf('starkey') >=0 ;
    			});
    			$(that).trigger('data_update_complete');
    			return;
			}else if(active_author == 'cover'){
				that.filtered_data = unfiltered_data.filter(function(row) {
        			return row['author'].indexOf('harrison') < 0 && row['author'].indexOf('lennon') < 0 && row['author'].indexOf('mccartney') < 0 && row['author'].indexOf('starkey') < 0 ;
    			});
    			$(that).trigger('data_update_complete');
    			return;
			}
    	}
    	if (active_author === 'all'){
			that.filtered_data = unfiltered_data.filter(function(row) {
        		return row['album'] == active_album;
    		});
    		$(that).trigger('data_update_complete');
    		return;
		}
		if (active_album != 'all' && active_author != 'all'){
			that.filtered_data = unfiltered_data.filter(function(row) {
        		return row['album'] == active_album;
    		});
			if(active_author == 'harrison' || active_author == 'lennon' || active_author == 'mccartney' || active_author == 'starkey'){
				that.filtered_data = that.filtered_data.filter(function(row) {
        			return row['author'].indexOf(active_author) >=0 ;
    			});
    			$(that).trigger('data_update_complete');
    			return;
			}else if(active_author == 'beatles'){
				that.filtered_data = that.filtered_data.filter(function(row) {
        			return row['author'].indexOf('harrison') >=0 || row['author'].indexOf('lennon') >=0 || row['author'].indexOf('mccartney') >=0 || row['author'].indexOf('starkey') >=0 ;
    			});
    			$(that).trigger('data_update_complete');
    			return;
			}else if(active_author == 'cover'){
				that.filtered_data = that.filtered_data.filter(function(row) {
        			return row['author'].indexOf('harrison') < 0 && row['author'].indexOf('lennon') < 0 && row['author'].indexOf('mccartney') < 0 && row['author'].indexOf('starkey') < 0 ;
    			});
    			$(that).trigger('data_update_complete');
    			return;
			}
    		$(that).trigger('data_update_complete');
    		return;
		}
		console.log("invalid filters...");
	};

	var init_all_albums_chart_data = function(filtered_data){
		that.all_data = {}

		var album_names = init_album_names(filtered_data);

		$.each(album_names, function(i, name){
			that.all_data[name] = [];
		});

		console.log(filtered_data);

		$.each(filtered_data, function(i, row){
			that.all_data[row.album].push(row);
		});

		console.log(that.all_data);

		$.each(album_names, function(i, name){
			var album_length = that.all_data[name].length;
			var album_column_chart = [];
			var album_column_pie = [];

			var album_values = {
				i: 0.0,
				ix: 0.0,
				ii: 0.0,
				iix: 0.0,
				iii: 0.0,
				iv: 0.0,
				ivx: 0.0,
				v: 0.0,
				vx: 0.0,
				vi: 0.0,
				vix: 0.0,
				vii: 0.0
			};

			album_column_chart.push(name);
			album_column_pie.push(name);

			$.each(that.all_data[name], function(i, song){

				var song_value_sum = 0.0;
				var song_percentages = {
					i: 0.0,
					ix: 0.0,
					ii: 0.0,
					iix: 0.0,
					iii: 0.0,
					iv: 0.0,
					ivx: 0.0,
					v: 0.0,
					vx: 0.0,
					vi: 0.0,
					vix: 0.0,
					vii: 0.0
				};

				song_value_sum = parseFloat(song.i) + parseFloat(song.ix) + parseFloat(song.ii) + parseFloat(song.iix) 
						+ parseFloat(song.iii) + parseFloat(song.iv) + parseFloat(song.ivx) + parseFloat(song.v) + parseFloat(song.vx)
						+ parseFloat(song.vi) + parseFloat(song.vix) + parseFloat(song.vii);

				album_values.i += parseFloat(song.i) / song_value_sum;
				album_values.ix += parseFloat(song.ix) / song_value_sum;
				album_values.ii += parseFloat(song.ii) / song_value_sum;
				album_values.iix += parseFloat(song.iix) / song_value_sum;
				album_values.iii += parseFloat(song.iii) / song_value_sum;
				album_values.iv += parseFloat(song.iv) / song_value_sum;
				album_values.ivx += parseFloat(song.ivx) / song_value_sum;
				album_values.v += parseFloat(song.v) / song_value_sum;
				album_values.vx += parseFloat(song.vx) / song_value_sum;
				album_values.vi += parseFloat(song.vi) / song_value_sum;
				album_values.vix += parseFloat(song.vix) / song_value_sum;
				album_values.vii += parseFloat(song.vii) / song_value_sum;
			});

			album_values.i = (album_values.i / album_length);
			album_values.ix = (album_values.ix / album_length);
			album_values.ii = (album_values.ii / album_length);
			album_values.iix = (album_values.iix / album_length);
			album_values.iii = (album_values.iii / album_length);
			album_values.iv = (album_values.iv / album_length);
			album_values.ivx = (album_values.ivx / album_length);
			album_values.v = (album_values.v / album_length);
			album_values.vx = (album_values.vx / album_length);
			album_values.vi = (album_values.vi / album_length);
			album_values.vix = (album_values.vix / album_length);
			album_values.vii = (album_values.vii / album_length);

			album_column_chart.push(round2fixed(album_values.i));
			album_column_chart.push(round2fixed(album_values.ix));
			album_column_chart.push(round2fixed(album_values.ii));
			album_column_chart.push(round2fixed(album_values.iix));
			album_column_chart.push(round2fixed(album_values.iii));
			album_column_chart.push(round2fixed(album_values.iv));
			album_column_chart.push(round2fixed(album_values.ivx));
			album_column_chart.push(round2fixed(album_values.v));
			album_column_chart.push(round2fixed(album_values.vx));
			album_column_chart.push(round2fixed(album_values.vi));
			album_column_chart.push(round2fixed(album_values.vix));
			album_column_chart.push(round2fixed(album_values.vii));

			album_column_pie.push(round2fixed(album_values.i + album_values.vi));
			album_column_pie.push(round2fixed(album_values.iii + album_values.v));
			album_column_pie.push(round2fixed(album_values.ii + album_values.iv + album_values.vii));
			album_column_pie.push(round2fixed(album_values.ix + album_values.iix + album_values.ivx + album_values.vx + album_values.vix));

			that.chartbar_data.push(album_column_chart);
			that.piechart_data.push(album_column_pie);
		});
	};

	var init_single_album_chart_data = function(filtered_data){
		that.all_data = {}
		var song_names = init_song_names(filtered_data);

		$.each(song_names, function(i, name){
			that.all_data[name] = [];
		});

		$.each(filtered_data, function(i, song){
			var song_column_chart = [];
			var song_column_pie = [];

			song_column_chart.push(song.title);
			song_column_pie.push(song.title);

			var song_value_sum = 0.0;
			var song_percentages = {
				i: 0.0,
				ix: 0.0,
				ii: 0.0,
				iix: 0.0,
				iii: 0.0,
				iv: 0.0,
				ivx: 0.0,
				v: 0.0,
				vx: 0.0,
				vi: 0.0,
				vix: 0.0,
				vii: 0.0
			};

			song_value_sum = parseFloat(song.i) + parseFloat(song.ix) + parseFloat(song.ii) + parseFloat(song.iix) 
						+ parseFloat(song.iii) + parseFloat(song.iv) + parseFloat(song.ivx) + parseFloat(song.v) + parseFloat(song.vx)
						+ parseFloat(song.vi) + parseFloat(song.vix) + parseFloat(song.vii);

			song_percentages.i = parseFloat(song.i) / song_value_sum;
			song_percentages.ix = parseFloat(song.ix) / song_value_sum;
			song_percentages.ii = parseFloat(song.ii) / song_value_sum;
			song_percentages.iix = parseFloat(song.iix) / song_value_sum;
			song_percentages.iii = parseFloat(song.iii) / song_value_sum;
			song_percentages.iv = parseFloat(song.iv) / song_value_sum;
			song_percentages.ivx = parseFloat(song.ivx) / song_value_sum;
			song_percentages.v = parseFloat(song.v) / song_value_sum;
			song_percentages.vx = parseFloat(song.vx) / song_value_sum;
			song_percentages.vi = parseFloat(song.vi) / song_value_sum;
			song_percentages.vix = parseFloat(song.vix) / song_value_sum;
			song_percentages.vii = parseFloat(song.vii) / song_value_sum;

			song_column_chart.push(round2fixed(song_percentages.i));
			song_column_chart.push(round2fixed(song_percentages.ix));
			song_column_chart.push(round2fixed(song_percentages.ii));
			song_column_chart.push(round2fixed(song_percentages.iix));
			song_column_chart.push(round2fixed(song_percentages.iii));
			song_column_chart.push(round2fixed(song_percentages.iv));
			song_column_chart.push(round2fixed(song_percentages.ivx));
			song_column_chart.push(round2fixed(song_percentages.v));
			song_column_chart.push(round2fixed(song_percentages.vx));
			song_column_chart.push(round2fixed(song_percentages.vi));
			song_column_chart.push(round2fixed(song_percentages.vix));
			song_column_chart.push(round2fixed(song_percentages.vii));

			song_column_pie.push(round2fixed(song_percentages.i + song_percentages.vi));
			song_column_pie.push(round2fixed(song_percentages.iii + song_percentages.v));
			song_column_pie.push(round2fixed(song_percentages.ii + song_percentages.iv + song_percentages.vii));
			song_column_pie.push(round2fixed(song_percentages.ix + song_percentages.iix + song_percentages.ivx + song_percentages.vx + song_percentages.vix));

			that.chartbar_data.push(song_column_chart);
			that.piechart_data.push(song_column_pie);
		});
	};

	var init_all_albums_chart_data_chords = function(){

	};

	var init_single_album_chart_data_chords = function(){

	};

	var build_piechart_data = function(){

	};

	var build_chartbar_data = function(){

	};

	var set_active_album = function(album){
		active_album = album;
	};

	var set_active_author = function(author){
		active_author = author;
	};

	var init_album_names = function(data){
		var album_names = [];
		$.each(data, function(index, row){
			if(jQuery.inArray(row.album, album_names) === -1)
				album_names.push(row.album);
		});
		return album_names;
	};

	var init_song_names = function(data){
		var song_names = [];
		$.each(data, function(index, row){
			song_names.push(row.title);
		});
		return song_names;
	};

	var round2fixed = function(value){
		value = +value;

  		if (isNaN(value))
    		return NaN;

  		// Shift
  		value = value.toString().split('e');
  		value = Math.round(+(value[0] + 'e' + (value[1] ? (+value[1] + 2) : 2)));

  		// Shift back
  		value = value.toString().split('e');
  		return (+(value[0] + 'e' + (value[1] ? (+value[1] - 2) : -2))).toFixed(2);
	};

	that.init_chart_data = init_chart_data;
	that.update_chart_data = update_chart_data;
	that.set_active_author = set_active_author;
	that.set_active_album = set_active_album;
	that.all_data = all_data;
	that.piechart_data = piechart_data;
	that.chartbar_data = chartbar_data;
	that.filter_by_author = filter_by_author;
	that.filter_by_album = filter_by_album;
	that.get_all_data = get_all_data;
	that.filtered_data = filtered_data;
	that.init = init;

	return that;
};
beatles_vis.beatles_vis_model = function(){

	var that = {};
	var filtered_data = null;
	var unfiltered_data = null;
	var chartbar_data = [];
	var piechart_data = [];
	var stacked_chart_data = [];
	var stacked_chart_data_chord = [];
	var chartbar_data_chord = [];
	var piechart_data_chord = [];
	var tree_map_data = {'key': [], 'metric': [], 'chord': []};
	var all_data = {};
	var album_name_array = [];
	var song_names = [];
	var active_album, active_author;
	var album_meta_data = {};
	var table_data = [];

	var init = function(){
		that.active_album = "all";
		active_author = "all";
		get_all_data();
	};

	var filter_by_author = function(author){
		d3.csv("data/corpus_data_chord2.csv", function(data) {
			that.filtered_data = data.filter(function(row) {
        		return row['author'] == author;
    		})
    		$(that).trigger('filter_request_finished');
		});
	};

	var filter_by_album = function(album){
		d3.csv("data/corpus_data_chord2.csv", function(data) {
			that.filtered_data = data.filter(function(row) {
        		return row['album'] == album;
    		});
		});
	};

	var get_all_data = function(){
		d3.csv("data/corpus_data_chord2.csv", function(data){
			unfiltered_data = data;
			that.filtered_data = data;
			$(that).trigger('data_update_complete');
		});
	};

	var init_chart_data = function(filtered_data){

		that.chartbar_data = [];
		that.piechart_data = [];
		that.chartbar_data_chord = [];
		that.piechart_data_chord = [];
		that.tree_map_data = {'key': [], 'metric': [], 'chord': []};
		that.album_meta_data = {};
		that.table_data = [];

		console.log(filtered_data);
		init_ablum_meta_data(filtered_data);

		if(that.active_album != 'all'){
			init_single_album_chart_data(filtered_data);
			init_single_album_chart_data_chords(filtered_data);
			init_tree_map_data(filtered_data);
			init_table_data(filtered_data);
		}else{
			init_all_albums_chart_data(filtered_data);
			init_all_albums_chart_data_chords(filtered_data);
		}

		$(that).trigger('model_init_complete');
	};

	var update_chart_data = function(){

		if (that.active_album === 'all' && active_author === 'all'){
			that.filtered_data = unfiltered_data;
			$(that).trigger('data_update_complete');
			return;
		}
		if (that.active_album === 'all'){
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
        		return row['album'] == that.active_album;
    		});
    		$(that).trigger('data_update_complete');
    		return;
		}
		if (that.active_album != 'all' && active_author != 'all'){
			that.filtered_data = unfiltered_data.filter(function(row) {
        		return row['album'] == that.active_album;
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
		that.album_name_array = [];

		var album_names = init_album_names(filtered_data);
		that.album_name_array = album_names;

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

		that.stacked_chart_data = init_stacked_chart_data(that.piechart_data);
	};

	var init_single_album_chart_data = function(filtered_data){
		that.all_data = {}
		that.song_names = [];
		that.song_names = init_song_names(filtered_data);

		$.each(that.song_names, function(i, name){
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
		that.stacked_chart_data = init_stacked_chart_data(that.piechart_data);
	};

	var init_all_albums_chart_data_chords = function(filtered_data){
		that.all_data = {}
		that.album_name_array = [];
		var album_names = init_album_names(filtered_data);
		that.album_name_array = album_names;

		$.each(album_names, function(i, name){
			that.all_data[name] = [];
		});

		$.each(filtered_data, function(i, row){
			that.all_data[row.album].push(row);
		});

		$.each(album_names, function(i, name){
			var album_length = that.all_data[name].length;
			var album_column_chart_chord = [];
			var album_column_pie_chord = [];
			var album_column_stacked_chord = [];

			var album_values = {
				ci: 0.0,
				cix: 0.0,
				cii: 0.0,
				ciix: 0.0,
				ciii: 0.0,
				civ: 0.0,
				civx: 0.0,
				cv: 0.0,
				cvx: 0.0,
				cvi: 0.0,
				cvix: 0.0,
				cvii: 0.0
			};

			album_column_chart_chord.push(name);
			album_column_pie_chord.push(name);

			$.each(that.all_data[name], function(i, song){

				var song_value_sum = 0.0;

				song_value_sum = parseFloat(get_chord_value(song.ci)) + parseFloat(get_chord_value(song.cix)) + parseFloat(get_chord_value(song.cii))+ parseFloat(get_chord_value(song.ciix)) 
						+ parseFloat(get_chord_value(song.ciii)) + parseFloat(get_chord_value(song.civ)) + parseFloat(get_chord_value(song.civx)) + parseFloat(get_chord_value(song.cv)) + parseFloat(get_chord_value(song.cvx))
						+ parseFloat(get_chord_value(song.cvi)) + parseFloat(get_chord_value(song.cvix)) + parseFloat(get_chord_value(song.cvii));

				if (song_value_sum == 0.0){
					album_length = album_length -1;
				}else{
					album_values.ci += parseFloat(get_chord_value(song.ci)) / song_value_sum;
					album_values.cix += parseFloat(get_chord_value(song.cix)) / song_value_sum;
					album_values.cii += parseFloat(get_chord_value(song.cii)) / song_value_sum;
					album_values.ciix += parseFloat(get_chord_value(song.ciix)) / song_value_sum;
					album_values.ciii += parseFloat(get_chord_value(song.ciii)) / song_value_sum;
					album_values.civ += parseFloat(get_chord_value(song.civ)) / song_value_sum;
					album_values.civx += parseFloat(get_chord_value(song.civx)) / song_value_sum;
					album_values.cv += parseFloat(get_chord_value(song.cv)) / song_value_sum;
					album_values.cvx += parseFloat(get_chord_value(song.cvx)) / song_value_sum;
					album_values.cvi += parseFloat(get_chord_value(song.cvi)) / song_value_sum;
					album_values.cvix += parseFloat(get_chord_value(song.cvix)) / song_value_sum;
					album_values.cvii += parseFloat(get_chord_value(song.cvii)) / song_value_sum;
				}
			});

			album_values.ci = (album_values.ci / album_length);
			album_values.cix = (album_values.cix / album_length);
			album_values.cii = (album_values.cii / album_length);
			album_values.ciix = (album_values.ciix / album_length);
			album_values.ciii = (album_values.ciii / album_length);
			album_values.civ = (album_values.civ / album_length);
			album_values.civx = (album_values.civx / album_length);
			album_values.cv = (album_values.cv / album_length);
			album_values.cvx = (album_values.cvx / album_length);
			album_values.cvi = (album_values.cvi / album_length);
			album_values.cvix = (album_values.cvix / album_length);
			album_values.cvii = (album_values.cvii / album_length);

			album_column_chart_chord.push(round2fixed(album_values.ci));
			album_column_chart_chord.push(round2fixed(album_values.cix));
			album_column_chart_chord.push(round2fixed(album_values.cii));
			album_column_chart_chord.push(round2fixed(album_values.ciix));
			album_column_chart_chord.push(round2fixed(album_values.ciii));
			album_column_chart_chord.push(round2fixed(album_values.civ));
			album_column_chart_chord.push(round2fixed(album_values.civx));
			album_column_chart_chord.push(round2fixed(album_values.cv));
			album_column_chart_chord.push(round2fixed(album_values.cvx));
			album_column_chart_chord.push(round2fixed(album_values.cvi));
			album_column_chart_chord.push(round2fixed(album_values.cvix));
			album_column_chart_chord.push(round2fixed(album_values.cvii));

			album_column_pie_chord.push(round2fixed(album_values.ci + album_values.cvi));
			album_column_pie_chord.push(round2fixed(album_values.civ + album_values.cv));
			album_column_pie_chord.push(round2fixed(album_values.cii + album_values.ciii + album_values.cvii));
			album_column_pie_chord.push(round2fixed(album_values.cix + album_values.ciix + album_values.civx + album_values.cvx + album_values.cvix));

			that.chartbar_data_chord.push(album_column_chart_chord);
			that.piechart_data_chord.push(album_column_pie_chord);
		});
		that.stacked_chart_data_chord = init_stacked_chart_data(that.piechart_data_chord);
	};

	var init_single_album_chart_data_chords = function(filtered_data){
		that.song_names = [];
		that.all_data = {}
		that.song_names = init_song_names(filtered_data);
		var album_length = song_names.length;

		$.each(that.song_names, function(i, name){
			that.all_data[name] = [];
		});

		$.each(filtered_data, function(i, song){
			var song_column_chart_chord = [];
			var song_column_pie_chord = [];

			song_column_chart_chord.push(song.title);
			song_column_pie_chord.push(song.title);

			var song_value_sum = 0.0;
			var song_percentages = {
				ci: 0.0,
				cix: 0.0,
				cii: 0.0,
				ciix: 0.0,
				ciii: 0.0,
				civ: 0.0,
				civx: 0.0,
				cv: 0.0,
				cvx: 0.0,
				cvi: 0.0,
				cvix: 0.0,
				cvii: 0.0
			};

			song_value_sum = parseFloat(get_chord_value(song.ci)) + parseFloat(get_chord_value(song.cix)) + parseFloat(get_chord_value(song.cii)) + parseFloat(get_chord_value(song.ciix)) 
						+ parseFloat(get_chord_value(song.ciii)) + parseFloat(get_chord_value(song.civ)) + parseFloat(get_chord_value(song.civx)) + parseFloat(get_chord_value(song.cv)) + parseFloat(get_chord_value(song.cvx))
						+ parseFloat(get_chord_value(song.cvi)) + parseFloat(get_chord_value(song.cvix)) + parseFloat(get_chord_value(song.cvii));
			if (song_value_sum == 0.0){
				album_length = album_length -1;
			}else{
				song_percentages.ci = parseFloat(get_chord_value(song.ci)) / song_value_sum;
				song_percentages.cix = parseFloat(get_chord_value(song.cix)) / song_value_sum;
				song_percentages.cii = parseFloat(get_chord_value(song.cii)) / song_value_sum;
				song_percentages.ciix = parseFloat(get_chord_value(song.ciix)) / song_value_sum;
				song_percentages.ciii = parseFloat(get_chord_value(song.ciii)) / song_value_sum;
				song_percentages.civ = parseFloat(get_chord_value(song.civ)) / song_value_sum;
				song_percentages.civx = parseFloat(get_chord_value(song.civx)) / song_value_sum;
				song_percentages.cv = parseFloat(get_chord_value(song.cv)) / song_value_sum;
				song_percentages.cvx = parseFloat(get_chord_value(song.cvx)) / song_value_sum;
				song_percentages.cvi = parseFloat(get_chord_value(song.cvi)) / song_value_sum;
				song_percentages.cvix = parseFloat(get_chord_value(song.cvix)) / song_value_sum;
				song_percentages.cvii = parseFloat(get_chord_value(song.cvii)) / song_value_sum;
			}

			song_column_chart_chord.push(round2fixed(song_percentages.ci));
			song_column_chart_chord.push(round2fixed(song_percentages.cix));
			song_column_chart_chord.push(round2fixed(song_percentages.cii));
			song_column_chart_chord.push(round2fixed(song_percentages.ciix));
			song_column_chart_chord.push(round2fixed(song_percentages.ciii));
			song_column_chart_chord.push(round2fixed(song_percentages.civ));
			song_column_chart_chord.push(round2fixed(song_percentages.civx));
			song_column_chart_chord.push(round2fixed(song_percentages.cv));
			song_column_chart_chord.push(round2fixed(song_percentages.cvx));
			song_column_chart_chord.push(round2fixed(song_percentages.cvi));
			song_column_chart_chord.push(round2fixed(song_percentages.cvix));
			song_column_chart_chord.push(round2fixed(song_percentages.cvii));

			song_column_pie_chord.push(round2fixed(song_percentages.ci + song_percentages.cvi));
			song_column_pie_chord.push(round2fixed(song_percentages.civ + song_percentages.cv));
			song_column_pie_chord.push(round2fixed(song_percentages.cii + song_percentages.ciii + song_percentages.cvii));
			song_column_pie_chord.push(round2fixed(song_percentages.cix + song_percentages.ciix + song_percentages.civx + song_percentages.cvx + song_percentages.cvix));

			that.chartbar_data_chord.push(song_column_chart_chord);
			that.piechart_data_chord.push(song_column_pie_chord);
		});
		that.stacked_chart_data_chord = init_stacked_chart_data(that.piechart_data_chord);
	};

	var set_active_album = function(album){
		that.active_album = album;
	};

	var set_active_author = function(author){
		active_author = author;
	};

	var init_stacked_chart_data = function(pie_data){
		var output = [['ebene1'], ['ebene2'], ['ebene3'], ['ebene4']];
		$.each(pie_data, function(index, album){
			output[0].push(album[1]);
			output[1].push(album[2]);
			output[2].push(album[3]);
			output[3].push(album[4]);
		});
		return output;
	};

	var init_tree_map_data = function(filtered_data){

		var key_map_data = {};
		var metric_map_data = {};

		$.each(filtered_data, function(index, song){
			var key_values = [];
			var metrics_arr = song.metrics.clean_metrics(";",2);
			metric_map_data = add_metrics_to_object(metric_map_data, metrics_arr);
			key_values.push(song.key);
			var key_change_info = song.key_change_info.replace(/\[/g,"");
			key_change_info = key_change_info.replace(/\]/g,"");
			key_change_info = key_change_info.replace(/\'/g,"");


			if(key_change_info.indexOf('None') < 0){
				console.log("key_change_info");
				console.log(key_change_info);
				var info_array = key_change_info.replace(" ","").split(';');
				console.log(info_array);
				$.each(info_array, function(index, val){
					key_values.push(val);
				});
			}

			console.log("key values");
			console.log(key_values);

			$.each(key_values, function(index, val){
				if(key_map_data.hasOwnProperty(val)){
					key_map_data[val] = parseInt(key_map_data[val]) + 1;
				}else{
					key_map_data[val] = 1;
				}
			});
			console.log("key_map_data");
			console.log(key_map_data);


		});
		key_map_data = transform_object_to_tree_data(key_map_data);
		metric_map_data = transform_object_to_tree_data(metric_map_data);

		that.tree_map_data.key = key_map_data;
		that.tree_map_data.metric = metric_map_data;
		that.tree_map_data.chord = extract_chord_types(filtered_data);

		console.log("map data: ");
		console.log(that.tree_map_data);
	};

	var init_ablum_meta_data = function(filtered_data){

		that.album_meta_data = {
			song_count: 0,
			key_changes: 0,
			metric_changes: 0,
			instrumental_tracks: 0,
			date: ""
		};

		that.album_meta_data.song_count = filtered_data.length;

		if (that.active_album == 'all' || that.active_album == 'single'){
			that.album_meta_data.date = "1963-1970"
		}else{
			that.album_meta_data.date = get_date_from_value(filtered_data[0].date);
		}

		$.each(filtered_data, function(index, song){
			var key_change_info = song.key_change_info;
			var metric_changes = song.metrics.clean_metrics(";", 2);

			if(key_change_info.indexOf('None') < 0 ){
				that.album_meta_data.key_changes = that.album_meta_data.key_changes + 1;
			}
			that.album_meta_data.instrumental_tracks = that.album_meta_data.instrumental_tracks + parseInt(song.number_of_parts);
			if(metric_changes.length > 1){
				that.album_meta_data.metric_changes = parseInt(that.album_meta_data.metric_changes) + 1;
			}
		});

		that.album_meta_data.instrumental_tracks = round2fixed(that.album_meta_data.instrumental_tracks / that.album_meta_data.song_count);
		console.log(that.album_meta_data);
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

	var init_table_data = function(data){
		var new_table_data = [];
		$.each(data, function(index, row){
			var table_row = [row.title, row.author, row.key, row.metrics];
			new_table_data.push(table_row);
		});
		that.table_data = new_table_data;
	};

	var get_chord_value = function(chord_string){
		var chord_values = chord_string.split('[');
		var chord_value = round2fixed(parseFloat(chord_values[0]));;

		return chord_value;
	};

	var get_date_from_value = function(value){
		var arr = value.split(' ');
		var month = "";
		var year = "";
		var output = "";

		switch (arr[0]) {
   			case '01':
      			month = "Januar";
      			break;
      		case '02':
      			month = "Februar";
      			break;
      		case '03':
      			month = "März";
      			break;
      		case '04':
      			month = "April";
      			break;
      		case '05':
      			month = "Mai";
      			break;
      		case '06':
      			month = "Juni";
      			break;
      		case '07':
      			month = "Juli";
      			break;
      		case '08':
      			month = "August";
      			break;
      		case '09':
      			month = "September";
      			break;
      		case '10':
      			month = "Oktober";
      			break;
      		case '11':
      			month = "November";
      			break;
      		case '12':
      			month = "Dezember";
      			break;
		}

		year = "19" + arr[1];
		output = month + " " + year;
		return output;
	};

	var transform_object_to_tree_data = function(object){
		var output_arr = [];

		for (key in object){
			var entry = {key:key, value: parseFloat(object[key])};
			output_arr.push(entry);
		}

		return output_arr;
	};

	var extract_chord_types = function(album){

		var chord_map_data = {};

		$.each(album, function(index, song){

			var chord_type_array = [];
			var song_chord_value_sum = 0.0;

			song_chord_value_sum = parseFloat(song.ci.split('[')[0]) + parseFloat(song.cix.split('[')[0]) + parseFloat(song.cii.split('[')[0])
				+ parseFloat(song.ciix.split('[')[0]) + parseFloat(song.ciii.split('[')[0]) + parseFloat(song.civ.split('[')[0])
				+ parseFloat(song.civx.split('[')[0]) + parseFloat(song.cv.split('[')[0]) + parseFloat(song.cvx.split('[')[0])
				+ parseFloat(song.cvi.split('[')[0]) + parseFloat(song.cvix.split('[')[0]) + parseFloat(song.cvii.split('[')[0]);

			chord_type_array.push(song.ci.clean_chord_types(';', 2));
			chord_type_array.push(song.cix.clean_chord_types(';', 2));
			chord_type_array.push(song.cii.clean_chord_types(';', 2));
			chord_type_array.push(song.ciix.clean_chord_types(';', 2));
			chord_type_array.push(song.ciii.clean_chord_types(';', 2));
			chord_type_array.push(song.civ.clean_chord_types(';', 2));

			chord_type_array.push(song.civx.clean_chord_types(';', 2));
			chord_type_array.push(song.cv.clean_chord_types(';', 2));
			chord_type_array.push(song.cvx.clean_chord_types(';', 2));
			chord_type_array.push(song.cvi.clean_chord_types(';', 2));
			chord_type_array.push(song.cvix.clean_chord_types(';', 2));
			chord_type_array.push(song.cvii.clean_chord_types(';', 2));

			$.each(chord_type_array, function(index, val){
				var splitted = val.toString().split(',');
				var variation = splitted[0];
				var value = splitted[1];

				if(variation == ""){
					//nothing
				}else if (chord_map_data.hasOwnProperty(variation)){
					chord_map_data.variation = (parseFloat(chord_map_data.variation) + (parseFloat(value) / parseFloat(song_chord_value_sum)));
				}else{
					chord_map_data[variation] = parseFloat(value) / parseFloat(song_chord_value_sum);
				}
			});

		});

		return transform_object_to_tree_data(chord_map_data);
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

	String.prototype.clean_metrics = function(splitter, every){
		var parts = this.replace(/\[/g,"").replace(/\(/g,"").replace(/\'/g,"").split(splitter);
		var answer = [];
		
		for (var i=0; i<parts.length; i++) {
        	if (i < 1) continue;
        	if (i % every == 1) {
           		answer.push(parts[i-1]);
        	}
 		}
    	return answer;
	};

	String.prototype.clean_chord_types = function(splitter, every){
		var clean_string = this.replace(/\]/g,"");
		clean_string = clean_string.replace(/\(/g,"");
		clean_string = clean_string.replace(/\)/g,"");
		clean_string = clean_string.replace(/\'/g,"");

		var parts = clean_string.split('[')[1].split(splitter);
		var answer = [];

		for (var i=0; i<parts.length; i++){
			if(i < 1) continue;
			if(i % every == 1){
				answer.push(parts[i-1] + "," + parts[i]);
			}
		}
		return answer;
	};

	var sum_chord_types = function(arr){

	};

	var add_metrics_to_object = function(object, arr){
		$.each(arr, function(index, m){
			if (object.hasOwnProperty(m)){
				object[m] = object[m] + 1;
			}else{
				object[m] = 1;
			}
		});

		return object;
	};

	that.album_meta_data = album_meta_data;
	that.active_album = active_album;
	that.init_chart_data = init_chart_data;
	that.update_chart_data = update_chart_data;
	that.set_active_author = set_active_author;
	that.set_active_album = set_active_album;
	that.all_data = all_data;
	that.table_data = table_data;
	that.song_names = song_names;
	that.album_name_array = album_name_array;
	that.piechart_data = piechart_data;
	that.chartbar_data = chartbar_data;
	that.stacked_chart_data = stacked_chart_data;
	that.stacked_chart_data_chord = stacked_chart_data_chord;
	that.piechart_data_chord = piechart_data_chord;
	that.chartbar_data_chord = chartbar_data_chord;
	that.tree_map_data = tree_map_data;
	that.filter_by_author = filter_by_author;
	that.filter_by_album = filter_by_album;
	that.get_all_data = get_all_data;
	that.filtered_data = filtered_data;
	that.init = init;

	return that;
};
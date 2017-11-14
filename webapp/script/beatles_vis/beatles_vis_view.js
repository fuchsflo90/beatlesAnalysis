beatles_vis.beatles_vis_view = function(){
	var that = {};
	var chartbar = null;
	var stacked_chartbar = null;
	var piechart = null;
	var piechart_array = [];
	var chartbar_array = [];
	var tree_map_array = [];

	var init = function(){
		hide_elements();
	};

	var set_body_padding = function(){
		var navbar_height = $('#fixed-top-navigation').height() / 2.0;
		$('body,html').css('padding-top',navbar_height);
		console.log('navbar_height: ' + navbar_height);
	};

	var build_chartbar = function(chartbar_data, anchor){
		chartbar = beatles_vis.chartbar();
		chartbar.init(chartbar_data, anchor);
		chartbar_array.push(chartbar);
	};

	var build_stacked_chartbar = function(stacked_chartbar_data, album_name_array, anchor){
		stacked_chartbar = beatles_vis.stacked_chartbar();
		stacked_chartbar.init(stacked_chartbar_data, album_name_array, anchor);
		chartbar_array.push(stacked_chartbar);
	};

	var build_stacked_chartbar_sep = function(stacked_chartbar_data, song_name_array, anchor){
		stacked_chartbar_sep = beatles_vis.stacked_chartbar_sep();
		stacked_chartbar_sep.init(stacked_chartbar_data, song_name_array, anchor);
		chartbar_array.push(stacked_chartbar_sep);
	};

	var build_piechart = function(i, title, piechart_data){

		var anchor = "#pie_chart" + i;

		$('#pie_chart_area').append("<div class='pie_chart_tile col-md-2 " + title + "'><div id='pie_chart" + i + "'></div><div id='pie_chart_album" + i + "' class='album_pile_button'>" + title + "</div></div>");
		piechart = beatles_vis.piechart();
		piechart.init(piechart_data, anchor);
		piechart_array.push(piechart);
	};

	var build_tree_map = function(tree_map_data, anchor){
		tree_map = beatles_vis.tree_map();
		tree_map.init(tree_map_data, anchor);
		tree_map_array.push(tree_map);
	};

	var build_info_table = function(info_arr){
		$('.info_table_body').empty();
		$.each(info_arr, function(index, row){
			$('.info_table_body').append("<tr><td>" + row[0] + "</td><td>" + row[1] + "</td><td>" + row[2] + "</td><td>" + row[3] + "</td></tr>");
		});
	};

	var clear_charts = function(){

		$.each(chartbar_array, function(i, chartbar){
			chartbar.destroy();
		});
		$.each(piechart_array, function(i, piechart){
			piechart.destroy();
		});
/*
		$.each(tree_map_array, function(i, tree_map){
			tree_map.destroy();
		});*/

		$('#pie_chart_area').empty();

		piechart_array = [];
		chartbar_array = [];
	};

	var build_headline_album_menu = function(data){
		$('.headline_album_menu').remove();
		$('#header').append("<div class='headline_album_menu'></div>");
		album_name_list = [];
		$.each(data, function(i, datarow){
			album_name_list.push(datarow[0]);
		});
		$.each(album_name_list, function(i, name){
			$('.headline_album_menu').append("<div class='headline_album_button col-md-1 "+ name +"'>" + name + "</div>");
		});
		set_body_padding();
	};

	var hide_elements = function(){
		$('#album_meta_data').hide();
		$('#single_album_tone_area').hide();
		$('#single_album_chord_area').hide();
	};

	var set_meta_data = function(meta_data){
		$('#song_count').html(meta_data.song_count);
		$('#key_change_count').html(meta_data.key_changes);
		$('#metric_change_count').html(meta_data.metric_changes);
		$('#instrumentation_count').html(meta_data.instrumental_tracks);
		$('#date').html(meta_data.date);
	};

	that.set_meta_data = set_meta_data;
	that.build_headline_album_menu = build_headline_album_menu;
	that.clear_charts = clear_charts;
	that.build_piechart = build_piechart;
	that.build_chartbar = build_chartbar;
	that.build_stacked_chartbar = build_stacked_chartbar;
	that.build_stacked_chartbar_sep = build_stacked_chartbar_sep;
	that.build_tree_map = build_tree_map;
	that.build_info_table = build_info_table;
	that.init = init;
	return that;
};
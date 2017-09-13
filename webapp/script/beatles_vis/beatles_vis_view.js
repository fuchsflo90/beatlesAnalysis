beatles_vis.beatles_vis_view = function(){
	var that = {};
	var chartbar = null;
	var piechart = null;
	var piechart_array = [];

	var init = function(){
		
	};

	var build_chartbar = function(chartbar_data){
		chartbar = beatles_vis.chartbar();
		chartbar.init(chartbar_data);
	};

	var build_piechart = function(i, title, piechart_data){

		var anchor = "#pie_chart" + i;

		$('#pie_chart_area').append("<div class='pie_chart_tile col-md-2 " + title + "'><div id='pie_chart" + i + "'></div><div id='pie_chart_album" + i + "' class='album_pile_button'>" + title + "</div></div>");
		piechart = beatles_vis.piechart();
		piechart.init(piechart_data, anchor);
		piechart_array.push(piechart);
	};

	var clear_charts = function(){

		chartbar.destroy();
		$.each(piechart_array, function(i, piechart){
			piechart.destroy();
		});

		$('#pie_chart_area').empty();

		piechart_array = [];
	};

	var build_headline_album_menu = function(data){
		$('.headline_album_menu').remove();
		$('#header').append("<div class='headline_album_menu'></div>");
		album_name_list = [];
		$.each(data, function(i, datarow){
			album_name_list.push(datarow[0]);
		});
		$.each(album_name_list, function(i, name){
			$('.headline_album_menu').append("<span class='headline_album_button'>" + name + "</span>");
		});
	};

	that.build_headline_album_menu = build_headline_album_menu;
	that.clear_charts = clear_charts;
	that.build_piechart = build_piechart;
	that.build_chartbar = build_chartbar;
	that.init = init;
	return that;
};
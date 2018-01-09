beatles_vis.beatles_vis_controller = function(){
	var that = {};

	var beatles_vis_model = null;
	var beatles_vis_view = null;

	var init = function(){

		beatles_vis_model = beatles_vis.beatles_vis_model();
		beatles_vis_view = beatles_vis.beatles_vis_view();

		init_trigger();
		init_button_functions();

		beatles_vis_model.init();

	};

	var init_trigger = function(){
		$(beatles_vis_model).on('model_init_complete', build_charts);
		$(beatles_vis_model).on('data_update_complete', init_chart_data);
	};

	var init_button_functions = function(){
		$('#all_albums_button').on('click', function(){
			reset_treemap_area();
			$('#chord_treemap_area').empty();
			$('#chord_treemap_area').addClass('hide');
			$('.selected_album').html('Alle');
			$('#stacked_chart_area').fadeIn();
			$('#stacked_chart_area_chord').fadeIn();
			$('#single_album_tone_area').addClass('hide');
			$('#single_album_chord_area').addClass('hide');
			beatles_vis_view.clear_charts();
			beatles_vis_model.set_active_album('all');
			beatles_vis_model.update_chart_data();
		});

		$('#author_select').on('change', function(){
			reset_treemap_area();
			$('#chord_treemap_area').empty();
			beatles_vis_view.clear_charts();
			beatles_vis_model.set_active_author(this.value);
			console.log(this.value);
			beatles_vis_model.update_chart_data();
		});

		$('.infolink').on('click', function(){
			$('body>div').addClass('hide');
			$('body>div').addClass('hide');
			$('#info').removeClass('hide');
		});
	};

	var build_charts = function(){

		$('body>div').removeClass('hide');
		$('.loader').addClass('hide');
		$('#info').addClass('hide');

		if(beatles_vis_model.active_album == 'all'){
			beatles_vis_view.build_headline_album_menu(beatles_vis_model.chartbar_data);

			$('.headline_album_button').on('click', function(){
				$('.selected_album').html($(this).html());
				reset_treemap_area();
				$('#chord_treemap_area').empty();
				$('#chord_treemap_area').removeClass('hide');
				$('.headline_album_button').removeClass('active');
				$(this).addClass('active');
				$('#stacked_chart_area').fadeOut();
				$('#stacked_chart_area_chord').fadeOut();
				$('#single_album_tone_area').removeClass('hide');
				$('#single_album_chord_area').removeClass('hide');
				$('#song_info_list').removeClass('hide');
				beatles_vis_view.clear_charts();
				beatles_vis_model.set_active_album($(this).html());
				beatles_vis_model.update_chart_data();
			});
		}

		beatles_vis_view.build_chartbar(beatles_vis_model.chartbar_data, '#bar_chart');
		beatles_vis_view.build_chartbar(beatles_vis_model.chartbar_data_chord, '#chord_chart_area');
		beatles_vis_view.build_stacked_chartbar(beatles_vis_model.stacked_chart_data, beatles_vis_model.album_name_array, '#stacked_chart_area');
		beatles_vis_view.build_stacked_chartbar(beatles_vis_model.stacked_chart_data_chord, beatles_vis_model.album_name_array, '#stacked_chart_area_chord');
		beatles_vis_view.build_stacked_chartbar_sep(beatles_vis_model.stacked_chart_data, beatles_vis_model.song_names, '#single_album_tone_area');
		beatles_vis_view.build_stacked_chartbar_sep(beatles_vis_model.stacked_chart_data_chord, beatles_vis_model.song_names, '#single_album_chord_area');
		beatles_vis_view.build_tree_map(beatles_vis_model.tree_map_data.key, '#key_map_area');
		beatles_vis_view.build_tree_map(beatles_vis_model.tree_map_data.metric, '#metric_map_area');
		beatles_vis_view.build_tree_map(beatles_vis_model.tree_map_data.chord, '#chord_treemap_area');
		beatles_vis_view.set_meta_data(beatles_vis_model.album_meta_data);
		beatles_vis_view.build_info_table(beatles_vis_model.table_data);
		$('.album_pile_button').remove();
		/*
		$.each(beatles_vis_model.piechart_data, function(i, data){
			beatles_vis_view.build_piechart(i, data[0] ,[['ebene1', data[1]], ['ebene2', data[2]], ['ebene3', data[3]], ['ebene4', data[4]]]);
		});
		*/
	};
	var reset_treemap_area = function(){
		$('#tree_map_area').empty();
		$('#tree_map_area').append("<div class='col-md-6'><h4>Tonarten</h4></div>");
		$('#tree_map_area').append("<div class='col-md-6'><h4>Taktarten</h4></div>");
		$('#tree_map_area').append("<div id='key_map_area' class='col-md-6'></div>");
		$('#tree_map_area').append("<div id='metric_map_area' class='col-md-6'></div>");
	};

	var init_chart_data = function(){
		beatles_vis_model.init_chart_data(beatles_vis_model.filtered_data);
	};

	that.init = init;

	return that;
};
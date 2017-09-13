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
			beatles_vis_view.clear_charts();
			beatles_vis_model.set_active_album('all');
			beatles_vis_model.update_chart_data();
		});
	};

	var build_charts = function(){
		if($('.headline_album_menu').length == 0){
			beatles_vis_view.build_headline_album_menu(beatles_vis_model.chartbar_data);
			$('.headline_album_button').on('click', function(){
				beatles_vis_view.clear_charts();
				beatles_vis_model.set_active_album($(this).html());
				beatles_vis_model.update_chart_data();
			});
		}

		beatles_vis_view.build_chartbar(beatles_vis_model.chartbar_data);
		$('.album_pile_button').remove();

		$.each(beatles_vis_model.piechart_data, function(i, data){
			beatles_vis_view.build_piechart(i, data[0] ,[['ebene1', data[1]], ['ebene2', data[2]], ['ebene3', data[3]], ['ebene4', data[4]]]);
		});
	};

	var init_chart_data = function(){
		beatles_vis_model.init_chart_data(beatles_vis_model.filtered_data);
	};

	that.init = init;

	return that;
};
beatles_vis.stacked_chartbar_sep = function(){

  var that = {};
  var chart = null;

  init = function(stacked_chartbar_data, song_name_array, anchor){
    generate_stacked_chart_bar_sep(stacked_chartbar_data, song_name_array, anchor);
  }

  var generate_stacked_chart_bar_sep = function(stacked_chartbar_data, song_name_array, anchor){

    chart = c3.generate({
      bindto: anchor,
      data: {
        columns: stacked_chartbar_data,
        type: 'bar',
        groups: [['ebene1', 'ebene2', 'ebene3', 'ebene4']],
        order: null
      },
      grid: {
        x: {
          show: true
        },
        y: {
          show: true
        }
      },
      bar: {
        width: {
            ratio: 0.8 // this makes bar width 50% of length between ticks
        }
        // or
        //width: 100 // this makes bar width 100px
      },
      axis: {
        x:{
          type: 'category',
          categories: song_name_array
        }
      }
    });
  };

  var destroy = function(){
    chart.load({
      unload: true 
    });
  };

  that.destroy = destroy;
  that.init = init;

  return that;
}
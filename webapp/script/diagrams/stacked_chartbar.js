beatles_vis.stacked_chartbar = function(){

  var that = {};
  var chart = null;

  init = function(stacked_chartbar_data, album_name_array, anchor){
    generate_stacked_chart_bar(stacked_chartbar_data, album_name_array, anchor);
  }

  var generate_stacked_chart_bar = function(stacked_chartbar_data, album_name_array, anchor){

    chart = c3.generate({
      bindto: anchor,
      data: {
        columns: stacked_chartbar_data,
        types: {
          ebene1: 'area-spline',
          ebene2: 'area-spline',
          ebene3: 'area-spline',
          ebene4: 'area-spline'
        },
        groups: [['ebene1', 'ebene2', 'ebene3', 'ebene4']]
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
          categories: album_name_array
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
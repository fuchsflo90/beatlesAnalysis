beatles_vis.stacked_chartbar = function(){

  var that = {};
  var chart = null;

  init = function(stacked_chartbar_data, album_name_array, anchor){
    generate_stacked_chart_bar(stacked_chartbar_data, album_name_array, anchor);
  }

  var generate_stacked_chart_bar = function(stacked_chartbar_data, album_name_array, anchor){

/**
    var new_name_array = [];

    $.each(album_name_array, function(i, value){
      if(i == 0){
        new_name_array.push(album_name_array[0]);
      }else if(i == 1){
        new_name_array.push("|");
        new_name_array.push(album_name_array[1])
      }else{
        new_name_array.push(album_name_array[i]);
      }
    })

    **/

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
            ratio: 0.8
        }
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
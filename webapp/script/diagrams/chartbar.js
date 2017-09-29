beatles_vis.chartbar = function(){

  var that = {};
  var chart = null;

  init = function(chartbar_data, anchor){
    generate_chart_bar(chartbar_data, anchor);
  }

  var generate_chart_bar = function(chartbar_data, anchor){

    chart = c3.generate({
      bindto: anchor,
      data: {
        columns: chartbar_data,
        type: 'bar'
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
          categories: ['I', 'I#', 'II', 'II#', 'III', 'IV', 'IV#', 'V', 'V#', 'VI', 'VI#', 'VII']
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
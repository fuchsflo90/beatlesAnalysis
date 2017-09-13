beatles_vis.chartbar = function(){

  var that = {};
  var chart = null;

  init = function(chartbar_data){
    generate_chart_bar(chartbar_data);
  }

  var generate_chart_bar = function(chartbar_data){

    console.log(chartbar_data);

    chart = c3.generate({
      bindto: '#bar_chart',
      data: {
        columns: chartbar_data,
        type: 'bar'
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
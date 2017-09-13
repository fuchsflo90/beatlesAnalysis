beatles_vis.piechart = function(){

  var that = {};
  var chart = null;

  init = function(piechart_data, anchor){
    generate_pie_chart(piechart_data, anchor);
  }

  var generate_pie_chart = function(piechart_data, anchor){

    chart = c3.generate({
      bindto: anchor,
      data: {
        columns: piechart_data,
        type: 'pie'
      },
      legend:{
        show: false
      }
      /*size: {
        width: 100
      }*/
    });
  };

  var destroy = function(){
    chart.destroy();
  };

  that.destroy = destroy;
  that.init = init;

  return that;
}
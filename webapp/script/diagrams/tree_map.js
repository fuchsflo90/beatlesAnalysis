beatles_vis.tree_map = function(){

  var that = {};
  var mapheight;
  var mapwidth;

  init = function(tree_map_data, anchor){
    mapheight = 40;
    generate_tree_map(tree_map_data, anchor);
  };

  var generate_tree_map = function(tree_map_data, anchor){

    var visualization = d3plus.viz()
    .container(anchor)    // container DIV to hold the visualization
    .height(calcY(mapheight))
    .data(tree_map_data)  // data to use with the visualization
    .type("tree_map")     // visualization type
    .id("key")           // key for which our data is unique on
    .size("value")        // sizing of blocks
    .draw();

    d3plus.textwrap().container('.d3plus_label').resize(true).size(6,30);

  };

  var init_data = function(data){
    var frequency_list = [];
      for (var i = 0; i < data.length; i++){
        var entry = {"name":data[i].key, "size":data[i].value};
        frequency_list.push(entry);
      } 
    return frequency_list;
  };

  var calcX = function(width){
    return ($(window).width()*(width/100));
  };

  var calcY = function(height){
    return ($(window).height()*(height/100));
  };

  that.init = init;

  return that;
}

var json = $.getJSON("https://www.quandl.com/api/v3/datasets/YAHOO/MSFT.json?start_date=2015-01-03&end_date=2015-02-03&order=asc");
var stockCodes;
json.complete(function() {

stockCodes = json.responseJSON;
console.log(stockCodes);


var start_date = stockCodes.dataset.start_date;
var end_date = stockCodes.dataset.end_date;
var stockData = stockCodes.dataset.data;

var parseDate = d3.time.format("%y-%b-%d").parse;

//d3 margin convention
var margin = {top: 20, right: 20, bottom: 30, left: 35},
    width = 660 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// Set the ranges
var	x = d3.time.scale().range([0,width]);
var	y = d3.scale.linear().range([height, 0]);

var line = d3.svg.line()
    .x(function(d) { return x(d[0]); })
    .y(function(d) { return y(d[4]); });

stockData.forEach(function(d) {
        d[0] = new Date(d[0]);
        d[4] = +d[4];
        console.log(d[4]);
    });

// Define the axes
x.domain(d3.extent(stockData, function(d) { return d[0]; }));
y.domain(d3.extent(stockData, function(d) { return d[4]; }));
var	xAxis = d3.svg.axis().scale(x)
	.orient("bottom").ticks(5);

var	yAxis = d3.svg.axis().scale(y)
	.orient("left").ticks(10);


var svg = d3.select(".chart").append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');


  svg.append("rect")
      .attr("width", "100%")
      .attr("height", "100%")
      .attr("fill", "white");

    // Add the X Axis
	svg.append("g")
		.attr("class", "x axis")
		.attr("transform", "translate(" + margin.left + "," + (margin.top + height) + ')')
		.call(xAxis);


	// Add the Y Axis
	svg.append("g")
		    .attr("class", "y axis")
        .attr("transform", "translate(" + margin.left + ','+ margin.top + ')')
		    .call(yAxis)
    .append("text")
        .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy", ".71em")
    .attr("fill", "black")
    .style("text-anchor", "end")
    .text("Price ($)");

  svg.append("path")
     .datum(stockData)
        .attr("class", "line")
     .attr("transform", "translate(" + margin.left + ','+ margin.top + ')')
        .attr("d", line);




  });

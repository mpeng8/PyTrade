
  //var data = [4, 8, 15, 16, 23, 42];
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
var margin = {top: 20, right: 80, bottom: 50, left: 100},
width = 750,
height = 500 - margin.top-margin.bottom;

// Set the ranges
var	x = d3.time.scale().range([0,width]);
var	y = d3.time.scale().range([height, 0]);
var line = d3.svg.line()
    .x(function(d) { return x(d[0]); })
    .y(function(d) { return y(d[4]); });

stockData.forEach(function(d) {
        d[0] = new Date(d[0]);
        console.log(d[0]);
    });
// Define the axes
x.domain(d3.extent(stockData, function(d) { return d[0]; }));
y.domain(d3.extent(stockData, function(d) { return d[4]; }));
var	xAxis = d3.svg.axis().scale(x)
	.orient("bottom").ticks(5);

var	yAxis = d3.svg.axis().scale(y)
	.orient("left").ticks(10);


var svg = d3.select(".chart").append("svg")
  .attr("width", 750)
  .attr("height", 500)
  .style("border", "1px solid black");

    // Add the X Axis
	svg.append("g")
		.attr("class", "x axis")
		.attr("transform", "translate(0," + height + ")")
		.call(xAxis);

	// Add the Y Axis
	svg.append("g")
		.attr("class", "y axis")
    .attr("transform", "translate(" + width + ",0)")
		.call(yAxis)
    .append("text")
    .attr("y", 6)
    .attr("dy", ".71em")
    .style("text-anchor", "end")
    .text("Price ($)");

    svg.append("path")
        .datum(stockData)
        .attr("class", "line")
        .attr("d", line);




  });

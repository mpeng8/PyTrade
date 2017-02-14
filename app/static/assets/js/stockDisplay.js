
var stockID = document.getElementById("stockID_info").innerText;
console.log(stockID);

var json = $.getJSON("https://www.quandl.com/api/v3/datasets/YAHOO/" + stockID+".json?start_date=2015-01-03&end_date=2015-02-03&order=asc");

json.complete(function() {

    var stockCodes = json.responseJSON;
    console.log(stockCodes);

    var start_date = stockCodes.dataset.start_date;
    var end_date = stockCodes.dataset.end_date;
    var stockData = stockCodes.dataset.data;

    //d3 margin convention
    var margin = {top: 20, right: 20, bottom: 30, left: 35},
      width = 770 - margin.left - margin.right,
      height = 400 - margin.top - margin.bottom;

    // Set the ranges
    var	x = d3.time.scale().range([0,width]);
    var	y = d3.scale.linear().range([height, 0]);

    var line = d3.svg.line()
    .x(function(d) { return x(d[0]); })
    .y(function(d) { return y(d[4]); });

    //parseDate
    stockData.forEach(function(d) {
        d[0] = new Date(d[0]);
    });

    var minN = d3.min(stockData, function (d) { return d[0]; }).getTime(),
        maxN = d3.max(stockData, function (d) { return d[0]; }).getTime();
    var minDate = new Date(minN - 8.64e7),
        maxDate = new Date(maxN + 8.64e7);
    var yMin = d3.min(stockData, function (d) { return d[3]; }),
        yMax = d3.max(stockData, function (d) { return d[2]; });

    // Define the axes
    x.domain([minDate, maxDate]);
    y.domain([yMin, yMax]).nice();

    var	xAxis = d3.svg.axis().scale(x)
	      .orient("bottom").ticks(5);
    var	yAxis = d3.svg.axis().scale(y)
	      .orient("left").ticks(10);


    var svg = d3.select(".chart").append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');



  var navWidth = width,
      navHeight = 100 - margin.top - margin.bottom;

  var navChart = d3.select('.chart').classed('chart', true).append('svg')
      .classed('navigator', true)
      .attr('width', navWidth + margin.left + margin.right)
      .attr('height', navHeight + margin.top + margin.bottom)
      .append('g')
      .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');
      var navXScale = d3.time.scale()
              .domain([minDate, maxDate])
              .range([0, navWidth]),
          navYScale = d3.scale.linear()
              .domain([yMin, yMax])
              .range([navHeight, 0]);

              var navXAxis = d3.svg.axis()
    .scale(navXScale)
    .orient('bottom');

navChart.append('g')
    .attr('class', 'x axis')
    .attr('transform', 'translate(0,' + navHeight + ')')
    .call(navXAxis);

    var navData = d3.svg.area()
    .x(function (d) { return navXScale(d[0]); })
    .y0(navHeight)
    .y1(function (d) { return navYScale(d[4]); });

var navLine = d3.svg.line()
    .x(function (d) { return navXScale(d[0]); })
    .y(function (d) { return navYScale(d[4]); });

navChart.append('path')
    .attr('class', 'data')
    .attr('d', navData(stockData));

navChart.append('path')
    .attr('class', 'line')
    .attr('d', navLine(stockData));

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

    svg.selectAll("rect")
      .data(stockData)
      .enter().append("svg:rect")
        	  .attr("x", function(d) { return x(d[0]); })
            .attr("y", function(d) {return y(Math.max(d[1], d[4]));})
        	  .attr("height", function(d) { return y(Math.min(d[1], d[4]))-y(Math.max(d[1], d[4]));})
        	  .attr("width", function(d) { return 0.5 * (width - 2*50)/stockData.length; })
            .attr("transform", "translate(" + (margin.left-(0.5 * (width - 2*50)/stockData.length)*.5) + ','+ margin.top + ')')
            .attr("fill",function(d) { return d[1] > d[4] ? "red" : "green" ;});

    svg.selectAll("line.stem")
              .data(stockData)
              .enter().append("svg:line")
              .attr("class", "stem")
              .attr("transform", "translate(" + (margin.left-(0.5 * (width - 2*50)/stockData.length)*.5) + ','+ margin.top + ')')
              .attr("x1", function(d) { return x(d[0]) + 0.25 * (width - 2 * 50)/ stockData.length;})
              .attr("x2", function(d) { return x(d[0]) + 0.25 * (width - 2 * 50)/ stockData.length;})
              .attr("y1", function(d) { return y(d[2]);})
              .attr("y2", function(d) { return y(d[3]); })
              .attr("stroke", function(d){ return d[1] > d[4] ? "red" : "green"; })



});

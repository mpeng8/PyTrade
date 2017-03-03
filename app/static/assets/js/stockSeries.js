function stock(data){
  this.open = data[2];
  this.close = data[5];
  this.date = new Date(data[1]);
  this.high = data[3];
  this.low =data[4];
}


var stockID = document.getElementById("stockID_info").innerText;
//console.log(stockID);

var todayDate = new Date();
//console.log(todayDate);
var oldDate = new Date();
oldDate.setDate(todayDate.getDate() - 30);
//console.log(oldDate);

var dateLT = todayDate.toJSON().slice(0,10).replace(/-/g,'');
var dateGTE = oldDate.toJSON().slice(0,10).replace(/-/g,'');
console.log(dateGTE);

$.ajax({
    crossOrigin: true,
    url: "https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?date.gte="+dateGTE+"&date.lt=" + dateLT+"&ticker=" + stockID+"&api_key=sXBsPYtsefUf_qaFxNDK",
    success: function(data) {
      //console.log(data);
      var stockCodes = JSON.parse(data);
      var length = stockCodes.datatable.data.length;
      var stockData = [];
      for (var i = 0; i < length; i++) {
        stockData.push(new stock(stockCodes.datatable.data[i]));
          //console.log(stockData[i]);
      }
      //d3 margin convention
      var margin = {top: 20, right: 20, bottom: 30, left: 35},
          width = 770 - margin.left - margin.right,
          height = 400 - margin.top - margin.bottom;

      var xScale = d3.time.scale(),
          yScale = d3.scale.linear();

      var xAxis = d3.svg.axis()
          .scale(xScale)
          .orient('bottom')
          .ticks(5);

      var yAxis = d3.svg.axis()
          .scale(yScale)
          .orient('left');

      var series = candlestick ()
          .xScale(xScale)
          .yScale(yScale);

        // var gridlines = gridlines ()
        //     .xScale(xScale)
        //     .yScale(yScale)
        //     .xTicks(10)
        //     .yTicks(5);

      var svg = d3.select('.chart').append('svg')
                  .attr('width', width + margin.left + margin.right)
                  .attr('height', height + margin.top + margin.bottom);

        // Create chart
      var g = svg.append('g')
                 .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

      // Create plot area
      var plotArea = g.append('g');

      plotArea.append('clipPath')
              .attr('id', 'plotAreaClip')
              .append('rect')
              .attr({ width: width, height: height });

      plotArea.attr('clip-path', 'url(#plotAreaClip)');

        // Set scale domains
      var minN = d3.min(stockData, function (d) { return d.date; }).getTime(),
          maxN = d3.max(stockData, function (d) { return d.date; }).getTime();
      var minDate = new Date(minN - 8.64e7),
          maxDate = new Date(maxN + 8.64e7);
      var yMin = d3.min(stockData, function (d) { return d.low; }),
          yMax = d3.max(stockData, function (d) { return d.high; });

        // There are 8.64e7 milliseconds in a day.
      xScale.domain([
          new Date(maxDate.getTime() - (8.64e7 * 31.5)),
          new Date(maxDate.getTime() + 8.64e7)
      ]);

      yScale.domain(
          [
              d3.min(stockData, function (d) {
                return d.low;
              }),
              d3.max(stockData, function (d) {
                return d.high;
            })
          ]
      ).nice();

      // Set scale ranges
      xScale.range([0, width]);
      yScale.range([height, 0]);
      // Draw axes
      g.append('g')
      .attr('class', 'x axis')
      .attr('transform', 'translate(0,' + height + ')')
      .call(xAxis);

      g.append('g')
      .attr('class', 'y axis')
      .call(yAxis);

      // plotArea.call(gridlines);

      // Draw the series.
      var dataSeries = plotArea.append('g')
      .attr('class', 'series')
      .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')
      .datum(stockData)
      .call(series);


      var navWidth = width,
      navHeight = 100 - margin.top - margin.bottom;

      var navChart = d3.select('.chart').append('svg')
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
        .x(function (d) { return navXScale(d.date); })
        .y0(navHeight)
        .y1(function (d) { return navYScale(d.close); });

      var navLine = d3.svg.line()
        .x(function (d) { return navXScale(d.date); })
        .y(function (d) { return navYScale(d.close); });

      navChart.append('path')
        .attr('class', 'data')
        .attr('d', navData(stockData));

      navChart.append('path')
        .attr('class', 'line')
        .attr('d', navLine(stockData));

      function redrawChart() {
          dataSeries.call(series);
          svg.select('.x.axis').call(xAxis);
      }

      function updateViewportFromChart() {
          if ((xScale.domain()[0] <= minDate) && (xScale.domain()[1] >= maxDate)) {
              viewport.clear();
          } else {
              viewport.extent(xScale.domain());
          }
          navChart.select('.viewport').call(viewport);
      }

      function updateZoomFromChart() {
          zoom.x(xScale);
          var fullDomain = maxDate - minDate,
              currentDomain = xScale.domain()[1] - xScale.domain()[0];
          var minScale = currentDomain / fullDomain,
              maxScale = minScale * 20;
          zoom.scaleExtent([minScale, maxScale]);
      }

      var viewport = d3.svg.brush()
      .x(navXScale)
      .on("brush", function () {
          xScale.domain(viewport.empty() ? navXScale.domain() : viewport.extent());
          redrawChart();
      });

      var zoom = d3.behavior.zoom()
      .x(xScale)
      .on('zoom', function() {
          if (xScale.domain()[0] < minDate) {
  	    var x = zoom.translate()[0] - xScale(minDate) + xScale.range()[0];
              zoom.translate([x, 0]);
          } else if (xScale.domain()[1] > maxDate) {
  	    var x = zoom.translate()[0] - xScale(maxDate) + xScale.range()[1];
              zoom.translate([x, 0]);
          }
          redrawChart();
          updateViewportFromChart();
      });

      var overlay = d3.svg.area()
          .x(function (d) { return xScale(d.date); })
          .y0(0)
          .y1(height);

      plotArea.append('path')
          .attr('class', 'overlay')
          .attr('d', overlay(stockData))
          .call(zoom);

      viewport.on("brushend", function () {
          updateZoomFromChart();
      });

      navChart.append("g")
          .attr("class", "viewport")
          .call(viewport)
          .selectAll("rect")
          .attr("height", navHeight);

      var daysShown = 12;

      xScale.domain([
          stockData[stockData.length - daysShown - 1].date,
          stockData[stockData.length - 1].date
      ]);

      redrawChart();
      updateViewportFromChart();
      updateZoomFromChart();
    },
  error: function(xhr, textStatus, errorThrown) {
    // Handle error
  }
});

function stock(data){
  this.open = data[2];
  this.close = data[5];
  this.date = new Date(data[1]);
  this.high = data[3];
  this.low =data[4];
  this.volume=data[6];
}

function createCORSRequest(method, url) {
  var xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {
    // Check if the XMLHttpRequest object has a "withCredentials" property.
    // "withCredentials" only exists on XMLHTTPRequest2 objects.
    xhr.open(method, url, true);
  } else if (typeof XDomainRequest != "undefined") {
    // Otherwise, check if XDomainRequest.
    // XDomainRequest only exists in IE, and is IE's way of making CORS requests.
    xhr = new XDomainRequest();
    xhr.open(method, url);
  } else {
    // Otherwise, CORS is not supported by the browser.
    xhr = null;
  }
  return xhr;
}

var stockIDs = document.getElementById("stockID_info").innerText;
var endDate = new Date();
console.log(endDate);
var oldDate = new Date();
oldDate.setDate(endDate.getDate() - 30);
$.ajax({
  type:"GET",
  url:"/getTime",
  success: function(time) {
    dates = time.data;
    if (dates['startDate'].length > 1) {
      oldDate = new Date(dates['startDate']);
    }
    if (dates['endDate'].length > 1) {
      endDate = new Date(dates['endDate']);
    }


var dateLT = endDate.toJSON().slice(0,10).replace(/-/g,'');
var dateGTE = oldDate.toJSON().slice(0,10).replace(/-/g,'');
console.log(dateGTE);
console.log(dateLT);
var url = "https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?date.gte="+dateGTE+"&date.lt=" + dateLT+"&ticker=" + stockIDs+"&api_key=sXBsPYtsefUf_qaFxNDK";

var xhr = createCORSRequest('GET', url);

if (!xhr) {
  throw new Error('CORS not supported');
}

xhr.onload = function() {
 var responseText = xhr.responseText;
 var stockCodes = JSON.parse(responseText);
 console.log(stockCodes);
 var length = stockCodes.datatable.data.length;
 var stockData = [];
 for (var i = 0; i < length; i++) {
   stockData.push(new stock(stockCodes.datatable.data[i]));
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
svg.append("rect")
                 .attr("width", "100%")
                 .attr("height", "100%")
                 .attr("fill", "white");

   // Create chart
 var g = svg.append('g')
            .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');
            svg.selectAll("line.horizontalGrid").data(yScale.ticks(4)).enter()
                .append("line")
                    .attr(
                    {
                        "class":"horizontalGrid",
                        "x1" : margin.right,
                        "x2" : width,
                        "y1" : function(d){ return yScale(d);},
                        "y2" : function(d){ return yScale(d);},
                        "fill" : "none",
                        "shape-rendering" : "crispEdges",
                        "stroke" : "black",
                        "stroke-width" : "1px"
                    });
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
 var minDate = new Date(minN),
     maxDate = new Date(maxN);
 var yMin = d3.min(stockData, function (d) { return d.low; }),
     yMax = d3.max(stockData, function (d) { return d.high; });
yScale.domain([yMin, yMax]).nice();

// There are 8.64e7 milliseconds in a day.
document.getElementById("today_open_price").innerText=stockData[length-1].open;
document.getElementById("today_high_price").innerText=stockData[length-1].high;
document.getElementById("today_close_price").innerText=stockData[length-1].close;
document.getElementById("today_low_price").innerText=stockData[length-1].low;
document.getElementById("today_volume").innerText=stockData[length-1].volume;

 xScale.domain([
     new Date(maxDate.getTime() - (8.64e7 * 31.5)),
     new Date(maxDate.getTime())
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
  .attr('transform', 'translate('+margin.left +', '+ height + ')')
  .call(xAxis);

 g.append('g')
 .attr('class', 'y axis')
 .call(yAxis);



 // Draw the series.
 var dataSeries = plotArea.append('g')
 .attr('class', 'series')
 .attr('transform', 'translate(0'  + ',' + margin.top + ')')
 .datum(stockData)
 .call(series)


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

   var trackers = tracker()
           .xScale(xScale)
           .yScale(yScale)
           .yValue('close')
           .movingAverage(5)
           .css('tracker-close-avg');

  var movingAverage = plotArea.append('g')
          .attr('class', 'trackers')
          .datum(stockData)
          .call(trackers);



 function redrawChart() {
     dataSeries.call(series);
     movingAverage.call(trackers);
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


var crosshair = crosshairs()
                 .target(plotArea)
                 .series(stockData)
                 .xScale(xScale)
                 .yScale(yScale);

plotArea.append('path')
        .attr('class', 'overlay')
        .attr('d', overlay(stockData))
        .call(crosshair);
};

xhr.onerror = function() {
    alert('Woops, there was an error making the request.');
};

xhr.send();

}
});

crosshairs = function () {

    var target = null,
        series = null,
        xScale = d3.time.scale(),
        yScale = d3.scale.linear(),
        yValue = 'close',
        formatH = function(data) { return d3.format('.1f')(data.close); },
        formatV = function(data) { return d3.time.format('%b %e')(data.date); };

    var lineH = null,
        lineV = null,
        circle = null,
        calloutH = null,
        calloutV = null;

    var highlight = null;
    var margin = {top: -6, right: 20, bottom: 30, left: 35};

    var crosshairs = function (selection) {

        var root = target.append('g')
            .attr('class', 'crosshairs');

        lineH = root.append("line")
            .attr('class', 'crosshairs horizontal')
            .attr('x1', xScale.range()[0])
            .attr('x2', xScale.range()[1])
            .attr('display', 'none');

        lineV = root.append("line")
            .attr('class', 'crosshairs vertical')
            .attr('y1', yScale.range()[0])
            .attr('y2', yScale.range()[1])
            .attr('display', 'none');

        circle = root.append("circle")
            .attr('class', 'crosshairs circle')
            .attr('r', 6)
            .attr('display', 'none');

        calloutH = root.append("text")
            .attr('class', 'crosshairs callout horizontal')
            .attr('x', xScale.range()[1])
            .attr('style', 'text-anchor: end')
            .attr('display', 'none');

        calloutV = root.append("text")
            .attr('class', 'crosshairs callout vertical')
            .attr('y', '1em')
            .attr('style', 'text-anchor: end')
            .attr('display', 'none');
    };

    function mousemove() {

        var xMouse = xScale.invert(d3.mouse(this)[0]),
            nearest = findNearest(xMouse);

        if ((nearest !== null) && (nearest !== highlight)) {

            highlight = nearest;

            var x = xScale(highlight.date),
                y = yScale(highlight[yValue]);

            lineH.attr('y1', y)
                .attr('y2', y);
            lineV.attr('x1', x)
                .attr('x2', x);
            circle.attr('cx', x)
                .attr('cy', y);
            calloutH.attr('y', y)
                .text(formatH(highlight));
            calloutV.attr('x', x)
                .text(formatV(highlight));

            lineH.attr('display', 'inherit');
            lineV.attr('display', 'inherit');
            circle.attr('display', 'inherit');
            calloutH.attr('display', 'inherit');
            calloutV.attr('display', 'inherit');
            document.getElementById('select_high_price').innerText="High: "+nearest.high+", "+"Low: "+nearest.low;
            document.getElementById('select_open_price').innerText="Open: "+nearest.open+", "+"Close: "+nearest.close;
            document.getElementById('popup').style.display='block';

        }
    }

    function mouseout() {

        highlight = null;

        lineH.attr('display', 'none');
        lineV.attr('display', 'none');
        circle.attr('display', 'none');
        calloutH.attr('display', 'none');
        calloutV.attr('display', 'none');
        document.getElementById('popup').style.display='none';
    }

    function findNearest(xMouse) {

        var nearest = null,
            dx = Number.MAX_VALUE;

        series.forEach(function(data) {

            var xData = data.date,
                xDiff = Math.abs(xMouse.getTime() - xData.getTime());

            if (xDiff < dx) {
                dx = xDiff;
                nearest = data;
            }
        });

        return nearest;
    }
    crosshairs.series = function(value) {
      if (!arguments.length) {
          return series;
      }
      series = value;
      return crosshairs;
    }
    crosshairs.xScale = function(value) {
      if (!arguments.length) {
        return xScale;
      }
      xScale=value;
      return crosshairs;
    }
    crosshairs.yScale = function(value) {
      if (!arguments.length) {
        return yScale;
      }
      yScale = value;
      return crosshairs;
    }
    crosshairs.target = function (value) {
        if (!arguments.length) {
            return target;
        }

        if (target) {
            target.on('mousemove.crosshairs', null);
            target.on('mouseout.crosshairs', null);
        }

        target = value;

        target.on('mousemove.crosshairs', mousemove);
        target.on('mouseout.crosshairs', mouseout);

        return crosshairs;
    };

    // ... other property accessors omitted, but they'd go here

    return crosshairs;
};

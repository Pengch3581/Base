$(function() {
    var width = 960,
        height = 136,
        cellSize = 17;

    var month_init = 20;
    var month_arr = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    var week_init = 20;
    var week_arr = ['Mon', 'Web', 'Fri']

    var formatPercent = d3.format(".1%");

    var color = d3.scaleQuantize()
        // .domain([-0.05, 0.05])
        // .range(["#a50026", "#d73027", "#f46d43", "#fdae61", "#fee08b", "#ffffbf", "#d9ef8b", "#a6d96a", "#66bd63",
        // "#1a9850", "#006837"
        // ]);
        .domain([1, 5])
        .range(["#ebedf0", "#c6e48b", "#7bc96f", "#239a3b", "#196127"]);

    var svg = d3.select("#" + "fault-body")
        .selectAll("svg")
        // .data(d3.range(1990, 2011))
        .data([2018])
        .enter().append("svg")
        .attr("width", width)
        .attr("height", height)
        .append("g")
        .attr("transform", "translate(" + ((width - cellSize * 53) / 2) + "," + (height - cellSize * 7 - 1) + ")");

    // svg.append("text")
    //     .attr("transform", "translate(-6," + cellSize * 3.5 + ")rotate(-90)")
    //     .attr("font-family", "sans-serif")
    //     .attr("font-size", 10)
    //     .attr("text-anchor", "middle")
    //     .text(function(d) {
    //         return d;
    //     });

    // add 月份
    month_arr.forEach(function(e) {
        svg.append("text")
            .text(e)
            .attr("font-family", "sans-serif")
            .attr("font-size", 12)
            .attr("fill", "#767676")
            .attr("transform", "translate(" + month_init + "," + cellSize * -0.3 + ")")
        month_init += 75;
    })

    // add 星期
    week_arr.forEach(function(e) {
        svg.append("text")
            .text(e)
            .attr("font-family", "sans-serif")
            .attr("font-size", 9)
            .attr("fill", "#767676")
            .attr("transform", "translate(-6 ," + (cellSize + week_init) + ")rotate(-90)")
        week_init += 31;
    })


    var rect = svg.append("g")
        // .attr("fill", "none")
        .attr("fill", "rgb(235, 237, 240)")
        // .attr("stroke", "#ccc")
        .attr("stroke", "#FFFFFF")
        .attr("stroke-width", "3")
        // .attr("stroke", "#000")
        .selectAll("rect")
        .data(function(d) {
            return d3.timeDays(new Date(d, 0, 1), new Date(d + 1, 0, 1));
        })
        .enter().append("rect")
        .attr("width", cellSize)
        .attr("height", cellSize)
        .attr("x", function(d) {
            return d3.timeWeek.count(d3.timeYear(d), d) * cellSize;
        })
        .attr("y", function(d) {
            return d.getDay() * cellSize;
        })
        .datum(d3.timeFormat("%Y-%m-%d"));

    // 月份实线
    // svg.append("g")
    //     .attr("fill", "none")
    //     // .attr("stroke", "#000")
    //     .attr("stroke", "#ffffff")
    //     .attr("fill", "rgb(235, 237, 240)")
    //     .selectAll("path")
    //     .data(function(d) {
    //         return d3.timeMonths(new Date(d, 0, 1), new Date(d + 1, 0, 1));
    //     })
    //     .enter().append("path")
    //     .attr("d", pathMonth);

    d3.csv("dji.csv", function(error, csv) {
        if (error) throw error;

        var data = d3.nest()
            .key(function(d) {
                return d.Date;
            })
            .rollup(function(d) {
                return (d[0].Close - d[0].Open) / d[0].Open;
            })
            .object(csv);

        rect.filter(function(d) {
                return d in data;
            })
            .attr("fill", function(d) {
                return color(data[d]);
            })
            .append("title")
            .text(function(d) {
                return d + ": " + formatPercent(data[d]);
            });
    });

    function pathMonth(t0) {
        var t1 = new Date(t0.getFullYear(), t0.getMonth() + 1, 0),
            d0 = t0.getDay(),
            w0 = d3.timeWeek.count(d3.timeYear(t0), t0),
            d1 = t1.getDay(),
            w1 = d3.timeWeek.count(d3.timeYear(t1), t1);
        return "M" + (w0 + 1) * cellSize + "," + d0 * cellSize +
            "H" + w0 * cellSize + "V" + 7 * cellSize +
            "H" + w1 * cellSize + "V" + (d1 + 1) * cellSize +
            "H" + (w1 + 1) * cellSize + "V" + 0 +
            "H" + (w0 + 1) * cellSize + "Z";
    }
})
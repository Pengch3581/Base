$(function() {
    chart = new Highcharts.Chart({
        chart: {
            type: 'columnrange', // columnrange 依赖 highcharts-more.js
            renderTo: 'container-operation',
            inverted: true
        },
        title: {
            text: '游戏列表--运营中'
        },
        subtitle: {
            text: '(共 12 款游戏)'
        },
        xAxis: {
            categories: ['gcmob', 'tjmob', 'gcmob', 'tjmob', 'gcmob', 'tjmob', 'gcmob', 'tjmob', 'gcmob', 'tjmob', 'gcmob', 'tjmob']
        },
        yAxis: {
            title: {
                text: '年份 ( y )'
            }
        },
        tooltip: {
            valueSuffix: '年'
        },
        plotOptions: {
            columnrange: {
                dataLabels: {
                    enabled: true,
                    formatter: function() {
                        return this.y + '年';
                    }
                }
            }
        },
        legend: {
            enabled: false
        },
        series: [{
            name: '年份',
            // colorByPoint: true,
            data: [
                [2010, 2018],
                [2014, 2018],
                [2010, 2018],
                [2013, 2018],
                [2011, 2018],
                [2011, 2018],
                [2015, 2018],
                [2011, 2018],
                [2010, 2018],
                [2017, 2018],
                [2010, 2018],
                [2011, 2018]
            ]
        }]
    });
})

$(function() {
    chart = new Highcharts.Chart({
        chart: {
            type: 'columnrange', // columnrange 依赖 highcharts-more.js
            renderTo: 'container-non',
            inverted: true
        },
        title: {
            text: '游戏列表--未上线'
        },
        subtitle: {
            text: '(共 12 款游戏)'
        },
        xAxis: {
            categories: ['gcmob', 'tjmob', 'gcmob', 'tjmob', 'gcmob', 'tjmob', 'gcmob', 'tjmob', 'gcmob', 'tjmob', 'gcmob', 'tjmob']
        },
        yAxis: {
            title: {
                text: '年份 ( y )'
            }
        },
        tooltip: {
            valueSuffix: '年'
        },
        plotOptions: {
            columnrange: {
                dataLabels: {
                    enabled: true,
                    formatter: function() {
                        return this.y + '年';
                    }
                }
            }
        },
        legend: {
            enabled: false
        },
        series: [{
            name: '年份',
            // colorByPoint: true,
            data: [
                [2010, 2018],
                [2014, 2018],
                [2010, 2018],
                [2013, 2018],
                [2011, 2018],
                [2011, 2018],
                [2015, 2018],
                [2011, 2018],
                [2010, 2018],
                [2017, 2018],
                [2010, 2018],
                [2011, 2018]
            ]
        }]
    });
})
$(function() {
    chart = new Highcharts.Chart({
        chart: {
            type: 'columnrange', // columnrange 依赖 highcharts-more.js
            renderTo: 'container-out',
            inverted: true
        },
        title: {
            text: '游戏列表--已下线'
        },
        subtitle: {
            text: '(共 12 款游戏)'
        },
        xAxis: {
            categories: ['gcmob', 'tjmob', 'gcmob', 'tjmob', 'gcmob', 'tjmob', 'gcmob', 'tjmob', 'gcmob', 'tjmob', 'gcmob', 'tjmob']
        },
        yAxis: {
            title: {
                text: '年份 ( y )'
            }
        },
        tooltip: {
            valueSuffix: '年'
        },
        plotOptions: {
            columnrange: {
                dataLabels: {
                    enabled: true,
                    formatter: function() {
                        return this.y + '年';
                    }
                }
            }
        },
        legend: {
            enabled: false
        },
        series: [{
            name: '年份',
            // colorByPoint: true,
            data: [
                [2010, 2015],
                [2014, 2014],
                [2010, 2014],
                [2013, 2014],
                [2011, 2015],
                [2011, 2017],
                [2015, 2017],
                [2011, 2018],
                [2010, 2018],
                [2017, 2018],
                [2010, 2018],
                [2011, 2018]
            ]
        }]
    });
})
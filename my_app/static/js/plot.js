$(document).ready(function () {

    console.log("tada!");

    $('#plot').highcharts({
        chart: {
            type: 'columnrange',
            inverted: true
        },

        title: {
            text: 'Crowd in Winter Park, CO'
        },

        subtitle: {
            text: 'Percentage of Maximum Crowd Size'
        },
        //this should be dates
        xAxis: {
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        },

        yAxis: {
            title: {
                text: 'Percentage of Maximum Skiers'
            }
        },

        tooltip: {
            valueSuffix: '°C'
        },

        plotOptions: {
            columnrange: {
                dataLabels: {
                    enabled: false,
                    formatter: function () {
                        return this.y + '°C';
                    }
                }
            }
        },

        legend: {
            enabled: false
        },

        series: [{
            name: 'Percentage of Maximum',
            data: [
                [-10, 9.4],
                [-8.7, 6.5],
                [-3.5, 9.4],
                [-1.4, 19.9],
                [0.0, 22.6],
                [2.9, 29.5],
                [9.2, 30.7],
                [7.3, 26.5],
                [4.4, 18.0],
                [-3.1, 11.4],
                [-5.2, 10.4],
                [-13.5, 9.8]
            ]
        }]

    });

});

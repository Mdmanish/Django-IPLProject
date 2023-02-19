const question_url = document.getElementById('question_url').innerHTML;
const graph_title = document.getElementById('title').innerHTML;
const xAxisContent = document.getElementById('xAxis').innerHTML;
const yAxisContent = document.getElementById('yAxis').innerHTML;
const xLable = document.getElementById('xLable').innerHTML;
const yLable = document.getElementById('yLable').innerHTML;
const graphType = document.getElementById('graphType').innerHTML;

fetch(question_url)
    .then((response) => {
        json_value = response.json()
        return json_value
    })
    .then((data) => {

        var xTicksValues = []
        var seriesValue = []
        var isGroupedChat = false

        if (graphType === 'bar') {
            const yValue = []
            for (let obj in data) {
                xTicksValues.push(data[obj][xAxisContent]);
                yValue.push(data[obj][yAxisContent]);
            }
            seriesValue.push({ data: yValue });
        }
        else {
            var groupedValue = {}
            for (let obj in data) {
                if (data[obj][xAxisContent] in groupedValue) {
                    groupedValue[data[obj][xAxisContent]][parseInt(data[obj]['season']) - 2008] += data[obj][yAxisContent];
                }
                else {
                    groupedValue[data[obj][xAxisContent]] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    groupedValue[data[obj][xAxisContent]][parseInt(data[obj]['season']) - 2008] += data[obj][yAxisContent];
                    xTicksValues.push(data[obj][xAxisContent]);
                }
            }
            console.log(groupedValue)
            for (var i = 2008; i <= 2017; i++) {
                var val = []
                for (var key in groupedValue) {
                    val.push(groupedValue[key][i - 2008])
                }
                seriesValue.push({
                    name: i,
                    data: val
                });
            }

            Highcharts.setOptions({
                colors: [
                    "red",
                    "green",
                    "blue",
                    "orange",
                    "brown",
                    "yellow",
                    "#77a1e5",
                    "#c42525",
                    "#a6c96a",
                    "pink",
                ]
            })
            isGroupedChat = true
        }

        Highcharts.setOptions({
            chart: {
                backgroundColor: {
                    linearGradient: [0, 0, 500, 500],
                    stops: [
                        [0, 'rgb(255, 255, 255)'],
                        [1, 'rgb(240, 240, 255)']
                    ]
                },
                borderWidth: 2,
                plotBackgroundColor: 'rgba(255, 255, 255, .9)',
                plotShadow: true,
                plotBorderWidth: 1,
            }
        });

        Highcharts.chart("container", {
            chart: {
                type: "column",
                zoomType: "y"
            },
            title: {
                text: graph_title
            },
            xAxis: {
                categories: xTicksValues,
                title: {
                    text: xLable
                }
            },
            yAxis: {
                title: {
                    text: yLable
                },
                labels: {
                    overflow: 'justify'
                }
            },
            plotOptions: {
                column: {
                    dataLabels: {
                        enabled: true,
                        format: "{y}",

                    }
                }
            },
            tooltip: {
                stickOnContact: true,
                backgroundColor: "rgba(255, 255, 255, 0.93)"
            },
            legend: {
                enabled: isGroupedChat
            },
            series: seriesValue
        });
    })

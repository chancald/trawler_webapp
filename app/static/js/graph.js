
// Importing data from DOM
const tableData = JSON.parse(document.getElementById("table_data").dataset.table_data);
const graphData = JSON.parse(document.getElementById("graph_data").dataset.graph_data);
const predData = JSON.parse(document.getElementById("pred_data").dataset.pred_data);
const trawlerTable = document.getElementById('trawler-graph');

let activeStock = document.getElementById('0').firstElementChild.innerHTML;
document.querySelector('tbody').firstElementChild.id ='active-row'

document.querySelectorAll('.table-row').forEach(item => {
    item.addEventListener('click', event => {
        activeStock = event.currentTarget.firstElementChild.innerHTML;
        document.getElementById('active-row').removeAttribute('id');
        item.id = 'active-row';
        displayGraph();
    })
    })

document.querySelectorAll('.table-header').forEach(item => {
    item.addEventListener('click', event => {

        document.getElementById('active-col').removeAttribute('id');
        item.id = 'active-col';

        const columnName = event.currentTarget.innerHTML.toLowerCase();
        if (columnName in ['open', 'close', 'low', 'high']) {
          columnName = 'open'
        }
        console.log(columnName);
        const key = `${columnName}_top_10`;
        const top10Table = tableData[key];

        const tableBody = table.getElementsByTagName('tbody')[0];
        const tableHeader = table.rows[0]
        
        for (let i=0; i < tableBody.rows.length; i++) {
            let row = tableBody.rows[i];
            for (let j=0; j <= row.cells.length-1; j++) {
              const columnKey = tableHeader.cells[j].innerHTML.toLowerCase();
              row.cells[j].innerHTML = top10Table[i][columnKey];
              
            }
        }
        document.getElementById('active-row').removeAttribute('id');
        firstRow = document.querySelector('tbody').firstElementChild
        firstRow.id = 'active-row';
        activeStock = firstRow.firstElementChild.innerHTML
        displayGraph();
    })
    })

function displayGraph() {
    
    if (predData[activeStock][0] == 0) {
        document.getElementById('prediction').className = 'arrow-down'
        document.getElementById('pred-cont').innerHTML = 'Going down'
    }
    else if (predData[activeStock][0] == 1) {
        document.getElementById('prediction').className = 'horizontal-line'
        document.getElementById('pred-cont').innerHTML = 'Not changing'
    } 
    else {
        document.getElementById('prediction').className = 'arrow-up'
        document.getElementById('pred-cont').innerHTML = 'Going up'
    }
    
    var trace1 = {
        x: graphData[activeStock][0],
        y: graphData[activeStock][1],
        type: 'scatter',
        mode: 'lines',
        name: "Mentions",
        margin: { t: 0 }
      };
      
    var trace2 = {
        x: graphData[activeStock][0],
        y: graphData[activeStock][2],
        type: 'scatter',
        mode: 'lines',
        name: "Volume",
        margin: { t: 0 },
        yaxis: 'y2',
      };
      
    var data = [trace1, trace2];
    var layout = {
        title: `${activeStock} Stock`,
        width: 800,
        xaxis: {
            autorange: true,
            range: ['2021-04-01', '2021-06-27'],
            rangeselector: {buttons: [
                {
                  count: 1,
                  label: '1m',
                  step: 'month',
                  stepmode: 'backward'
                },
                {
                  count: 3,
                  label: '2m',
                  step: 'month',
                  stepmode: 'backward'
                },
                {step: 'all'}
              ]},
            rangeslider: {range: ['2021-04-01', '2021-06-27']},
            type: 'date'
          },
          yaxis: {
            title: 'Mentions',
            autorange: true,
            type: 'linear'
          },
          yaxis2: {
            title: 'Volume',
            overlaying: 'y',
            side: 'right'
          }
    };

    var config = {responsive: true};
    
    Plotly.newPlot(trawlerTable, data, layout, { margin: { t: 0 } });
    }

displayGraph();
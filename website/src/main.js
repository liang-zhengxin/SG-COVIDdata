const input = document.getElementById('value');
const progressValue = document.querySelector('.Progressbar__value');
const percent = document.querySelector('.percent');
const date = document.querySelector('.date');

function setValue(value) {
  progressValue.style.width = `${value}%`;
  percent.textContent = String(Math.round(value)) + "%"
}

const latestData = {
  "dailyLocalCases": {
      "06-07-2021": 2
  },
  "dailyVaxData": {
      "05-07-2021": {
          "total": 5858571,
          "first": 3670862,
          "completed": 2187709
      }
  }
};

fetch("api/latest.json")
  .then(response => response.json())
  .then(data=> {getValue(data)});

// getValue(latestData)
function getValue(latestData) {
  const pop = 5685800
  const t = Object.keys(latestData.dailyVaxData)
  var completed = latestData.dailyVaxData[t].completed
  date.textContent = "Updated: " + t + " Data: MOH Press Release"
  var percent =(completed/pop)*100
  setValue(percent)
}


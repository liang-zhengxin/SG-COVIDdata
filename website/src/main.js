const progressValue = document.querySelector('.Progressbar__value');
const percent = document.querySelector('.percent');
const date = document.querySelector('.date');

function setValue(value) {
  progressValue.style.width = `${value}%`;
  percent.textContent = String(Math.round(value)) + "%"
}

fetch("api/latest.json")
  .then(response => response.json())
  .then(data=> {getValue(data)});

function getValue(latestData) {
  const pop = 5685800
  const t = Object.keys(latestData.dailyVaxDataPercent)
  var completed = latestData.dailyVaxData[t].completed
  date.textContent = "Updated: " + t
  // var percent =(completed/pop)*100
  var percent = completed
  setValue(percent)
  // getMilestone(66-percent)
}

/*
// Adding Text Milestones
function getMilestone(percentageLeft) {
  const milestone = document.createElement("h4");
  if (percentageLeft <= 0) {
    //  block of code to be executed if the condition is true
    document.getElementById("target").innerHTML = "66% Vaccination Milestone Achieved";
  } else {
    var figure = document.createTextNode(String(Math.round(percentageLeft)) + "% remaining to achieve target");
    milestone.appendChild(figure);
    const element = document.querySelector('.Texttargets');
    element.appendChild(milestone);
  }
}
*/

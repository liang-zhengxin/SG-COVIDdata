fetch("api/latest.json")
    .then(response => response.json())
    .then(data=> {show(data)});

function show(data) {
    const t = Object.keys(data.dailyLocalCases)
    var cases = latestData.dailyLocalCases[t]
    document.getElementById("localcases").innerHTML = "There were " + String(cases) + " new locally transmitted cases"
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

  show(latestData)

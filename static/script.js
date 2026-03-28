var map = L.map('map').setView([20,78],5)

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
maxZoom:19
}).addTo(map)

var buildings = []

function generateBuildings(){

for(let i=0;i<10;i++){

let lat = 20 + Math.random()*5
let lon = 78 + Math.random()*5

let marker = L.marker([lat,lon]).addTo(map)

marker.bindPopup("Building")

buildings.push(marker)

}

}

generateBuildings()


function startSimulation(){

fetch('/earthquake')
.then(res=>res.json())
.then(data=>{

simulateDamage()

displayResults(data)

})
}


function simulateDamage(){

buildings.forEach(b=>{
b.bindPopup("Damaged Building")
})

addHospitals()

}


function addHospitals(){

for(let i=0;i<3;i++){

let lat = 20 + Math.random()*5
let lon = 78 + Math.random()*5

L.marker([lat,lon])
.addTo(map)
.bindPopup("Hospital")

}

}


function displayResults(data){

let div = document.getElementById("results")

div.innerHTML = `
FCFS Order: ${data.fcfs}<br>
SJF Order: ${data.sjf}<br>
Priority Order: ${data.priority}<br>
Round Robin Order: ${data.round_robin}
`

}
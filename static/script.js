var map = L.map('map').setView([22,77],5)

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
maxZoom:18
}).addTo(map)


function log(msg){

var logDiv=document.getElementById("log")

var p=document.createElement("div")

p.className="log"

p.innerText=msg

logDiv.appendChild(p)

}


function startSimulation(){

fetch("/start")
.then(res=>res.json())
.then(data=>{

map.eachLayer(function(layer){
if(layer instanceof L.Marker) map.removeLayer(layer)
})


var epic=data.epicenter

L.circle([epic.lat,epic.lng],{
radius:300000,
color:"red"
}).addTo(map)

log("Earthquake detected at epicenter")

data.people.forEach(p=>{

L.marker([p.lat,p.lng])
.addTo(map)
.bindPopup("Person "+p.id)

})

data.buildings.forEach(b=>{

L.marker([b.lat,b.lng])
.addTo(map)
.bindPopup("Building "+b.id)

})


log("Evacuation scheduling using SJF")

log("Medical scheduling using Priority")

log("Food distribution scheduled")

})
}
const mymap = L.map('mapid').setView([38.722252, -9.139337], 15);

var myMarker = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);
L.marker([51.5, -0.09]).addTo(mymap)
    .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
    .openPopup();
mymap.on('click',addMarker);

function addMarker(e){
//console.log(latlng.lat + ', ' + latlng.lng)
//L.marker([lat, lng]).addTo(mymap)
const {lat , lng} = e.latlng;
const marker = new L.marker(e.latlng, {
    draggable: true
  }).addTo(mymap)
.bindPopup(' Lat: '+ lat+ 'Long:'+ lng+' ')
.openPopup();
marker.on('click', removeMarker)
}

  function removeMarker(){
      const marker = this;
      mymap.removeLayer(marker);
  }

function chooseAddr(lat1, lng1)
{

console.log(lat1,lng1)
mymap.closePopup();
mymap.setView([lat1, lng1], 15);
const marker = new L.circleMarker([lat1,lng1], {
    draggable: true
  }).addTo(mymap)
marker.setLatLng([lat1, lng1]);
 lat = lat1.toFixed(8);
 lon = lng1.toFixed(8);
 document.getElementById('lat').value = lat;
 document.getElementById('lng').value = lon;
 marker.bindPopup("Lat " + lat + "<br />Lon " + lon).openPopup();
}

function myFunction(arr)
{
 var out = "<br />";
 var i;

 if(arr.length > 0)
 {
  for(i = 0; i < arr.length; i++)
  {
   out += "<div class='address' title='localizaçao e coordenadas' onclick='chooseAddr(" + arr[i].lat + ", " + arr[i].lon + ");return false;'>" + arr[i].display_name + "</div>";
  }
  document.getElementById('results').innerHTML = out;
 }
 else
 {
  document.getElementById('results').innerHTML = "Nao existe resultado ...";
 }

}

function address_search()
{
 var inp = document.getElementById("address");
 var xmlhttp = new XMLHttpRequest();
 var url = "https://nominatim.openstreetmap.org/search?format=json&limit=5&q=" + inp.value;
 xmlhttp.onreadystatechange = function()
 {
   if (this.readyState == 4 && this.status == 200)
   {
    var myArr = JSON.parse(this.responseText);
    myFunction(myArr);
   }
 };
 xmlhttp.open("GET", url, true);
 xmlhttp.send();
}

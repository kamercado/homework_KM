//link to geojson data
var link = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

// Create a map using Leaflet that plots all of the earthquakes from your data set based on their longitude and latitude.

// create map
var myMap = L.map("map", {
	center: [39.83, -98.58],
	zoom: 3
});
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

//create a GeoJSON layer
d3.json(link, function(data) {
	L.geoJSON(data, {
		pointToLayer: function (feature, latlng) {
			return L.circleMarker(latlng, {
				radius: setRadius(feature.properties.mag),
				fillColor: setColor(feature.properties.mag),
				color: setColor(feature.properties.mag),
				opacity: 1,
				weight: 0.75,
				fillOpacity: 0.25
			});
		}
	}).addTo(myMap)
});

// Function that will determine the color of marker based on magnitude
function setColor(magnitude) {
   	if (magnitude > 5) {
       	return '#FF0000'
   	} else if (magnitude > 4) {
       	return '#FF7C00'
   	} else if (magnitude > 3) {
       	return '#FFBE00'
   	} else if (magnitude > 2) {
       	return '#FFF500'
   	} else if (magnitude > 1) {
       	return '#AEFF00'
   	} else {
       	return '#39FF00'
   	}
}

//Function to set radius of circle marker based on magnitude
function setRadius(magnitude) {
	return magnitude * 2
}
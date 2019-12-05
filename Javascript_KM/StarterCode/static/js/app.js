// from data.js
var tableData = data;

// YOUR CODE HERE!

// Using the UFO dataset provided in the form of an array of JavaScript objects, write code that appends a table to your 
// web page and then adds new rows of data for each UFO sighting.

// Make sure you have a column for date/time, city, state, country, shape, and comment at the very least.
// Use a date form in your HTML document and write JavaScript code that will listen for events and search through the date/time 
// column to find rows that match user input.

// Get a reference to the table body
var tbody = d3.select("#ufo-table");

// Console.log the weather data from data.js
console.log(data);

// steps modeled from in-class activity

// Step 1: Loop Through `data` and console.log each UFO Sighting object
data.forEach(function(UFOSighting) {
  console.log(UFOSighting);
  // Step 2:  Use d3 to append one table row `tr` for each UFO Sighting object
  var row = tbody.append("tr");
// // Step 3:  Use `Object.entries` to console.log each UFO Sighting value]
  Object.entries(UFOSighting).forEach(function([key, value]) {
    console.log(key, value);
    // // Step 4: Use d3 to append 1 cell per UFO Sighting value
    var cell = row.append("td");
// Step 5: Use d3 to update each cell's text with
// UFO Sighting values
    cell.text(value);

  });
});


//Form / event listener


//Reference to button to filter data
var button = d3.select("#filter-btn")

button.on("click", function() {
//Reference to form's input box
	var inputBox = d3.select("#datetime")
	//value property of input
	var inputDate = inputBox.property("value");
	//check that it works
	console.log(inputDate)
//reference to filtered data
	var filteredSightings = tableData.filter(sighting => sighting.datetime === inputDate);
	console.log(filteredSightings);

// 	filteredSightings.forEach(function(filteredSighting) {
// 	// append one table row for each UFO sighting object
// 	//clear rows
// 	d3.selectAll("td").html("")
// 	var row = tbody.append("tr");
// // Use `Object.entries` to display each UFO Sighting value
// 	Object.entries(filteredSightings).forEach(function([key, value]) {
//     console.log(key, value);
//     // // Step 4: Use d3 to append 1 cell per UFO Sighting value
//     var cell = row.append("td");

//     cell.text(value);
// 	})

// })
})

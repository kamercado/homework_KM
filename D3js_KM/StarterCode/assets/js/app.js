// @TODO: YOUR CODE HERE!

//steps pulled from class activity:
function makeResponsive() {
	// Step 1: Set up our chart
	var svgWidth = 960;
	var svgHeight = 500;

	var margin = {
	  top: 20,
	  right: 40,
	  bottom: 60,
	  left: 50
	};

	var width = svgWidth - margin.left - margin.right;
	var height = svgHeight - margin.top - margin.bottom;

	// Step 2: Create an SVG wrapper,
	// append an SVG group that will hold our chart,
	// and shift the latter by left and top margins.

	var svg = d3.select("#scatter")
	  .append("svg")
	  .attr("width", svgWidth)
	  .attr("height", svgHeight);

	var chartGroup = svg.append("g")
	  .attr("transform", `translate(${margin.left}, ${margin.top})`);

	// Step 3:
	// Import data from the data.csv file
	d3.csv("./assets/data/data.csv").then(healthpovData => {
	    // Step 4: Parse the data
	  // Format the data and convert to numerical values
	  healthpovData.forEach(data => {
	  	data.healthcare = +data.healthcare;
	   	data.poverty = +data.poverty;
	   });

	      // Step 5: Create scales
	  var xLinearScale = d3.scaleLinear()
	  	.domain([0, d3.max(healthpovData, d => d.poverty)])
	  	.range([0, width]);
	  var yLinearScale = d3.scaleLinear()
	  	.domain([0, d3.max(healthpovData, d => d.healthcare)])
	  	.range([height, 0]);


	  // Step 6: Create axes
	  var bottomAxis = d3.axisBottom(xLinearScale);
	  var leftAxis = d3.axisLeft(yLinearScale);

	  // Step 7: Append the axes to the chartGroup
	  // Add x-axis
	  chartGroup.append("g")
	    .attr("transform", `translate(0, ${height})`)
	    .call(bottomAxis);

	  // Add y-axis
	  chartGroup.append("g")
	  	.call(leftAxis);

	  // Step 8: Set up dots generators

	  // Circles for data
	  var circlesGroup = chartGroup.selectAll("circle")
	    .data(healthpovData)
	    .enter()
	    .append("circle")
	    .attr("cx", (d,i) => {
	    	return xLinearScale(d.poverty)})
	    .attr("cy", data => {
	    	return yLinearScale(data.healthcare)})
	    .attr("r", "10")
	    .attr("fill", "lightblue");

	});

}

makeResponsive();

d3.select(window).on("resize", makeResponsive);

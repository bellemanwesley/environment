function update(){
	document.getElementById("one").innerHTML = "New Text!";
}

function uk_update(){
	//postData('https://search-dcos-tutorial-2kfa5db5yllkqpnfaysztenoku.us-east-2.es.amazonaws.com/movies/_search?q=mars')
	//document.getElementById("one").innerHTML = postData("https://search-dcos-tutorial-2kfa5db5yllkqpnfaysztenoku.us-east-2.es.amazonaws.com/movies/_search?q=mars")
	document.getElementById("one").innerHTML = postData("http://x.com/")
}

function postData(url) {
	var xhttp = new XMLHttpRequest();
	xhttp.open("POST", "http://localhost");
	xhttp.send(url);
	my_response = xhttp.responseText;
	console.log(my_response);
	return my_response;
}



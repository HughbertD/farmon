## Hello World

<div id="text"></div>
 
<script>
const http = new XMLHttpRequest();
http.open("GET", 'https://flooding-data.s3.eu-west-2.amazonaws.com/plot.html');
http.send();
http.onreadystatechange = function (e) {
console.log(e);
   if (this.readyState === 4 && this.status === 200) {
	console.log(http);
   	document.getElementById("text").innerHTML = http.responseText;	
   }
}
</script>

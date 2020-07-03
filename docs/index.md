## Hello World

<div id="text"></div>
 
<script>
const http = new XMLHttpRequest();
http.open("GET", 'https://flooding-data.s3.eu-west-2.amazonaws.com/plot.html');
http.send();
http.onreadystatechange = (e) => {
   if (this.readyState === 4 && this.status === 200) {
	console.log(Http);
   	document.getElementById("text").innerHTML = Http.responseText;	
   }
}
</script>

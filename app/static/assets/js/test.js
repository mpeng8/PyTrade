function stock(data){
  this.open = data[2];
  this.close = data[5];
  this.date = new Date(data[1]);
  this.high = data[3];
  this.low =data[4];
}


var stockIDs = document.getElementById("stockID_info").innerText;
//console.log(stockID);

var todayDate = new Date();
//console.log(todayDate);
var oldDate = new Date();
oldDate.setDate(todayDate.getDate() - 30);
//console.log(oldDate);

var dateLT = todayDate.toJSON().slice(0,10).replace(/-/g,'');
var dateGTE = oldDate.toJSON().slice(0,10).replace(/-/g,'');
console.log(dateGTE);
console.log(dateLT);
var url = "https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?date.gte="+dateGTE+"&date.lt=" + dateLT+"&ticker=" + stockIDs+"&api_key=sXBsPYtsefUf_qaFxNDK";


function createCORSRequest(method, url) {
  var xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {

    // Check if the XMLHttpRequest object has a "withCredentials" property.
    // "withCredentials" only exists on XMLHTTPRequest2 objects.
    xhr.open(method, url, true);

  } else if (typeof XDomainRequest != "undefined") {

    // Otherwise, check if XDomainRequest.
    // XDomainRequest only exists in IE, and is IE's way of making CORS requests.
    xhr = new XDomainRequest();
    xhr.open(method, url);

  } else {

    // Otherwise, CORS is not supported by the browser.
    xhr = null;

  }
  return xhr;
}

var xhr = createCORSRequest('GET', url);
console.log("d");
if (!xhr) {
  throw new Error('CORS not supported');
}
xhr.onload = function() {
 var responseText = xhr.responseText;
 console.log(responseText);
 // process the response.
};
xhr.onerror = function() {
    alert('Woops, there was an error making the request.');
  };

  xhr.send();
console.log("dd");

'use strict';

var ENDPOINT = 'http://localhost:3000/reps'
// var ENDPOINT = 'https://phone-your-rep-api.herokuapp.com/reps'


/**
 * Embeds a json object into the url
 * for use in an HTTP request
 * @param  {string} base | the domain and endpoint
 * @param  {json} data | the params to incorporate (only one level deep please)
 * @return {string}
 */
function createURLString(base, data) {
  for (var key in data) {
    var value = encodeURIComponent(data[key])
    base += `?${key}=${value}`
  }

  return base
}

/**
 * Sends an HTTP request
 * @param  {[type]} data    [description]
 * @param  {[type]} onLoad  [description]
 * @param  {[type]} onError [description]
 * @return {[type]}         [description]
 */
function sendHTTP(baseURL, data, onLoad, onError) {
  var request = new XMLHttpRequest();
  var url = createURLString(baseURL, data);

  request.open("GET", url);
  request.addEventListener("load", onLoad);
  request.addEventListener("error", onError);
  request.send();
}

/**
 * Returns the main input's value
 * @return address
 */
function getInputValue() {
  return document.getElementById('pyr-input').value
}

function success() {
  console.log("success");
  var response = JSON.parse(this.responseText);

  if (this.status >= 200 && this.status < 400 && response) {
    document.getElementById('pyr-query').innerText = response.zipcode;
    document.getElementById('pyr-name').innerText = response.member_full;
    document.getElementById('pyr-phone').innerText = response.dc_tel;
    document.getElementById('pyr-phone-link').href = "tel:" + response.dc_tel;
    document.getElementById('pyr-result').style = "display: block;";
    document.getElementById('pyr-no-result').style = "display: none;";


  } else {
    // We reached our target server, but it returned an error
    document.getElementById('pyr-error').style = "display: none;";
    document.getElementById('pyr-not-found').style = "display: block;";
    document.getElementById('pyr-no-result').style = "display: block;";

    console.log("Did not find it.");
  }

}

function failure() {
  console.log("Failure :(");
  document.getElementById('pyr-error').style = "display: block;";
  document.getElementById('pyr-not-found').style = "display: none;";
  document.getElementById('pyr-no-result').style = "display: block;";

}

function clicked() {
  console.log("clicked");
  var zipinput = getInputValue();
  var data = { zip: zipinput };
  sendHTTP(ENDPOINT, data, success, failure);
}

(function() {

})();

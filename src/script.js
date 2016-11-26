'use strict';

var ENDPOINT = ''


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
  request.addEventListener("load", onLoad);
  request.addEventListener("error", onError);

  var url = createURLString(baseURL, data)
  request.open("GET", url);
}

/**
 * Returns the main input's value
 * @return address
 */
function getInputValue() {
  return document.getElementById('pyr-input').value
}

function clicked() {

}

(function() {

})();

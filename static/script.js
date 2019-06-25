function upload() {
  var output;
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/upvote');
  xhr.send();

  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      output = xhr.responseText;
      document.getElementById('output').innerHTML = output;
      console.log(output);
    }
  }
}

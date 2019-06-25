function upvote(id) {
  console.log('id is this', id);
  fetch('/upvote', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({'id': id})
  }).then(function(response) {
    console.log('response', response);
  }).catch(function(err) {
    // Error :(
    console.log('err', err);
  });
}

function downvote(id) {
}

function upvote(id) {
  console.log('id', id);
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
    console.log('error', err);
  });
}

function downvote(id) {
  fetch('/downvote', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({'id': id})
  }).then(function(response) {
    console.log('response', response);
  }).catch(function(err) {
    console.log('error', err);
  });
}

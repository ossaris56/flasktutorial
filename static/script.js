function upvote(id) {
  points = document.getElementById('p'+id);
  fetch('/upvote', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({'id': id})
  }).then(res => res.json())
  .then(function(response) {
    points.innerText = response['id']
  }).catch(function(err) {
    console.log('error', err);
  })
}

function downvote(id) {
  points = document.getElementById('p'+id);
  fetch('/downvote', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({'id': id})
  }).then(res => res.json())
  .then(function(response) {
    points.innerText = response['id'];
  }) .catch(function(err) {
    console.log('error', err);
  });
}
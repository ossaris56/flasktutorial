function upvote(id) {
  if (document.getElementById('p'+id).classList.contains('upvoted')) {
    return
  }
  fetch('/upvote', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({'id': id})
  }).then(function(response) {
    // return a promise
    return response.json()
  }).then(function(response) {
    console.log(JSON.stringify(response));
    document.getElementById('p'+id).innerText = response['id'];
    document.getElementById('p'+id).classList.add('upvoted');
    if (document.getElementById('p'+id).classList.contains('downvoted')) {
      document.getElementById('p'+id).classList.remove('downvoted')
    }
  }).catch(function(err) {
    console.log('error', err);
  })
  upvoted = true;
}

function downvote(id) {
  if (document.getElementById('p'+id).classList.contains('downvoted')) {
    return
  }
  fetch('/downvote', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({'id': id})
  }).then(function(response) {
    return response.json()
  }).then(function(response) {
    console.log(JSON.stringify(response));
    document.getElementById('p'+id).innerText = response['id'];
    document.getElementById('p'+id).classList.add('downvoted');
    if (document.getElementById('p'+id).classList.contains('upvoted')) {
      document.getElementById('p'+id).classList.remove('upvoted')
    }
  }) .catch(function(err) {
    console.log('error', err);
  });
  downvoted = true;
}
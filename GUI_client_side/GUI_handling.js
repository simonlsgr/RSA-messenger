

var readJson = (path, cb) => {
    fs.readFile(require.resolve(path), (err, data) => {
      if (err)
        cb(err)
      else
        cb(null, JSON.parse(data))
    })
}

var fetched_messages = []
readJson('./messages.json', (err, data) => {
    if (err) {  // handle error 
    } else {
        fetched_messages = data
    }
});

console.log(fetched_messages)
function contactClicked() {
    document.querySelectorAll('.contact').forEach(button => {
      button.classList.remove('selected-contact');
    });
    
    this.classList.add('selected-contact');
}
  
document.querySelectorAll('.contact').forEach(button => {
    button.onclick = contactClicked;
});



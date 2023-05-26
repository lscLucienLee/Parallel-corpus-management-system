function getfile(){
  var fileInput = document.getElementById('file');
  var fileName = fileInput.files[0].name;
  var fileLabel = document.getElementById('filename');
  fileLabel.innerHTML = fileName;
}
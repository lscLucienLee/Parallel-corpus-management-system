function getfile(){
  let fileInput = document.getElementById('file');
  let fileName = fileInput.files[0].name;
  let fileLabel = document.getElementById('filename');
  fileLabel.innerHTML = fileName;
}
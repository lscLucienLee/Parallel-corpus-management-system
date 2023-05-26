function frequency(){
var word = $('input[name="word"]').val();
if (word=="") {
alert("请输入查询内容！");
return;
}
$("#word").text(word);
}
function hover(){
    const button = document.querySelector('.btn.btn-default');
    const panel = document.querySelector('.panel.panel-default');

    button.addEventListener('mouseover', () => {
      panel.style.visibility = 'visible';
    });

    button.addEventListener('mouseout', () => {
      panel.style.visibility = 'hidden';
    });
}
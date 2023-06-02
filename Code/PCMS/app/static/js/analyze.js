//查询输入单词的词频
function frequency(){
    var wordVal = $('input[name="word"]').val();
    if (wordVal=="") {
        alert("请输入查询内容！");
        return;
    }else{
        $("#word").text(word);
        var requestBody={
            word:'word'
        };
        requestBody.word=wordVal;
        var jqxhr = $.post('/path/to/resource',requestBody);
        jqxhr.done(function(data) {
            $("#frequencyId").test(data.frequency);
        });
    }
}

//鼠标放上去会解释查询
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

//查找一共有多少条平行语料
var corpusNumber = $.getJSON('/path/to/resource', {
    corpus_name: 'Bob Lee',
}).done(function (data) {
    $("#corpusNumberId")=data.corpus_number;
    // data已经被解析为JSON对象了
});


    var json = [{
        "id": "1001",
        "": "java核心技术1",
        "price": "120",
        "imgurl": "res/productimg/1.jpeg"
    }, {
        "product_id": "1002",
        "product_name": "java核心技术2",
        "price": "130",
        "imgurl": "res/productimg/2.jpeg"
    }, {
        "product_id": "1003",
        "product_name": "web技术",
        "price": "100",
        "imgurl": "res/productimg/3.jpeg"
    }, {
        "product_id": "1004",
        "product_name": "Mysql必知必会",
        "price": "39",
        "imgurl": "res/productimg/4.jpeg"
    }, {
        "product_id": "1005",
        "product_name": "中国近代史",
        "price": "105",
        "imgurl": "res/productimg/4.jpeg"
    }];

var json = $.getJSON('/path/to/resource', {
    corpus_name: 'Bob Lee',
}).done(function (data) {

    // data已经被解析为JSON对象了
});


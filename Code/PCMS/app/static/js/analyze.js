//初始页面加载：获得词频前五的数据
/*
方法：get
res:
[
{"corpus_number":"100"}
{"id":"1","original":"词","translation":"word","frequencyId":"12"}//
...
]
*/
$(document).ready(function () {
    let tbody = document.querySelector("tbody");
    $.ajax({
        url: '/path/to/resource',
        type: 'GET',
        dataType: 'text',
        success: function (data) {
            console.log(data);
            // 处理响应数据

            let json = JSON.parse(data);
            json.forEach(function (item, i) {
                if (i === 0) {
                    $("#corpusNumberId").text(item.corpus_number);
                } else {
                    if (i < 6) {
                        let tr = document.createElement("tr");
                        tr.innerHTML = `
                            <td>${item.id}</td>
                            <td>${item.original}</td>
                            <td>${item.translation}</td>
                            <td>${item.frequencyId}</td>
                            `
                        tbody.appendChild(tr);
                    }
                }
            })
        },
        error: function (xhr, textStatus, errorThrown) {
            console.log("Error: " + errorThrown);
            // 处理错误
        }
    });
});


//查询输入单词的词频
/*
* 方法：post
* req:
* {word:"word"}
*
* res:
* {
*   "word":"word",
*   "frequencyId":"13"
* }
*
*/
function frequency() {
    let wordVal = $('input[name="word"]').val();
    if (wordVal === " ") {
        alert("请输入查询内容！");
    } else {
        $("#word").text(wordVal);
        let requestBody = {
            word: 'word'
        };
        requestBody.word = wordVal;
        $.ajax({
            url: '/path/to/resource',
            type: 'POST',
            data: requestBody,
            dataType: 'json',
            success: function (data) {
                console.log(data);
                console.log(data.frequencyId);
                $("#frequencyId").text(data.frequencyId);
                // 处理响应数据
            },
            error: function (xhr, textStatus, errorThrown) {
                console.log("Error: " + errorThrown);
                // 处理错误
            }
        });

    }
}

//鼠标放上去会解释查询
function hover() {
    const button = document.querySelector('.btn.btn-default');
    const panel = document.querySelector('.panel.panel-default');

    button.addEventListener('mouseover', () => {
        panel.style.visibility = 'visible';
    });

    button.addEventListener('mouseout', () => {
        panel.style.visibility = 'hidden';
    });
}







function openwindow(){
		var r = confirm("确认删除嘛？")
		if (r == true) {
		window.location.href=""
		} else {

		}
	}


function search(){
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
            url: '/browse/search/',
            type: 'POST',
            data: requestBody,
            dataType: 'json',
            success: function (data)
            {
                window.location.href = "/browse/?corpus_name=" + data.name + "&key=" + data.key;
            },
            error: function (xhr, textStatus, errorThrown) {
                console.log("Error: " + errorThrown);
                // 处理错误
            }
        });

    }
``}
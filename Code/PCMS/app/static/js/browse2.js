function openwindow(){
		var r = confirm("确认删除吗？")
		if (r == true) {
		window.location.href="#"
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
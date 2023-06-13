function ok(){

　　　　//获取所有单选按钮（同一组），得到对象
　　　　var n1 = document.getElementByName("n1");

　　　　for(var i=0;i<n1.length;i++){

　　　　　　if(n1[i].checked){

　　　　　　　　alert("选择了"+n1[i].value);

　　　　　　}

　　　　}

　　}
     function Post(){

           var corpus_name1=$('input:radio:checked').val()

           $.ajax({
            url: "/index/", //后端地址
            type: "post",       //提交方式
            data: {  "corpus_name":corpus_name1
            },
            dataType: "JSON",       //规定请求成功后返回的数据
            success: function (data) {
                //请求成功之后进入该方法，data为成功后返回的数据
            },
            error: function (errorMsg) {
                //请求失败之后进入该方法，errorMsg为失败后返回的错误信息
            }
        });


     }
function openwindow(){
		var r = confirm("确认拆分吗？")
		if (r == true) {
		window.location.href="/manage/"
		} else {

		}
	}
function ShowImage(self){
       if($("#status").val()==1)
       {$("#image1").removeClass("hidden");
       $("#image2").addClass("hidden");
       $("#image3").addClass("hidden");
       }
       else if($("#status").val()==2)
       {$("#image1").removeClass("hidden");
       $("#image2").removeClass("hidden");
       $("#image3").addClass("hidden");}
       else if($("#status").val()==3)
       {
           $("#image1").removeClass("hidden");
           $("#image2").removeClass("hidden");
           $("#image3").removeClass("hidden");}
       else if($("#status").val()==0)
       {
           $("#image1").addClass("hidden");
           $("#image2").addClass("hidden");
           $("#image3").addClass("hidden");
       }


     }
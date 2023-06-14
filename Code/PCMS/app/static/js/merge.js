
    var table = document.querySelector("table")
    //模拟后台响应的数据
    $(document).ready(function () {
        $.ajax({
            url: '/manage/data/',
            type: 'GET',
            dataType: 'text',
            success: function (data) {
                console.log(data);
                // 处理响应数据
                let json = JSON.parse(data);
                var ul = document.querySelector(".pagination");
        var page_number = 5; //单页浏览的条数
        var Total_pages; //页数
        var liAll; //页码按钮下标为 1到length-2是页数 0和length-1为上一页和下一页
        var pre; //上一页
        var next; //下一页

        function clearTable() {
            table.innerHTML = `
        <tbody>
             <tr>
                <th style="width:40px">#</th>
          <th style="width:320px;text-align: center">语料库名</th>
          <th style="width:320px;text-align: center ">创建时间</th>
          <th style="width:120px;text-align: center ">是否选择合并</th>
            </tr>
        </tbody>
        `
        }

        json.forEach(function (item, i) {
            var tbody = document.querySelector("tbody");
            if (i < page_number) {
                var tr = document.createElement("tr");
                tr.innerHTML = `
                             <td>${item.id}</td>
                            <td>${item.name}</td>
                            <td>${item.time}</td>
                            <td><input id="${item.id}" name="${item.id}"  type="checkbox" style="margin-left: 40px"></td>
                            `
                tbody.appendChild(tr);
            }

        })

        var len = json.length; //总记录条数

        Total_pages = len % page_number == 0 ? len / page_number : len / page_number + 1; //页数

        for (var i = 1; i <= Total_pages; i++) {
            ul.innerHTML += `
            <li  id="${i}"><a href="#">${i}</a></li>
            `
        }

        ul.innerHTML += `
                <li id="next">
                    <a href="#" aria-label="Next">
                        <span aria-hidden="true">&raquo;</span>
                    </a>
                </li>
        `;
        liAll = document.querySelectorAll("li");

        // console.log([liAll])
        var pagethis = 1; //当前是第几页
        for (var i = 1; i < liAll.length - 1; i++) {
            liAll[i].onclick = function () {
                for (var j = 1; j < liAll.length - 1; j++) {

                }
                pagethis = this.id; //获取当前是第几页

                // console.log(liAll[i])
                let start; //当页数据的起始下标
                let end; //当页数据的结束下标
                if (pagethis != 1) {
                    start = (pagethis - 1) * page_number;
                    end = start + page_number - 1;
                    if (end > json.length - 1) { //如果当页数据结束值大于总数据条数下标的值则赋值为总数据条数最大下标值
                        end = json.length - 1;
                    }
                } else {
                    start = 0;
                    end = page_number - 1;
                }
                 json.forEach(function (item, i) {
                        if (i >= start && i <= end) {

                            item.checked = document.getElementById(item.id).checked;
                        }
                    })
                    // for (let j = 1; j < liAll.length - 1; j++) {
                    // }


                clearTable();
                var tbody = document.querySelector("tbody");
                json.forEach(function (item, i) {

                    if (i >= start && i <= end) {
                        var tr = document.createElement("tr");
                        tr.innerHTML = `
                        <td>${item.id}</td>
                            <td>${item.name}</td>
                            <td>${item.time}</td>
                            <td><input id="${item.id}" name="${item.id}"  type="checkbox" style="margin-left: 40px"></td>
                            `
                        tbody.appendChild(tr);
                    }
                })

            }
        }
        pre = document.querySelector("#pre") //上一页
        next = document.querySelector("#next") //下一页
        pre.onclick = function () {

            if (pagethis != 1) { //当前页数不等于1时执行上一页
                pagethis--;
                for (var j = 1; j < liAll.length - 1; j++) {

                }

                let start;
                let end;
                if (pagethis != 1) {
                    start = (pagethis - 1) * page_number;
                    end = start + page_number - 1;
                    if (end > json.length - 1) {
                        end = json.length - 1;
                    }
                } else {
                    start = 0;
                    end = page_number - 1;
                }
                  json.forEach(function (item, i) {
                        if (i >= start && i <= end) {

                            item.checked = document.getElementById(item.nid).checked;
                        }
                    })

                clearTable();
                var tbody = document.querySelector("tbody");
                json.forEach(function (item, i) {
                    if (i >= start && i <= end) {
                        var tr = document.createElement("tr");
                        tr.innerHTML = `
                             <td>${item.id}</td>
                            <td>${item.name}</td>
                            <td>${item.time}</td>
                            <td><input id="${item.id}" name="${item.id}"  type="checkbox" style="margin-left: 40px"></td>
                            `
                        console.log(tr)
                        tbody.appendChild(tr);
                    }
                })
            }
        }

        next.onclick = function () {
            // alert(pagethis)
            if (pagethis < liAll.length - 2) { //当前页数小于最后一页则执行下一页
                pagethis++;
                for (var j = 1; j < liAll.length - 1; j++) {

                }

                let start;
                let end;
                if (pagethis != 1) {
                    start = (pagethis - 1) * page_number;
                    end = start + page_number - 1;
                    if (end > json.length - 1) {
                        end = json.length - 1;
                    }
                } else {
                    start = 0;
                    end = page_number - 1;
                }
                json.forEach(function (item, i) {
                        if (i >= start && i <= end) {
                            let index = document.getElementById(item.id).selectedIndex;
                            item.value = document.getElementById(item.id).options[index].value;
                        }
                    })

                clearTable();
                var tbody = document.querySelector("tbody");
                json.forEach(function (item, i) {
                    if (i >= start && i <= end) {
                        var tr = document.createElement("tr");
                        tr.innerHTML = `
                             <td>${item.id}</td>
                            <td>${item.name}</td>
                            <td>${item.time}</td>
                            <td><input id="${item.id}" name="${item.id}"  type="checkbox" style="margin-left: 40px"></td>
                            `
                        console.log(tr)
                        tbody.appendChild(tr);
                    }
                })
            }
        }
            }
        })


    })








var table = document.querySelector("table")
    //模拟后台响应的数据
    var json = [{
        "product_id": "1001",
        "product_name": "java核心技术1",
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
    }, {
        "product_id": "1006",
        "product_name": "世界史",
        "price": "110",
        "imgurl": "res/productimg/1.jpeg"
    }, {
        "product_id": "1007",
        "product_name": "高等数学",
        "price": "50",
        "imgurl": "res/productimg/1.jpeg"
    }, {
        "product_id": "1008",
        "product_name": "离散数学",
        "price": "60",
        "imgurl": "res/productimg/1.jpeg"
    }, {
        "product_id": "1010",
        "product_name": "线性代数",
        "price": "50",
        "imgurl": "res\\productimg/3e83c2a6-b529-4bee-8ca9-ecc868b4d6f7.jpeg"
    }, {
        "product_id": "1011",
        "product_name": "数据结构",
        "price": "100",
        "imgurl": "res\\productimg/53dccb9f-b918-4a81-acc9-f99594992db1.jpeg"
    }, {
        "product_id": "1013",
        "product_name": "人工智能",
        "price": "120",
        "imgurl": "res\\productimg/94736781-046b-4c7c-8499-bebad2542b6f.jpg"
    }, {
        "product_id": "1014",
        "product_name": "大数据",
        "price": "120",
        "imgurl": "res\\productimg/f891569d-45e3-4b7f-a37e-980273f84508.jpg"
    }];

    var ul = document.querySelector(".pagination");
    var page_number = 5; //单页浏览的条数
    var Total_pages; //页数
    var liAll; //页码按钮下标为 1到length-2是页数 0和length-1为上一页和下一页
    var pre; //上一页
    var next; //下一页

    function clearTable() {
        table.innerHTML = `
            <tbody>
                <th>序号</th>
                <th>原文</th>
                <th>语料库参考译文</th>
                <th>机器翻译译文</th>
                <th id="hoverId">打分</th>
            </tbody>
        `
    }
    window.onload = function() {
        json.forEach(function(item, i) {
            var tbody = document.querySelector("tbody");
            if (i < page_number) {
                var tr = document.createElement("tr");
                tr.innerHTML = `
                            <td>${item.product_id}</td>
                            <td>${item.product_name}</td>
                            <td>${item.price}</td>
                            <td>${item.imgurl}</td>
                            <td>
                                <select name="${item.product_id}">
                                    <option value="0">打分</option>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                </select>
                            </td>
                            `
                tbody.appendChild(tr);
            }


        })
        var tbody = document.querySelector("tbody");
                var tr = document.createElement("tr");
                tr.innerHTML = `
                <td colspan="5">
                    <button type="button" class="btn btn-default dropdown-toggle"
                            style="background-color:#DCDCDC;">提交分数
                    </button>
                </td>
                `
                tbody.appendChild(tr);

        var len = json.length; //总记录条数

        Total_pages = len % page_number == 0 ? len / page_number : len / page_number + 1; //页数

        for (var i = 1; i <= Total_pages; i++) {
            ul.innerHTML += `
            <li class="page_li" id="${i}"><a href="#">${i}</a></li>
            `
        }

        ul.innerHTML += `
                <li id="next" class="page_li">
                    <a href="#" aria-label="Next">
                        <span aria-hidden="true">&raquo;</span>
                    </a>
                </li>
        `;
        liAll = document.querySelectorAll("li.page_li");
        var pagethis = 1; //当前是第几页
        for (var i = 1; i < liAll.length - 1; i++) {
            liAll[i].onclick = function() {
                for (var j = 1; j < liAll.length - 1; j++) {
                }
                pagethis = this.id; //获取当前是第几页
                console.log(pagethis);
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
                console.log("start=" + start)
                console.log("end=" + end)
                clearTable();
                var tbody = document.querySelector("tbody");
                json.forEach(function(item, i) {

                    if (i >= start && i <= end) {
                        var tr = document.createElement("tr");
                        tr.innerHTML = `
                            <td>${item.product_id}</td>
                            <td>${item.product_name}</td>
                            <td>${item.price}</td>
                            <td>${item.imgurl}</td>
                            <td>
                                <select name="${item.product_id}">
                                    <option value="0">打分</option>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                </select>
                            </td>
                            `
                        tbody.appendChild(tr);
                    }
                })
                var tr = document.createElement("tr");
                tr.innerHTML = `
                <td colspan="5">
                    <button type="button" class="btn btn-default dropdown-toggle"
                            style="background-color:#DCDCDC;">提交分数
                    </button>
                </td>
                `
                tbody.appendChild(tr);

            }
        }
        pre = document.querySelector("#pre")
        next = document.querySelector("#next") //下一页
        pre.onclick = function() {
            //alert(pagethis)
            if (pagethis != 1) { //当前页数不等于1时执行上一页
                pagethis--;

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

                clearTable();
                var tbody = document.querySelector("tbody");
                json.forEach(function(item, i) {
                    if (i >= start && i <= end) {
                        var tr = document.createElement("tr");
                        tr.innerHTML = `
                            <td>${item.product_id}</td>
                            <td>${item.product_name}</td>
                            <td>${item.price}</td>
                            <td>${item.imgurl}</td>
                            <td>
                                <select name="${item.product_id}">
                                    <option value="0">打分</option>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                </select>
                            </td>
                            `
                        tbody.appendChild(tr);
                    }

                })
                var tr = document.createElement("tr");
                tr.innerHTML = `
                <td colspan="5">
                    <button type="button" class="btn btn-default dropdown-toggle"
                            style="background-color:#DCDCDC;">提交分数
                    </button>
                </td>
                `
                tbody.appendChild(tr);

            }
            else
            {
             alert("当前为第一页")
            }
        }
        next.onclick = function() {
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

                clearTable();
                var tbody = document.querySelector("tbody");
                json.forEach(function(item, i) {
                    if (i >= start && i <= end) {
                        var tr = document.createElement("tr");
                        tr.innerHTML = `
                            <td>${item.product_id}</td>
                            <td>${item.product_name}</td>
                            <td>${item.price}</td>
                            <td>${item.imgurl}</td>
                            <td>
                                <select name="${item.product_id}">
                                    <option value="0">打分</option>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                </select>
                            </td>
                            `
                        tbody.appendChild(tr);
                    }
                })
                var tr = document.createElement("tr");
                tr.innerHTML = `
                <td colspan="5">
                    <button type="button" class="btn btn-default dropdown-toggle"
                            style="background-color:#DCDCDC;">提交分数
                    </button>
                </td>
                `
                tbody.appendChild(tr);
            }
            else
            {
            alert("当前为最后一页")
            }
        }

    }

let table = document.querySelector("table")
    //模拟后台响应的数据
    let json = [{
        "id": "1001",
        "original": "java核心技术1",
        "standard_translation": "120",
        "machine_translation": "res/productimg/1.jpeg"
    }, {
        "id": "1002",
        "original": "java核心技术2",
        "standard_translation": "130",
        "machine_translation": "res/productimg/2.jpeg"
    }, {
        "id": "1002",
        "original": "java核心技术2",
        "standard_translation": "130",
        "machine_translation": "res/productimg/2.jpeg"
    }, {
        "id": "1002",
        "original": "java核心技术2",
        "standard_translation": "130",
        "machine_translation": "res/productimg/2.jpeg"
    }, {
        "id": "1002",
        "original": "java核心技术2",
        "standard_translation": "130",
        "machine_translation": "res/productimg/2.jpeg"
    }, {
        "id": "1002",
        "original": "java核心技术2",
        "standard_translation": "130",
        "machine_translation": "res/productimg/2.jpeg"
    }];

    let ul = document.querySelector(".pagination");
    let page_number = 5; //单页浏览的条数
    let Total_pages; //页数
    let liAll; //页码按钮下标为 1到length-2是页数 0和length-1为上一页和下一页
    let pre; //上一页
    let next; //下一页

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
            let tbody = document.querySelector("tbody");
            if (i < page_number) {
                let tr = document.createElement("tr");
                tr.innerHTML = `
                            <td>${item.id}</td>
                            <td>${item.original}</td>
                            <td>${item.standard_translation}</td>
                            <td>${item.machine_translation}</td>
                            <td>
                                <select name="${item.id}">
                                    <option value="0">0</option>
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

        Total_pages = len % page_number === 0 ? len / page_number : len / page_number + 1; //页数

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
            if (pagethis !== 1) { //当前页数不等于1时执行上一页
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

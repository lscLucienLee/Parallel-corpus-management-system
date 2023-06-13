
    var table = document.querySelector("table")
    $(document).ready(function () {
    let tbody = document.querySelector("tbody");
    $.ajax({
        url: '/browse/data/',
        type: 'GET',
        dataType: 'text',
        success: function (data) {
            console.log(data);


            let json = JSON.parse(data);


    var ul = document.querySelector(".pagination");
    var page_number = 10;
    var Total_pages;
    var liAll;
    var pre;
    var next;

    function clearTable() {
        table.innerHTML = `
        <tbody>
             <tr>
                 <th style="width: 50px">#</th>
                    <th style="width:400px">??</th>
          <th style="width: 400px">??</th>
          <th style="width: 140px">??</th>
            </tr>
        </tbody>
        `
    }
    window.onload = function() {
        json.forEach(function(item, i) {
            var tbody = document.querySelector("tbody");
            if (i < page_number) {
                var tr = document.createElement("tr");
                tr.innerHTML = `
                            <td style="width: 50px">${item.id}</td>
                            <td style="width: 400px">${item.original}</td>
                            <td style="width: 400px">${item.translation}</td>
                            <td style="width:140px">
              <a href="/update/"><button type="button" class="btn btn-default btn-sm" style="width:50px;height:25px;background-color:#DCDCDC">??</button></a>
              <button type="button" class="btn btn-default btn-sm" style="width:50px;height:25px;background-color:#DCDCDC" onclick="openwindow()">??</button>
          </td>
                            `
                tbody.appendChild(tr);
            }

        })

        var len = json.length; //?????

        Total_pages = len % page_number == 0 ? len / page_number : len / page_number + 1; //??

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
        var pagethis = 1; //??????
        for (var i = 1; i < liAll.length - 1; i++) {
            liAll[i].onclick = function() {
                for (var j = 1; j < liAll.length - 1; j++) {

                }
                pagethis = this.id; //????????

                // console.log(liAll[i])
                let start; //?????????
                let end; //?????????
                if (pagethis != 1) {
                    start = (pagethis - 1) * page_number;
                    end = start + page_number;
                    if (end > json.length - 1) { //??????????????????????????????????
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
                            <td style="width: 50px">${item.id}</td>
                            <td style="width: 400px">${item.original}</td>
                            <td style="width: 400px">${item.translation}</td>
                            <td style="width:140px">
              <a href="/update/"><button type="button" class="btn btn-default btn-sm" style="width:50px;height:25px;background-color:#DCDCDC">??</button></a>
              <button type="button" class="btn btn-default btn-sm" style="width:50px;height:25px;background-color:#DCDCDC" onclick="openwindow()">??</button>
          </td>
                            `
                        tbody.appendChild(tr);
                    }
                })

            }
        }
        pre = document.querySelector("#pre") //???
        next = document.querySelector("#next") //???
        pre.onclick = function() {

            if (pagethis != 1) { //???????1??????
                pagethis--;
                for (var j = 1; j < liAll.length - 1; j++) {

                }

                let start;
                let end;
                if (pagethis != 1) {
                    start = (pagethis - 1) * page_number;
                    end = start + page_number;
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
                             <td style="width: 50px">${item.id}</td>
                            <td style="width: 400px">${item.original}</td>
                            <td style="width: 400px">${item.translation}</td>
                            <td style="width:140px">
              <a href="/update/"><button type="button" class="btn btn-default btn-sm" style="width:50px;height:25px;background-color:#DCDCDC">??</button></a>
              <button type="button" class="btn btn-default btn-sm" style="width:50px;height:25px;background-color:#DCDCDC" onclick="openwindow()">??</button>
          </td>
                            `
                        console.log(tr)
                        tbody.appendChild(tr);
                    }
                })
            }
        }
        next.onclick = function() {
            // alert(pagethis)
            if (pagethis < liAll.length - 2) { //????????????????
                pagethis++;
                for (var j = 1; j < liAll.length - 1; j++) {

                }

                let start;
                let end;
                if (pagethis != 1) {
                    start = (pagethis - 1) * page_number;
                    end = start + page_number;
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
                             <td style="width: 50px">${item.id}</td>
                            <td style="width: 400px">${item.original}</td>
                            <td style="width: 400px">${item.translation}</td>
                            <td style="width:140px">
             <a href="/update/"><button type="button" class="btn btn-default btn-sm" style="width:50px;height:25px;background-color:#DCDCDC">??</button></a>
              <button type="button" class="btn btn-default btn-sm" style="width:50px;height:25px;background-color:#DCDCDC" onclick="openwindow()">??</button>
          </td>
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


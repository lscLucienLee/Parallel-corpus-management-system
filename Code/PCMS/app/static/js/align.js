/*
方法：get
res:
success:
{
    "word_num":"4",
    "origin": ["那本","书","在","哪"],
    "translation": ["the","book", "is", "there"]
}
error:
{
    "error":"已达最后一条",
}
*/
let json;
window.onload = function () {
    $.ajax({
        url: '/align/',
        type: 'GET',
        dataType: 'text',
        success: function (data) {
            console.log(data);
            // 处理响应数据
            json = JSON.parse(data);
            let tbody = document.querySelector("tbody");
            let tr1 = document.createElement("tr");
            let td1 = document.createElement("td");
            json.original.forEach(function (data, i) {
                td1.innerHTML += `<span class="borderText">${i + 1} ${data}</span>  `
            })
            tr1.appendChild(td1);
            tbody.appendChild(tr1);
            let tr2 = document.createElement("tr");
            let td2 = document.createElement("td");


            json.translation.forEach(function (data, i) {
                let select = document.createElement("select");
                let span = document.createElement("span");
                span.classList.add("borderText");
                const optionElement1 = document.createElement("option");

                optionElement1.value = $(i + 1)[0];
                optionElement1.text = $(i + 1)[0];
                select.add(optionElement1);
                optionElement1.selected = true;
                for (let j = 1; j <= json.word_num; j++) {
                    const optionElement2 = document.createElement("option");
                    optionElement2.value = $(j)[0];
                    optionElement2.text = $(j)[0];
                    select.add(optionElement2);
                }
                select.name = data;
                select.setAttribute("id", (i + 1).toString());
                span.appendChild(select);
                console.log(select.id)
                span.innerHTML += data;
                td2.appendChild(span)
                tr2.appendChild(td2);
                tbody.appendChild(tr2);
            })

        },
        error: function (xhr, textStatus, errorThrown) {
            console.log("Error: " + errorThrown);
            // 处理错误
        }
    })

}

function next() {
    let select_list = document.querySelectorAll('tr td span select');
    const set = new Set();
    select_list.forEach(function (select) {
        let index = select.selectedIndex;
        let value = select.options[index].value;
        set.add(value);
    })
    if (set.size < json.word_num) {
        alert("选择重复！");
    } else {
        select_list.forEach(function (select) {
            let index = select.selectedIndex;
            let value = select.options[index].value;
            json.translation[value - 1] = select.name;
        })
        console.log(JSON.stringify(json));
        $.ajax({
            url: '/path',
            type: 'post',
            data: JSON.stringify(json),
            dataType: 'text',
            success: function (data) {
                console.log(data);
                if ("error" in data) {
                    alert(data.error);
                } else {
                    console.log(data);
                    // 处理响应数据
                    json = JSON.parse(data);
                    let tbody = document.querySelector("tbody");
                    tbody.innerHTML=``;
                    let tr1 = document.createElement("tr");
                    let td1 = document.createElement("td");
                    json.original.forEach(function (data, i) {
                        td1.innerHTML += `<span class="borderText">${i + 1} ${data}</span>  `
                    })
                    tr1.appendChild(td1);
                    tbody.appendChild(tr1);
                    let tr2 = document.createElement("tr");
                    let td2 = document.createElement("td");


                    json.translation.forEach(function (data, i) {
                        let select = document.createElement("select");
                        let span = document.createElement("span");
                        span.classList.add("borderText");
                        const optionElement1 = document.createElement("option");

                        optionElement1.value = $(i + 1)[0];
                        optionElement1.text = $(i + 1)[0];
                        select.add(optionElement1);
                        optionElement1.selected = true;
                        for (let j = 1; j <= json.word_num; j++) {
                            const optionElement2 = document.createElement("option");
                            optionElement2.value = $(j)[0];
                            optionElement2.text = $(j)[0];
                            select.add(optionElement2);
                        }
                        select.name = data;
                        select.setAttribute("id", (i + 1).toString());
                        span.appendChild(select);
                        console.log(select.id)
                        span.innerHTML += data;
                        td2.appendChild(span)
                        tr2.appendChild(td2);
                        tbody.appendChild(tr2);
                    })
                }
            },
            error: function (xhr, textStatus, errorThrown) {
                console.log("Error: " + errorThrown);
                // 处理错误
            }
        })
    }
}

function downloadFile(filename) {
    $.ajax({
        url: "/path/to/" + filename,
        type: "GET",
        dataType: "blob",
        responseType: "blob",
        success: function (res, status, xhr) {
            const blob = new Blob([res], {type: "application/octet-stream"});
            const url = window.URL.createObjectURL(blob);
            const link = document.createElement("a");
            link.href = url;
            link.download = filename;
            link.click();
            window.URL.revokeObjectURL(url);
        },
        error: function (xhr, status, error) {
            console.error("Error while downloading file '" + filename + "': " + error);
        }
    });
}
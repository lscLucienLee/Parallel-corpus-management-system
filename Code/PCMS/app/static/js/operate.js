function filter(){
var jqxhr = $.getJSON('/path/to/resource', {
    corpus_name: 'Bob Lee',
}).done(function (data) {
    alert("过滤成功");
    // data已经被解析为JSON对象了
});
}

function normalize(){
var jqxhr = $.getJSON('/path/to/resource', {
    corpus_name: 'Bob Lee',
}).done(function (data) {
    alert("规范化成功");
    // data已经被解析为JSON对象了
});
}

function remove(){
var jqxhr = $.getJSON('/path/to/resource', {
    corpus_name: 'Bob Lee',
}).done(function (data) {
    alert("去重成功");
    // data已经被解析为JSON对象了
});
}
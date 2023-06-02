function filter(){
var jqxhr = $.getJSON('/path/to/resource', {
    corpus_name: 'Bob Lee',
}).done(function (data) {
    alert(data.data;
    // data已经被解析为JSON对象了
});
}

function normalize(){
var jqxhr = $.getJSON('/path/to/resource', {
    corpus_name: 'Bob Lee',
}).done(function (data) {
    alert(data.data);
    // data已经被解析为JSON对象了
});
}

function remove(){
var jqxhr = $.getJSON('/path/to/resource', {
    corpus_name: 'Bob Lee',
}).done(function (data) {
    alert(data.data);
    // data已经被解析为JSON对象了
});
}
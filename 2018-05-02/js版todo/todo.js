/*
1. 给add绑定事件
2. 在事件处理函数中，获取input的值
3. 用获取的值组装一个todo-cell
4. 并插入todo
 */
var log = function () {
    console.log.apply(console, arguments)
};
var e = function (sel) {
    return document.querySelector(sel)
};

var todoTemplate = function(todo){
    var t1 = `
        <div class="todo-cell">
            <button class="todo-delete">删除</button>
            <span>${todo}</span>
        </div>`;
    return t1
};


var b = e("#id-button-add");

b.addEventListener('click', function () {
    log('click');
    var input = e("#id-input-todo");
    var todo = input.value;
    log("todo", todo);
    var todoCell = todoTemplate(todo);
    var todoList = e('.todo-list');
    todoList.insertAdjacentHTML("beforeend", todoCell)
});
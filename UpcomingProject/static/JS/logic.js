// 全局变量oldText 用于保存点击编辑前的Title
let oldText = ""

// 加载时候的内容逻辑
$(document).ready(function () {
    $.ajax({
        url: '/allData',
        dataType: 'json',
        type: 'GET',
        async: false,
        success: function (data) {
            $("#Content").html(displayContent(data))
        }
    })
})

// 底部计数逻辑
$(document).ready(function () {
    $.ajax({
        // 接口待更改
        url: '/allDataCount',
        dataType: 'json',
        type: 'GET',
        async: false,
        success: function (data) {
            $("#BottomContent").html(displayCount(data))
        }
    })
})

// 即时搜索的逻辑
function Search() {
    let text = document.getElementById("SearchInput").value;
    if (text === '') {
        $.ajax({
            url: '/allData',
            dataType: 'json',
            type: 'GET',
            async: false,
            success: function (data) {
                $("#Content").html(displayContent(data))
            }
        })
    } else {
        $.ajax({
            url: '/data?condition=' + text,
            dataType: 'json',
            type: 'POST',
            async: false,
            success: function (data) {
                $("#Content").html(displayContent(data))
            }
        })
    }

}

// 添加记录函数
function addRecord() {
    let text = document.getElementById("addRecord").value;
    $.ajax({
        url: '/insertData?condition=' + text,
        dataType: 'json',
        type: 'POST',
        async: false,
        success: function (data) {
            console.log(data)
            $("#addRecord").val("")
            console.log(displayContent(data))
            $("#Content").html(displayContent(data))
            $("#BottomContent").html(displayCount(data))
        }
    })
}

// 显示主题内容
function displayContent(data) {
    let html = "";
    for (let index = 0; index < data.records.length; index++) {
        let content = data.records[index];
        html += '<div style="float:left;height:27px;width:110px;"><label id="label' + (index + 1) + '">' + (index + 1) + '</label></div>';
        if (content.Undo) {
            html += '<div style="float:left;height:27px;width:300px;"><input id="input' + (index + 1) + '" type="text" readonly value="' +
                content.Title + '" style="border:None"></div>';
            html += '<div style="float:left;height: 36px;width: 230px;"><button onclick="isFinish(this.id,' + content.Undo + ')" id="Dbutton' + (index + 1) + '" style="height: 28px;width: auto">Done</button>';
        } else {
            html += '<div style="float:left;height:27px;width:300px;"><input id="input' + (index + 1) + '" type="text" readonly="readonly" value="' +
                content.Title + '" style="border:None;text-decoration:line-through"></div>';
            html += '<div style="float:left;height: 36px;width: 230px;"><button onclick="isFinish(this.id,' + content.Undo + ')" id="Dbutton' + (index + 1) + '" style="height: 28px;width: auto">Undo</button>';
        }
        html += '<button onclick="editRecord(this.id)" id="Ebutton' + (index + 1) + '" style="height: 28px;width: auto">Edit</button>';
        html += '<button onclick="RemoveRecord(this.id)" id="Rbutton' + (index + 1) + '" style="height: 28px;width: auto">Remove</button></div>';
        html += '<hr style="height:3px;width:640px ;border: none;border-top:3px solid #ddd;margin:15px 0 5px 0;"/>'
    }
    return html;
}

// 显示 左下角的计数器
function displayCount(data) {
    let html = "";
    html += ' <button disabled="disabled" style="height: 30px;padding: 0 0;width: auto;background: rgba(118,119,118,0.95);">All(' +
        data.count.total_count + ')</button>';
    html += ' <button disabled="disabled" style="height: 30px;padding: 0 0;width: auto;background: rgba(92,183,92,0.95);">Done(' +
        data.count.Done_count + ')</button>';
    html += ' <button disabled="disabled" style="height: 30px;padding: 0 0;width: auto;background: rgba(240,173,78,0.95);">Active(' +
        data.count.Undo_count + ')</button>';
    return html;
}

// 移除记录
function RemoveRecord(id) {
    let text = document.getElementById("input" + id.substring(7)).value;
    ajax_request('/removeData?condition=' + text)
}

// Undo 和Done 的转换
function isFinish(id, Undo) {
    let text = document.getElementById("input" + id.substring(7)).value;
    ajax_request('/isFinish?condition=' + text + '&Undo=' + Undo)
}

// 修改记录
function editRecord(id) {
    let inputId = "input" + id.substring(7)
    let text = document.getElementById(inputId).value;
    let isReadonly = document.getElementById(inputId).readOnly;
    if (isReadonly) {
        document.getElementById(inputId).readOnly = false;
        document.getElementById('Ebutton' + id.substring(7)).onclick = function () {
            saveRecord('Ebutton' + id.substring(7))
        }
        document.getElementById('Ebutton' + id.substring(7)).innerHTML = "Save";
    }
    oldText = text
}

// 保存修改记录
function saveRecord(id) {
    let inputId = "input" + id.substring(7)
    let text = document.getElementById(inputId).value;
    let isReadonly = document.getElementById(inputId).readOnly;
    if (!isReadonly) {
        document.getElementById(inputId).readOnly = true;
        document.getElementById('Sbutton' + id.substring(7)).onclick = function () {
            editRecord('Sbutton' + id.substring(7))
        }
        document.getElementById('Sbutton' + id.substring(7)).innerHTML = "Edit";
    }
    ajax_request('/editRecord?condition=' + oldText + '&newText=' + text)
    oldText = "" // 重新恢复成空
}

//ajax的请求
function ajax_request(url) {
    $.ajax({
        url: url,
        dataType: 'json',
        type: 'POST',
        async: false,
        success: function (data) {
            $("#Content").html(displayContent(data))
            $("#BottomContent").html(displayCount(data))
        }
    })
}
// 加载时候的内容逻辑
$(document).ready(function() {
    $.ajax({
        url: '/allData',
        dataType: 'json',
        type: 'GET',
        async: false,
        success: function(data) {
            $("#Content").html(displayContent(data))
            displayCount()
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
            success: function(data) {
                $("#Content").html(displayContent(data))
            }
        })
    } else {
        $.ajax({
            url: '/data?condition=' + text,
            dataType: 'json',
            type: 'POST',
            async: false,
            success: function(data) {
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
        success: function(data) {
            console.log(data)
            $("#addRecord").val("")
            $("#Content").html(displayContent(data))
            displayCount()
        }
    })
}

// 显示主题内容
function displayContent(data) {
    let html = "";
    for (let index = 0; index < data.records.length; index++) {
        let content = data.records[index];
        html += '<div class="numDiv"><label id="label' + (index + 1) + '">' + (index + 1) + '</label></div>';
        if (content.Undo) {
            html += '<div class="titleDiv"><input class="titleFinish" id="input' + (index + 1) + '" type="text" readonly value="' + content.Title + '"></div>';
            html += '<div class="controlDiv"><button onclick="isFinish(this.id,' + content.Undo + ')" name="Done" id="Dbutton' + (index + 1) + '">Done</button>';
        } else {
            html += '<div class="titleDiv"><input class="titleUnFinish" id="input' + (index + 1) + '" type="text" readonly="readonly" value="' + content.Title + '"></div>';
            html += '<div class="controlDiv"><button onclick="isFinish(this.id,' + content.Undo + ')" name="Undo" id="Dbutton' + (index + 1) + '">Undo</button>';
        }
        html += '<button onclick="editRecord(this.id)"  valueText="" id="Ebutton' + (index + 1) + '">Edit</button>';
        html += '<button onclick="RemoveRecord(this.id)" id="Rbutton' + (index + 1) + '">Remove</button></div>';
        html += '<hr/>'
    }
    return html;
}

// 显示 左下角的计数器
function displayCount() {
    let UndoCount = document.getElementsByName("Undo").length;
    let DoneCount = document.getElementsByName("Done").length;
    document.getElementById("allCount").innerText = "All(" + (UndoCount + DoneCount) + ")"
    document.getElementById("doneCount").innerText = "Done(" + DoneCount + ")"
    document.getElementById("activeCount").innerText = "All(" + UndoCount + ")"
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
    let isReadonly = document.getElementById(inputId).readOnly;
    if (isReadonly) {
        document.getElementById(inputId).readOnly = false;
        document.getElementById('Ebutton' + id.substring(7)).innerText = "Save";
        document.getElementById('Ebutton' + id.substring(7)).valueText = document.getElementById(inputId).value;
    } else {
        document.getElementById(inputId).readOnly = true;
        document.getElementById('Ebutton' + id.substring(7)).innerText = "Edit";
        let oldText = document.getElementById('Ebutton' + id.substring(7)).valueText;
        let newText = document.getElementById(inputId).value;
        ajax_request('/editRecord?condition=' + oldText + '&newText=' + newText)
    }

}

//ajax的请求
function ajax_request(url) {
    $.ajax({
        url: url,
        dataType: 'json',
        type: 'POST',
        async: false,
        success: function(data) {
            $("#Content").html(displayContent(data))
            displayCount()
        }
    })
}
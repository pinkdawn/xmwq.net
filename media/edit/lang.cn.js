(function ($) {
    if (undefined === $.wysiwyg) {
    throw "lang.cn.js depends on $.wysiwyg";
}
if (undefined === $.wysiwyg.i18n) {
    throw "lang.cn.js depends on $.wysiwyg.i18n";
}

$.wysiwyg.i18n.lang.cn = {
    controls: {
    "Bold": "加粗",
    "Colorpicker": "颜色选择",
    "Copy": "复制",
    "Create link": "创建链接",
    "Cut": "剪切",
    "Decrease font size": "减少字体",
    "Fullscreen": "全屏",
    "Header 1": "标题1",
    "Header 2": "标题2",
    "Header 3": "标题3",
    "View source code": "查看源代码",
    "Increase font size": "增加字体",
    "Indent": "缩进",
    "Insert Horizontal Rule": "插入水平线",
    "Insert image": "插入图片",
    "Insert Ordered List": "插入有序列表",
    "Insert table": "插入表格",
    "Insert Unordered List": "插入无序列表",
    "Italic": "斜体字",
    "Justify Center": "居中",
    "Justify Full": "分散对齐",
    "Justify Left": "左对齐",
    "Justify Right": "右对齐",
    "Left to Right": "从左到右",
    "Outdent": "减少缩进",
    "Paste": "粘帖",
    "Redo": "重做",
    "Remove formatting": "去除格式",
    "Right to Left": "从右到左",
    "Strike-through": "删除线",
    "Subscript": "下标",
    "Superscript": "上标",
    "Underline": "下划线",
    "Undo": "撤销"
    },

dialogs: {
    // for all
    "Apply": "应用",
    "Cancel": "取消",
    
    colorpicker: {
    "Colorpicker": "选择颜色",
    "Color": "颜色"
},

image: {
    "Insert Image": "插入图片",
    "Preview": "预览",
    "URL": "地址",
    "Title": "标题",
    "Description": "描述",
    "Width": "宽度",
    "Height": "高度",
    "Original W x H": "原始 宽度 X 高度",
    "Float": "图片靠",
    "None": "无",
    "Left": "左",
    "Right": "右"
},

link: {
    "Insert Link": "插入链接",
    "Link URL": "链接地址",
    "Link Title": "链接标题",
    "Link Target": "链接目标"
},

table: {
    "Insert table": "插入表格",
    "Count of columns": "行数",
    "Count of rows": "列数"
}
}
};
})(jQuery);
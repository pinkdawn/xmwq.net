/**
 * 2012-5-8 by Daoyu.
 */

function do_search_title(keyword) {
	if (keyword && keyword.length != 0) {
		keyword = encodeURIComponent(keyword);
		location.href = "/bbs/search/" + keyword + "/";
	} else {
		location.href = "/";
	}
}

/*
 * 打印分页的当前页面，及离其最近的前后页面。
 * currentPage: 当前页面数。
 * totalPage: 总共页面数
 * numOfPages: 分别显示前后多少页面。
 * 如 currentPage=4, totalPage=7, numOfPages=2，则显示 2,3,4,5,6
 */
 function page(currentPage, totalPage, numOfPages){                
     //输出当前页面往后4个页面的导航按钮
     for (var index = (currentPage + numOfPages) > totalPage ? totalPage : (currentPage + numOfPages);index> currentPage;index --)
         document.write("<div class='page'><a href='?page=" + index + "'>" + index + "</a></div>");
     
     document.write("<div class='page'><a href='?page=" + currentPage + "'><strong>"+currentPage+"</strong></div>");
     if (currentPage == 1) return ;
         
     //输出当前页面往前4个页面的导航按钮
     var stopIndex = (currentPage - numOfPages) < 1 ? 1 : (currentPage - numOfPages);                
     var startIndex = (currentPage -1) < 1 ? 1:(currentPage-1);                
         
     for(var index = startIndex;index >= stopIndex;index--){                    
         document.write("<div class='page'><a href='?page=" + index + "'>" + index + "</a></div>");
     }
 }
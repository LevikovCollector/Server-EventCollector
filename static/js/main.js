$(document).ready(function(){
    $("#reset-button").bind("click", function(event){
        event.preventDefault();
        var ch_chrome = $("#show_chrome_info").is(':checked');
        var ch_pycharm = $("#show_pycharm_info").is(':checked');
        var ch_sublime = $("#show_sublime_info").is(':checked');
        
        if(ch_chrome)
        {   
            show_or_hide("th-google", "table.table.table-striped>tbody>tr.all-data>td#active_tab_url", 1)
        }
        else
        {
            show_or_hide("th-google", "table.table.table-striped>tbody>tr.all-data>td#active_tab_url", 0)
        }

        if(ch_pycharm)
        {   
            show_or_hide("th-pycharm", "table.table.table-striped>tbody>tr.all-data>td#pycharm_project", 1)
        }
        else
        {
            show_or_hide("th-pycharm", "table.table.table-striped>tbody>tr.all-data>td#pycharm_project", 0)
        }

        if(ch_sublime)
        {   
            show_or_hide("th-sublime", "table.table.table-striped>tbody>tr.all-data>td#sublime_path", 1)
        }
        else
        {
            show_or_hide("th-sublime", "table.table.table-striped>tbody>tr.all-data>td#sublime_path", 0)
        }

    });
});

function show_or_hide(th_id, td_selector, show)
{
    if(show)
    {
        document.getElementById(th_id).className="table-all-data hidden-lg hidden-md hidden-sm"
        var chrm_col = document.querySelectorAll(td_selector)
        for(i=0;i<chrm_col.length;i++)
        {
            chrm_col[i].className="hidden-lg hidden-md hidden-sm"
        }
    }
    else
    {
        document.getElementById(th_id).className="table-all-data"
        var chrm_col = document.querySelectorAll(td_selector)
        for(i=0;i<chrm_col.length;i++)
        {
            chrm_col[i].className="None"
        }
    }
    
}
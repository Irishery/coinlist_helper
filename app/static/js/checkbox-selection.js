$(function(){

    //button select all or cancel
    $("#select-all").click(function () {
        var all = $("input.select-all")[0];
        all.checked = !all.checked
        var checked = all.checked;
        $("input.select-item").each(function (index,item) {
            item.checked = checked;
        });
    });

    //button select invert
    $("#select-invert").click(function () {
        $("input.select-item").each(function (index,item) {
            item.checked = !item.checked;
        });
        checkSelected();
    });

    //button get selected info
    $("button.start-checked-btn").click(function () {
        var items=[];
        $("input.select-item:checked:checked").each(function (index,item) {
            items[index] = item.value;
        });
        if (items.length < 1) {
            alert("no selected items!!!");
        }else {
            console.log(items);
        }
    });

    //column checkbox select all or cancel
    $("input.select-all").click(function () {
        var checked = this.checked;
        $("input.select-item").each(function (index,item) {
            item.checked = checked;
        });
    });

    //check selected items
    $("input.select-item").click(function () {
        var checked = this.checked;
        checkSelected();
    });

    // $("button.start-checked-btn").click(function () {
    //     let checked
    // });

    //check is all selected
    function checkSelected() {
        var all = $("input.select-all")[0];
        var total = $("input.select-item").length;
        var len = $("input.select-item:checked:checked").length;
        all.checked = len===total;
    }
});
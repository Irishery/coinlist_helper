document.addEventListener('click', event => {
    target = event.target
    if (target.id == 'cancel-editing') {
        row = document.getElementById("edit-row" + target.value)
        row.style.display = "none"
    }

    if (target.id == 'edit-btn') {
        row = document.getElementById("edit-row" + target.value)
        console.log(row)
        row.style.display = "table-row"
    }
})

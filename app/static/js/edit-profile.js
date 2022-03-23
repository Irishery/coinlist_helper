let edit_block = document.getElementById("user-edit")
let user_info = document.getElementById("user-info")

document.getElementById("show-edit").onclick = () => {
    console.log(user_info)
    user_info.style.display = "none"
    edit_block.style.display = "block"
}

document.getElementById("save").onclick = () => {
    user_info.style.display = "block"
    edit_block.style.display = "none"
}

document.getElementById("cancel").onclick = () => {
    user_info.style.display = "block"
    edit_block.style.display = "none"
}

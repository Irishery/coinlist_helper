const get_user = (id) => {
    const request = new Request('http://127.0.0.1:5000/api/user/?' + new URLSearchParams({
        action: 'ping',
        id: id
    }),
    {method: 'GET'});

    return fetch(request)
    .then(response => {
        if (response.status === 200) {
        return response.json();
        } else {
        throw new Error('Something went wrong on api server!');
        }
    })
    .then(response => {
        return response
    }).catch(error => {
        console.error(error);
    });
}


document.addEventListener('click', async (event) => {
    target = event.target
    if (target.id == 'cancel-editing') {
        row = document.getElementById("edit-row" + target.value);
        row.remove();
    }

    if (target.id == 'edit-btn') {
        let edit_row = document.getElementById("show-info" + target.value)
        let rows = document.getElementsByClassName("row" + target.value)
        if (rows.length > 0) {
          return
        }
        user = await get_user(target.value);
        edit_row.insertAdjacentHTML('afterend',
        `<tr class="edit-row row${user.id}" id="edit-row${user.id}">
        <td class="active" id="${user.id}">
          <input type="checkbox" disabled="disabled" class="select-item checkbox" name="select-item" value="${user.id}" />
        </td>
        <td>
          <button id="save-changes" form="${user.id}" type="submit" class="btn btn-dark btn" value="${user.id}">Save</button>
        </td>
        <td>
          <button id="cancel-editing" type="button" class="btn btn-danger" value="${user.id}">Cancel</button>
        </td>
          <td><input name="name" form="${user.id}" default="${user.name}" value="${user.name}" class="form-control"></td>
        <td>
          <select name="platform" form="${user.id}" class="form-select" aria-label="${user.platform}">
            <option value="${user.platform}">conlist</option>
          </select>
        </td>
          <td><input name="login" form="${user.id}" default="${user.login}" value="${user.login}" class="form-control"></td>
          <td><input name="info" form="${user.id}" default="${user.info}" value="${user.info}" class="form-control"></td>
          <td><input name="proxy_host" form="${user.id}" default="${user.proxy_host}" value="${user.proxy_host}" class="form-control"></td>
          <td><input name="proxy_port" form="${user.id}" default="${user.proxy_port}" value="${user.proxy_port}" class="form-control"></td>
          <td><input name="proxy_login" form="${user.id}" default="${user.proxy_login}" value="${user.proxy_login}" class="form-control"></td>
          <td><input name="proxy_pass" form="${user.id}" default="${user.proxy_pass}" value="${user.proxy_pass}" class="form-control"></td>
          <td><input name="user_agent" form="${user.id}" default="${user.user_agent}" value="${user.user_agent}" class="form-control"></td>
          <td><input name="unmasked_vendor" form="${user.id}" default="${user.unmasked_vendor}" value="${user.unmasked_vendor}" class="form-control"></td>
          <td><input name="unmasked_renderer" form="${user.id}" default="${user.unmasked_renderer}" value="${user.unmasked_renderer}" class="form-control"></td>
          <td><input name="resolution" form="${user.id}" default="${user.resolution}" value="${user.resolution}" class="form-control"></td>
      </tr>`);
    }
})

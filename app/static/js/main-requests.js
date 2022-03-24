"use strict";

document.addEventListener('click', event => {
    target = event.target
    if (target.id == 'start_up') {
        const request = new Request('http://127.0.0.1:5000/api/selenium/?' + new URLSearchParams({
            action: 'ping',
            user_id: target.value
        }));

        const url = request.url;

        console.log(url)

        fetch(request)
        .then(response => {
            if (response.status === 200) {
            return response.json();
            } else {
            throw new Error('Something went wrong on api server!');
            }
        })
        .then(response => {
            console.debug(response);
            // ...
        }).catch(error => {
            console.error(error);
        });
    }
})
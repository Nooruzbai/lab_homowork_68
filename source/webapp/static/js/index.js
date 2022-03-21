  async function make_request(url, method = 'GET') {
        let response = await fetch(url, {method})
        if (response.ok) {
            console.log('OK')
            return await response.json();
        } else {
            console.log('Not Successful')
            let error = new Error(response.statusText);
            error.response = response;
            throw error;
        }

    }


    let Like = async function (event){

        let url=event.target.dataset.articlesUrl;

            let data = await make_request(url)
            let counter = document.getElementById(`${event.target.dataset.id}`);
            counter.innerText = `${data.like_quantity}`

            let button = document.getElementById(event.target.dataset.id)
                button.innerText = "Unlike"

    }


  let LikeComment = async function(event){

    let url=event.target.dataset.articlesUrl;

        let data = await make_request(url)
        let counter = document.getElementById(`${event.target.dataset.id}`);
        console.log(counter)
        counter.innerText = `${data.like_quantity}`

}

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


let LikeArticle = async function (event) {

    let url = event.target.dataset.articlesUrl;

    let data = await make_request(url)
     console.log()
    let counter = document.getElementById(`${event.target.dataset.id}`);
    counter.innerText = `${data.like_quantity}`
    let like_button = document.getElementById('like')
    let button = event.target
    if (button.innerText == "unlike") {
        button.innerText = "like"

    } else {
        button.innerText = "unlike"
    }

}

// let UnLikeArticle = async function (event) {
//
//     let url = event.target.dataset.articlesUrl;
//
//     let data = await make_request(url)
//     let counter = document.getElementById(`${event.target.dataset.id}`);
//     counter.innerText = `${data.like_quantity}`
//
// }


let LikeComment = async function (event) {

    let url = event.target.dataset.articlesUrl;

    let data = await make_request(url)
    let counter = document.getElementById(`${event.target.dataset.id}`);
    console.log(counter)
    counter.innerText = `${data.like_quantity}`
    let button = event.target
    if (button.innerText == "unlike") {
        button.innerText = "like"

    } else {
        button.innerText = "unlike"

    }
}
    // let UnLikeComment = async function (event) {
    //
    //     let url = event.target.dataset.articlesUrl;
    //
    //     let data = await make_request(url)
    //     let counter = document.getElementById(`${event.target.dataset.id}`);
    //     console.log(counter)
    //     counter.innerText = `${data.like_quantity}`
    //
    // }

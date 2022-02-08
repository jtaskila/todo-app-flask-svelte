import {api_url} from '../config.js'

// url      = endpoint url
// request  = fetch request object
// success  = callback function for succesfull request
// failure  = callback function for failed request
// done = callback function always executed after request
function ApiCall(url, request, success, failed, done = null){
    let full_url = api_url+url
    fetch(full_url, request)
    .then(response => response.json().then(data => ({
        status: response.status,
        data: data
    })))
    .then(response => {
        success(response)
        if(done != null){
            done()
        }
    })
    .catch(error => {
        failed(error)
        if(done != null){
            done()
        }
    })
}

export default ApiCall

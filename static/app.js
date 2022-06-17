
    axios.get('http:://127.0.0.1:5000/ratings')
        .then(response => {
            
            console.log(response);
        })
        .catch(error => console.error(error));

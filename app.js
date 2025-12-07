function startCounter() {
    
    document.getElementById("score").innerHTML = "Counting..." //can set html of that tag

    fetch("http://127.0.0.1:5000/count")
        .then(response => response.json())
        .then(data => {
            document.getElementById("score").innerHTML = 
            "Score : " + data.score;
            console.log(data.score)
        })
        //err handing?

}
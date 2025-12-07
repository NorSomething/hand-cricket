function startCounter() {
    
    document.getElementById("score").innerHTML = "Counting..." //can set html of that tag

    fetch("http://127.0.0.1:5000/count") //defaults to get
        .then(response => response.json())
        .then(data => {
            document.getElementById("score").innerHTML = 
            "Score : " + data.score;
            document.getElementById("cpu_move").innerHTML = 
            "CPU Move : " + data.cpu_move
            console.log(data.score)
        })
        //err handing?

}


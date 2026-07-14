const guessText = document.getElementById("guess");

const lowBtn = document.getElementById("low");

const highBtn = document.getElementById("high");

const correctBtn = document.getElementById("correct");

const restartBtn = document.getElementById("restart");

const attemptsText = document.getElementById("attempts");

async function loadGuess(){

    const response = await fetch("/guess");

    const data = await response.json();

    guessText.innerText = data.guess;

}

loadGuess();

async function send(action){

    const response = await fetch("/feedback",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            action:action
        })

    });

    const data = await response.json();

    guessText.innerText = data.guess;
    attemptsText.innerText = "Attempts: " + data.attempts;

}

lowBtn.onclick=()=>send("low");

highBtn.onclick=()=>send("high");

restartBtn.onclick=()=>{

    send("reset");

}

correctBtn.onclick = () => {

    guessText.innerHTML = "🎉 AI guessed correctly!";
    attemptsText.innerHTML = "Total Attempts: " + attemptsText.innerText.split(": ")[1];

    lowBtn.disabled = true;
    highBtn.disabled = true;
    correctBtn.disabled = true;

}

restartBtn.onclick=()=>{

    lowBtn.disabled=false;

    highBtn.disabled=false;

    correctBtn.disabled=false;

    send("reset");

}
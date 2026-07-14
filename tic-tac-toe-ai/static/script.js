const cells = document.querySelectorAll(".cell");

const statusText = document.getElementById("status");

const restartBtn = document.getElementById("restart");

let board = [
    " "," "," ",
    " "," "," ",
    " "," "," "
];

let humanScore = 0;
let aiScore = 0;
let drawScore = 0;

let gameOver = false;

const wins = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
];

cells.forEach(cell=>{

    cell.addEventListener("click",humanMove);

});

restartBtn.addEventListener("click",restartGame);

function humanMove(){

    if(gameOver)
        return;

    const index = Number(this.dataset.index);

    if(board[index]!=" ")
        return;

    board[index]="X";

    render();

    let result = checkWinner();

    if(result){

        finishGame(result);

        return;

    }

    statusText.innerText="AI Thinking...";

    setTimeout(aiMove,500);

}

async function aiMove(){

    const response = await fetch("/ai_move",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            board:board
        })

    });

    const data = await response.json();

    if(data.move!=-1){

        board[data.move]="O";

    }

    render();

    let result = checkWinner();

    if(result){

        finishGame(result);

        return;

    }

    statusText.innerText="Your Turn";

}

function render(){

    for(let i=0;i<9;i++){

        cells[i].innerText = board[i];

    }

}

function checkWinner(){

    for(let win of wins){

        let a = win[0];

        let b = win[1];

        let c = win[2];

        if(
            board[a]!=" " &&
            board[a]==board[b] &&
            board[b]==board[c]
        ){

            return board[a];

        }

    }

    if(!board.includes(" ")){

        return "Draw";

    }

    return null;

}
function finishGame(result){

    gameOver = true;

    if(result === "X"){

        statusText.innerText = "You Win!";
        humanScore++;
        document.getElementById("humanScore").innerText = humanScore;

    }
    else if(result === "O"){

        statusText.innerText = "AI Wins!";
        aiScore++;
        document.getElementById("aiScore").innerText = aiScore;

    }
    else{

        statusText.innerText = "It's a Draw!";
        drawScore++;
        document.getElementById("drawScore").innerText = drawScore;

    }

}

function restartGame(){

    board = [
        " "," "," ",
        " "," "," ",
        " "," "," "
    ];

    gameOver = false;

    statusText.innerText = "Your Turn";

    render();

}

render();
let taskWord="";
let mainLangWords = [];
let secondLangWords = [];
let wordsToRemember = [];
let appStatus = "TextToRemember";
let roundNumber = 0;
function appAction(actionButtonID, wordsQuantity, mainWords, secondWords) {
    let actionButton = document.getElementById(actionButtonID)
    if (appStatus === "TextToRemember") {
        // set tuples with words on both languages
        mainLangWords = mainWords;
        secondLangWords = secondWords;
        // set words to remember (list of words which will be decrease by 1 each round)

        // hide rows with words to remeber
        for (let i = 0; i < wordsQuantity; i++){
            let row = document.getElementById("wordRow_" + i);
            row.style.display = 'none'
            }
        // set to application round conditions
        appRound(mainLangWords, mainLangWords);

        actionButton.style.display = "none";
        appStatus = "Next round";
    } else if (appStatus === "Next round") {
//         getSupportActionBar().setTitle(Title_line[1][second_language] + (11 - temp_main_list.size()));
//
//         set_initial();
//         game_round();
// //                    CentralTextView.setMinWidth(1);
//         TransitionManager.beginDelayedTransition(tContainer);
// //                    CentralTextView.setMinWidth(1);
// //                    CentralTextView.setText(task_word);
//         Word11.setText(task_word);
// //                    RunAnimation();
//
//
//         button1.setText(answer_list.get(0));
//
//         button2.setText(answer_list.get(1));
//
//         button3.setText(answer_list.get(2));
//
//         button4.setText(answer_list.get(3));
//         button5.setVisibility(View.INVISIBLE);
//         if (temp_main_list.size() == 0) {
//             GameStatus = "Result";
//         }

    } else if (appStatus === "Result") {
//         task_word = "";
//         getSupportActionBar().setTitle(Title_line[2][second_language]);
//         button1.setVisibility(View.GONE);
//
//         button2.setVisibility(View.GONE);
//
//         button3.setVisibility(View.GONE);
//
//         button4.setVisibility(View.GONE);
//         //button5.setText("OK");
//         button5.setVisibility(View.VISIBLE);
//
// //                    CentralTextView.setText("");
// //                    LeftTextView.setText("");
// //                    RightTextView.setText("");
//         TransitionManager.beginDelayedTransition(tContainer);
//
// //                    CentralTextView.setText("Result: " + String.valueOf(correct_answers) + "/10");
//         Word11.setText(String.valueOf(correct_answers) + "/10");
//
//         Intent
//         intent = new Intent();
//         intent.putExtra("percentage", String.valueOf(correct_answers * 10));
//         setResult(RESULT_OK, intent);
//
//         GameStatus = "End";

    }
}


function appRound() {
    // increase round number
    roundNumber +=1;
    // taking task words from array
    let taskWordIndex = Math.floor(Math.random() * ( wordsToRemember.length + 1));
    console.log(taskWordIndex);
    taskWord = wordsToRemember[taskWordIndex];
    console.log(taskWordIndex);
    // deleting task word from array of words to learn
    wordsToRemember = wordsToRemember.splice(taskWordIndex);
    console.log(wordsToRemember);
    // index of correct words
    let answerIndex = secondLangWords.indexOf(taskWord);
    // getting correct answer word
    let answerWord = mainLangWords[answerIndex];
    console.log(answerWord);
    // adding correct answer to array of round answers
    let answers = [];
    answers.push(answerWord);
    // temp array to get incorrect answers
    let tempMainLangWords = mainLangWords;
    // deleting correct answer
    tempMainLangWords = tempMainLangWords.splice(answerIndex);
    // getting 3 random incorrect answers
    for (let i =0; i<3; i++){
        taskWordIndex = Math.floor(Math.random() * ( tempMainLangWords.length + 1));
        answers.push(tempMainLangWords[taskWordIndex]);
        tempMainLangWords.splice(taskWordIndex);
    }
    console.log(answers)

}
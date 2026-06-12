function Questions({ count }) {
    let questionText = "";

    if (count === 0) {
        questionText = "Welcome to the Quiz";
    }
    else if (count === 1) {
        questionText = "What is the Capital of France?";
    }
    else if (count === 2) {
        questionText = "What is the tallest Mountain in the world?";
    }
    else if (count === 3) {
        questionText = "What is the largest animal in the world?";
    }
    else if (count === 4) {
        questionText = "What is the biggest planet in our solar system?";
    }
    else if (count === 5) {
        questionText = "What is the most abundant element in the atmosphere?";
    }

    return <h2>{questionText}</h2>;
}

export default Questions;
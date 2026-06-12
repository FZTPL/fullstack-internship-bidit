function Answer({ count, showAnswer }) {
    let answer = "";

    if (count === 1) {
        answer = "Paris";
    }
    else if (count === 2) {
        answer = "Mount Everest";
    }
    else if (count === 3) {
        answer = "Blue Whale";
    }
    else if (count === 4) {
        answer = "Jupiter";
    }
    else if (count === 5) {
        answer = "Nitrogen";
    }

    return (
        <>
            {showAnswer && <p>{answer}</p>}
        </>
    );
}

export default Answer;
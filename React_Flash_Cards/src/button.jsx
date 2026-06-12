function Button({ setCount, showAnswer, setShowAnswer }) {
    return (
        <div className="button-container">
            <button
                onClick={() => {
                    setCount(prev => (prev > 0 ? prev - 1 : prev));
                    setShowAnswer(false);
                }}
            >
                Previous
            </button>

            <button
                onClick={() => setShowAnswer(prev => !prev)}
            >
                {showAnswer ? "Hide Answer" : "Show Answer"}
            </button>

            <button
                onClick={() => {
                    setCount(prev => (prev < 5 ? prev + 1 : prev));
                    setShowAnswer(false);
                }}
            >
                Next
            </button>
        </div>
    );
}

export default Button;
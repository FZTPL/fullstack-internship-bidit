import "./index.css";
import { useState } from "react";

import Percent from "./percentage.jsx";
import Button from "./button.jsx";
import Questions from "./questions.jsx";
import Answer from "./answer.jsx";

function App() {
    const [count, setCount] = useState(0);
    const [showAnswer, setShowAnswer] = useState(false);

    return (
        <div className="app-container">
            <h1>Quiz</h1>

            <Percent count={count} />

            <div className="question-container">
                <Questions count={count} />
            </div>

            <div className="answer-container">
                <Answer
                    count={count}
                    showAnswer={showAnswer}
                />
            </div>

            <Button
                setCount={setCount}
                showAnswer={showAnswer}
                setShowAnswer={setShowAnswer}
            />
        </div>
    );
}

export default App;
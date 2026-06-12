function Percent({ count }) {
    return (
        <h2>
            {count} of 5 — {Math.round((count / 5) * 100)}% Completed
        </h2>
    );
}

export default Percent;
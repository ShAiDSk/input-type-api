import { useState, useEffect } from "react";

export default function App() {
  const [input, setInput] = useState("");
  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);

  const handleCheck = async () => {
    const res = await fetch("http://127.0.0.1:5000/check", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ input }),
    });
    const data = await res.json();
    setResult(data);
    fetchHistory();
  };

  const fetchHistory = async () => {
    const res = await fetch("http://127.0.0.1:5000/history");
    const data = await res.json();
    setHistory(data);
  };

  useEffect(() => {
    fetchHistory();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-6">
      <div className="bg-white shadow-xl rounded-2xl p-8 w-full max-w-lg">
        <h1 className="text-2xl font-bold text-center mb-6">🔍 Input Type Checker</h1>

        <div className="flex space-x-2 mb-4">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Enter text, number, or hash..."
            className="flex-1 px-4 py-2 border rounded-xl focus:ring focus:ring-blue-300"
          />
          <button
            onClick={handleCheck}
            className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-xl"
          >
            Check
          </button>
        </div>

        {result && (
          <div className="p-4 border rounded-xl bg-green-50 text-center mb-4">
            <p className="font-semibold">Input: <span className="text-gray-700">{result.input}</span></p>
            <p className="text-lg font-bold text-green-700">Detected: {result.type}</p>
          </div>
        )}

        {/* History */}
        <div className="mt-6">
          <h2 className="text-xl font-semibold mb-2">📜 Last 5 Checks</h2>
          <ul className="space-y-2">
            {history.map((item, idx) => (
              <li key={idx} className="p-2 bg-gray-50 border rounded-lg">
                <span className="font-semibold">{item.input}</span> → <span className="text-blue-600">{item.type}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

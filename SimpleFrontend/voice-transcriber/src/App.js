import './App.css';
import AudioRecorder from "./Components/AudioRecorder/AudioRecorder"

function App() {
  return (
      <div className="App">
          <header className="App-header">
              <h1>Voice Transcriber</h1>
              <AudioRecorder />
          </header>
      </div>
  );
}

export default App;

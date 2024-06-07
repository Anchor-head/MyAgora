// src/AudioRecorder.js
import React, { useState, useCallback ,useContext} from 'react';
import { UserContext } from '../../Contexts/UserContext';
import { ReactMediaRecorder } from 'react-media-recorder';
import axios from 'axios';
import './AudioRecorder.css';

const AudioRecorder = () => {
  const { user } = useContext(UserContext);
  const [transcription, setTranscription] = useState('');

  const handleStop = useCallback(async (blobUrl, blob) => {
    const formData = new FormData();
    formData.append('file', blob, 'audio.wav');

    try {
      const response = await axios.post('http://localhost:8000/transcribe/', formData, {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
      });
      console.log(response.data)
      setTranscription(response.data.transcription);
    } catch (error) {
      console.error('Error transcribing audio:', error);
    }
  }, []);

  return (
    <div className="audio-recorder">
      {user && <p>Logged in as: {user.username}</p>}
      <ReactMediaRecorder
        audio
        blobPropertyBag={{ type: 'audio/wav' }}
        onStop={handleStop}
        render={({ startRecording, stopRecording }) => (
          <div>
            <button
              onMouseDown={startRecording}
              onMouseUp={stopRecording}
              onTouchStart={startRecording}
              onTouchEnd={stopRecording}
              className="record-button"
            >
              Hold to Record
            </button>
            <p>{transcription}</p>
          </div>
        )}
      />
    </div>
  );
};

export default AudioRecorder;

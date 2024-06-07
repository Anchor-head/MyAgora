import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Register from './Components/Register/Register';
import Login from './Components/Login/Login';
import AudioRecorder from './Components/AudioRecorder/AudioRecorder';
import ProtectedRoute from './Components/ProtectedRoute';
import MainPage from './Components/MainPage/MainPage';

const App = () => {
    return (
        <Router>
            <h1>Agora</h1>
            <Routes>
                <Route path="/" element={<MainPage />} />
                <Route path="/register" element={<Register />} />
                <Route path="/login" element={<Login />} />
                <Route
                    path="/audiorecorder"
                    element={
                        <ProtectedRoute>
                            <AudioRecorder />
                        </ProtectedRoute>
                    }
                />
            </Routes>
        </Router>
    );
};

export default App;

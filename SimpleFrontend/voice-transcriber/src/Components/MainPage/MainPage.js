import React from 'react';
import { useNavigate } from 'react-router-dom';
import './MainPage.css';

const MainPage = () => {
    const navigate = useNavigate();

    return (
        <div className="main-container">
            <div className="button-group">
                <button onClick={() => navigate('/register')} className="main-button">Register</button>
                <button onClick={() => navigate('/login')} className="main-button">Login</button>
            </div>
        </div>
    );
};

export default MainPage;

import React, { useState } from 'react';
import './App.css';
import Login from './components/login/Login'
import Dashboard from './components/dashboard/Dashboard';
import useToken from './useToken';
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";

function App() {
  const { token, setToken } = useToken();

  function redirectToLogin(page) {
    if (!token) {
      return <Navigate to="/login" />;
    }
    return page;
  }
    return (
      <div className="App">
        <Router>
          <Routes>
            <Route path="/" element={redirectToLogin(<Dashboard/>)} />
            <Route path="/login" element={<Login setToken={setToken}/>} />
          </Routes>
        </Router>
      </div>
    );
}

export default App;
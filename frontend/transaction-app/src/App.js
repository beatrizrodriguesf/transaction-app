import React, { useState } from 'react';
import './App.css';
import Login from './components/login/Login'
// import { BrowserRouter, Route, Routes } from 'react-router-dom';

function setToken(userToken) {
  sessionStorage.setItem('token', JSON.stringify(userToken));
}

function getToken() {
  const tokenString = sessionStorage.getItem('token');
  const userToken = JSON.parse(tokenString);
  return userToken?.token
}

function App() {
  const token = getToken();

  if(!token) {
    return <Login setToken={ setToken } />
  }

  return (
    <div className="wrapper">
      <h1>Application</h1>
    </div>
  );
}

export default App;
import React, { useState } from 'react';
import './App.css';
import Login from './components/login/Login'
import useToken from './useToken';

function App() {
  const { token, setToken } = useToken();

  if(!token) {
    return <Login setToken={setToken} />
  }

  return (
    <div className="wrapper">
      <h1>Application</h1>
    </div>
  );
}

export default App;
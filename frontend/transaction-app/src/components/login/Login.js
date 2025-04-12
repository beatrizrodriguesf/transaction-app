import React, { useState } from 'react';
import './Login.css';
import axios from 'axios'
import {useNavigate} from 'react-router-dom';

async function loginUser(credentials) {
    return axios.post('http://localhost:8000/login', credentials)
      .then(response => response.data)
      .catch(e=>console.log(e))
   }

export default function Login({ setToken }) {
    const [email, setEmail] = useState();
    const [password, setPassword] = useState();
    const navigate = useNavigate();

    const handleSubmit = async e => {
        e.preventDefault();
        const token = await loginUser({
          'email':email,
          'password':password
        });
        setToken(token);
        if (token) {
            navigate("/");
        }
      }

      const handleCadastrar = async e => {
        e.preventDefault();
        navigate("/register");
      };
    
    return(
        <div className="login-wrapper">
        <h1>Please Log In</h1>
        <form>
            <label>
            <p>email</p>
            <input type="email" onChange={e => setEmail(e.target.value)}/>
            </label>
            <label>
            <p>Password</p>
            <input type="password" onChange={e => setPassword(e.target.value)}/>
            </label>
            <div className ="buttons">
              <div>
              <button onClick={handleSubmit} type="submit">Login</button>
              </div>
              <div>
              <button onClick={handleCadastrar}>Cadastrar</button>
              </div>
            </div>
        </form>
        </div>
    )
}
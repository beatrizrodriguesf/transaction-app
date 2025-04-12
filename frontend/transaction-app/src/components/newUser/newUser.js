import React, { useState } from 'react';
import axios from 'axios'
import {useNavigate} from 'react-router-dom';
import '../login/Login.css'

async function createUser(info) {
    return axios.post('http://localhost:8000/registrar', info)
      .then(response => response.data)
      .catch(e=>console.log(e))
   }

export default function Register() {
    const [email, setEmail] = useState();
    const [password, setPassword] = useState();
    const [name, setName] = useState();
    const [birthDate, setBirthDate] = useState();

    const navigate = useNavigate();

    const handleSubmit = async e => {
        e.preventDefault();
        const token = await createUser({
          'name':name,
          'email':email,
          'password':password,
          'birthDate':birthDate
        });
        if (token) {
            navigate("/login");
        }
      }

    const handleVoltar = async e => {
        e.preventDefault();
        navigate("/login");
      };
    
    
    return(
        <div className="login-wrapper">
        <h1>Cadastro</h1>
        <form>
            <label>
            <p>nome completo</p>
            <input onChange={e => setName(e.target.value)}/>
            </label>
            <label>
            <p>data de nascimento</p>
            <input type="date" onChange={e => setBirthDate(e.target.value)}/>
            </label>
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
                <button onClick={handleSubmit} type="submit">Cadastrar</button>
                </div>
                <div>
                <button onClick={handleVoltar}>Voltar</button>
                </div>
            </div>
        </form>
        </div>
    )
}
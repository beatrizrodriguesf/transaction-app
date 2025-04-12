import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Dashboard.css';
import DropdownButton from './Dropdown';

export default function Dashboard() {
    const [transacoes, setTransacoes] = useState([]);
    const [categoria, setCategoria] = useState();
    const [categorias, setCategorias] = useState();

    const handleOptionSelect = (option) => {
        setCategoria(option); // Atualiza o estado com a opção clicada
    };    

    useEffect(() => {
        if (categoria == undefined) {
            axios.get('http://localhost:8000/transacoes/', {
                headers: {
                    Authorization: 'Bearer ' + sessionStorage.getItem('token')
                }
            })
            .then((response) => setTransacoes(response.data))
            .catch(e=>console.log(e))
        }
        else {
            axios.get(`http://localhost:8000/transacoes/${categoria}`, {
                headers: {
                    Authorization: 'Bearer ' + sessionStorage.getItem('token')
                }
            })
            .then((response) => setTransacoes(response.data))
            .catch(e=>console.log(e))
        }
    }, [categoria])

      useEffect(() => {
        axios.get('http://localhost:8000/categorias/', {
            headers: {
                Authorization: 'Bearer ' + sessionStorage.getItem('token')
              }
        })
          .then((response) => setCategorias(response.data))
          .catch(e=>console.log(e))
    }, [])
    
    return(
        <div className = "dashboard">
            <h2>Dashboard</h2>
            <div className='filtros'>
                <h3>Filtros</h3>
                <div>
                    <DropdownButton name="categorias" options={categorias} onOptionSelect={handleOptionSelect}/>
                </div>
                <h3>Transações</h3>
            </div>
            <div className='transacoes'>
                {transacoes.map((transacao, index) => (
                    <div className = "transaction" key = {index}>
                        <i className = {`material-icons ${transacao["type"]==="revenue" ? 'revenue' : 'expense'}`}> 
                        {transacao["type"]==="revenue" ? 'add_circle' : 'remove_circle'}</i>
                        <div className = "info">
                            <div className = "top-line">
                                <p> {transacao["category"]}</p>
                                <p>R$ {transacao["value"]}</p>
                            </div>
                            <p className = "details" >{transacao["details"]}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}
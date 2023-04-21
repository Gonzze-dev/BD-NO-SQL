import React, { useState } from 'react';

import './formGetChacaters.css'
import { linkApi } from '../config';

const FormGetChacaters = () => {
  const [capitulo, setCapitulo] = useState('');
  const [personajes, setPersonajes] = useState([]);

  const link = `${linkApi}/getCharacters/${capitulo}`

  const handleCapituloChange = (e) => {
    setCapitulo(e.target.value);
  }

  const handleListarClick = () => {
    // Realizar búsqueda en la API utilizando el número del capítulo ingresado
    fetch(link)
      .then(response => response.json())
      .then(data => setPersonajes(data))
      .catch(error => console.error(error));

    alert(`Personajes del capitulo ${capitulo} obtenidos con exito!`)
  }

  return (
    <div className="formulario-container">
      <h2>Listar personajes de un capitulo</h2>
      <form>
        <label htmlFor="capitulo">Número del Capítulo:</label>
        <input type="number" id="capitulo" value={capitulo} onChange={handleCapituloChange} />
        <button className='button-getCharacters' type="button" onClick={handleListarClick}>Listar</button>
      </form>
      <table>
        <thead>
          <tr>
            <th>Nombre del Personaje</th>
          </tr>
        </thead>
        <tbody>
          {personajes.map(personaje => (
            <tr key={personaje}>
              <td>{personaje}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default FormGetChacaters;
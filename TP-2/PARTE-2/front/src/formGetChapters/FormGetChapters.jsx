import React, { useState } from "react";
import './FormGetChapters.css';

import { linkApi } from '../config';
import funcFetch from '../utilities/funcFetch';

const FormGetChapters = () => {
  const [chapters, setCapitulos] = useState([]);

  const obtenerCapitulos = async () => {
    // Simulación de obtención de los capítulos (puedes reemplazar esto con tu lógica de obtención de datos)
    const capitulosObtenidos = [
      { idCapitulo: 1, nombre: "Capítulo 1", estado: "Activo" },
      { idCapitulo: 2, nombre: "Capítulo 2", estado: "Inactivo" },
      { idCapitulo: 3, nombre: "Capítulo 3", estado: "Activo" }
    ];

    const link = `${linkApi}/getChapters`


    const config = {
      method: 'GET'
    };

    const response = await funcFetch(link, config)

    alert(response.message);

    setCapitulos(response.data);
  };

  return (
    <div className="Form-GetChapters-Container">
      <h1>Formulario de Capítulos</h1>
      <button onClick={obtenerCapitulos}>Obtener Capítulos</button>
      <table>
        <thead>
          <tr>
            <th>Capitulo</th>
            <th>Nombre</th>
            <th>Estado</th>
          </tr>
        </thead>
        <tbody>
          {chapters.map(chapter => (
            <tr key={chapter.chapter}>
              <td>{chapter.chapter}</td>
              <td>{chapter.name}</td>
              <td>{chapter.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default FormGetChapters;
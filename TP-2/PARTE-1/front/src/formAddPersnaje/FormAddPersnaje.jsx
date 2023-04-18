import React, { useState } from 'react';
import './FormAddPersnaje.css';

import { linkApi } from '../config';
import funcPost from '../utilities/funcPost';
function FormAddPersnaje() {
  const [numeroCapitulo, setNumeroCapitulo] = useState('');
  const [nombrePersonaje, setNombrePersonaje] = useState('');
  const link = `${linkApi}/add/${numeroCapitulo}/${nombrePersonaje}`


  const agregarPersonaje = async () => {
    alert(`Se agregó el personaje ${nombrePersonaje} al capítulo ${numeroCapitulo}`)

    const data = {
      numberChapter: numeroCapitulo,
      character: nombrePersonaje
    };

    await funcPost(link, data);
    
    setNumeroCapitulo('');
    setNombrePersonaje('');
  };

  return (
    <form className='formAddChapter'>
      <h2>Agregar personaje</h2>
      <label className='formAddChapter-label'>
        Número del capítulo:
        <input className='formAddChapter-input' type="number" value={numeroCapitulo} onChange={e => setNumeroCapitulo(e.target.value)} />
      </label>
      <br />
      <label className='formAddChapter-label'>
        Nombre del personaje:
        <input className='formAddChapter-input' type="text" value={nombrePersonaje} onChange={e => setNombrePersonaje(e.target.value)} />
      </label>
      <br />
      <button className='button-addCharacter' type="button" onClick={agregarPersonaje}>AGREGAR</button>
    </form>
  );
}

export default FormAddPersnaje;
import React, { useState } from 'react';
import './FormDeleteCharacter.css';
import { linkApi } from '../config';
import funcPost from '../utilities/funcPost';
function FormDeleteCharacter() {
  const [numeroCapitulo, setNumeroCapitulo] = useState('');
  const [nombrePersonaje, setNombrePersonaje] = useState('');

  const link = `${linkApi}/delete/${numeroCapitulo}/${nombrePersonaje}`

  const deleteCharacter = async () => {
    const data = {
      numberChapter: numeroCapitulo,
      character: nombrePersonaje
    };

    await funcPost(link, data);

    alert(`Personaje '${nombrePersonaje}' fue eliminado al capítulo '${numeroCapitulo}'`);

    setNumeroCapitulo('');
    setNombrePersonaje('');
  };

  return (
    <form className='formDeleteCharacter'>
      <h2>Eliminar personaje</h2>
      <label className='formDeleteCharacter-label'>
        Número del capítulo:
        <input className='formDeleteCharacter-input' type="number" value={numeroCapitulo} onChange={e => setNumeroCapitulo(e.target.value)} />
      </label>
      <br />
      <label className='formDeleteCharacter-label'>
        Nombre del personaje:
        <input className='formDeleteCharacter-input' type="text" value={nombrePersonaje} onChange={e => setNombrePersonaje(e.target.value)} />
      </label>
      <br />
      <button className='button-deleteCharacter' type="button" onClick={deleteCharacter}>ELIMINAR</button>
    </form>
  );
}

export default FormDeleteCharacter;
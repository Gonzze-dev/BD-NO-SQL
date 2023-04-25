import React, { useState } from 'react';
import './FormAlqChapter.css';
import { linkApi } from '../config';
import funcFetch from '../utilities/funcFetch';

function FormAlqChapter() {
  const [numeroCapitulo, setNumeroCapitulo] = useState('');

  const link = `${linkApi}/payment/${numeroCapitulo}`

  const alqChapter = async () => {
    const config = {
      method: 'POST'
    };

    const response = await funcFetch(link, config);

    alert(response.message);

    setNumeroCapitulo('');
  };

  return (
    <form className='formAlqChapter'>
      <h2>Confirmar Pago</h2>
      <label className='formAlqChapter-label'>
        Número del capítulo:
        <input className='formAlqChapter-input' type="number" value={numeroCapitulo} onChange={e => setNumeroCapitulo(e.target.value)} />
      </label>
      <br />
      <button className='button-alqChapter' type="button" onClick={alqChapter}>Alquilar</button>
    </form>
  );
}

export default FormAlqChapter;
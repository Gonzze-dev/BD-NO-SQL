import React, { useState } from 'react';
import './FormRentChapter.css';

import { linkApi } from '../config';
import funcFetch from '../utilities/funcFetch';


function FormRentChapter() {
  const [numeroCapitulo, setNumeroCapitulo] = useState('');

  const link = `${linkApi}/rent/${numeroCapitulo}`

  const rentChapter = async () => {
    const config = {
      method: 'POST'
    };

    const response = await funcFetch(link, config)

    alert(response.message);

    setNumeroCapitulo('');
  };

  return (
    <form className='formRentChapter'>
      <h2>Rentar capitulo</h2>
      <label className='formRentChapter-label'>
        Número del capítulo:
        <input className='formRentChapter-input' type="number" value={numeroCapitulo} onChange={e => setNumeroCapitulo(e.target.value)} />
      </label>
      <br />
      <button className='button-rentChapter' type="button" onClick={rentChapter}>Rentar</button>
    </form>
  );
}

export default FormRentChapter;
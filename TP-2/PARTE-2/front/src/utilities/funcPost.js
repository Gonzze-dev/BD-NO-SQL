const funcPost = async (link, data) => {
    try {

      // Configurar las opciones para la solicitud POST
      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      };

      // Hacer la solicitud POST utilizando fetch
      const response = await fetch(link, requestOptions);

      // Manejar la respuesta exitosa
      const responseData = await response.json();
      return responseData
    } catch (error) {
      // Manejar el error
      console.error('Error:', error);
      return error
    }
  }

export default funcPost;
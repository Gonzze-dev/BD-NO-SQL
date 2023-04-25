
const funcFetch = async (link, config) => {
    try {

      const response = await fetch(link, config);
      
      // Manejar la respuesta exitosa
      const responseData = response.json();
      return responseData
    } catch (error) {
      // Manejar el error
      console.error('Error:', error);
      return error
    }
  }

export default funcFetch;
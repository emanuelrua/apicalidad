const apiUrl = 'http://127.0.0.1:8000/api/asesores/';

// Realiza la solicitud utilizando fetch
fetch(apiUrl)
  .then(response => {
    // Verifica si la solicitud fue exitosa (código de estado 200-299)
    if (!response.ok) {
      throw new Error('La solicitud no fue exitosa');
    }
    // Parsea la respuesta como JSON
    return response.json();
  })
  .then(data => {
    // Maneja los datos de la respuesta
    console.log(data);
  })
  .catch(error => {
    // Maneja errores
    console.error('Error al consumir la API:', error);
  });
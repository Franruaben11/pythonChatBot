
function enviarMensaje() {
      const input = document.getElementById('user-input');
      const chatBox = document.getElementById('chat-box');
      const mensaje = input.value;
      if (mensaje.trim() === '') return;

      chatBox.innerHTML += `<div class="mensaje usuario">${mensaje}</div>`;
      input.value = '';

      fetch("http://127.0.0.1:3000/", {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({pregunta: mensaje})
      })
          .then(res => res.json())
          .then(data => {
              console.log(data)
                    // Simula respuesta IA
            setTimeout(() => {
        //agrega un mensaje en el contenedor
        chatBox.innerHTML += `<div class="mensaje ia">${data.respuesta}</div>`;
        //el chat se desplace automáticamente hacia abajo
        chatBox.scrollTop = chatBox.scrollHeight;
      }, 500);
          });


    }


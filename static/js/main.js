function enviarMensaje() {
    const input = document.getElementById('user-input');
      const chatBox = document.getElementById('chat-box');
      const mensaje = input.value;
      if (mensaje.trim() === '') return;

      chatBox.innerHTML += `<div class="message user">${mensaje}</div>`;
      input.value = '';
      fetch("/api/chat", {
          method: 'POST',
          credentials: 'include',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({pregunta: mensaje})
      })
          .then(res => res.json())
          .then(data => {
              // Simula respuesta IA
              setTimeout(() => {
              //agrega un mensaje en el contenedor
              chatBox.innerHTML += `<div class="message bot">${data.respuesta}</div>`;
              //el chat se desplace automáticamente hacia abajo
              chatBox.scrollTop = chatBox.scrollHeight;
          }, 500);
      });
    }


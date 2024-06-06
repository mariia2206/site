document.getElementById('service-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var form = event.target;
    var formData = new FormData(form);
    var successUrl = form.getAttribute('data-success-url');

    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        },
    }).then(response => response.json())
      .then(data => {
          console.log('Response data:', data);  // Добавляем отладочную информацию
          if (data.success) {
              // Обработка успешной отправки формы
              window.location.href = successUrl;
          } else {
              // Обработка ошибок
              document.querySelectorAll('.error').forEach(function(errorDiv) {
                  errorDiv.textContent = '';
              });

              Object.keys(data.errors).forEach(field => {
                  var fieldElement = document.querySelector(`#id_${field}`);
                  if (fieldElement) {
                      var errorDiv = document.createElement('div');
                      errorDiv.classList.add('error');
                      errorDiv.textContent = data.errors[field].join(', ');
                      fieldElement.parentNode.appendChild(errorDiv);
                  }
              });

              // Перенаправление к форме с ошибками
              window.location.hash = '#booking_form';
          }
      })
      .catch(error => console.error('Error:', error));
});

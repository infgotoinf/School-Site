// const ninjaFetch = async (url) => {
//   try {
//     const response = await fetch(url);
//     if (!response.ok) {
//       throw new Error(`HTTP ошибка! Статус: ${response.status}`);
//     }
//     return await response.json(); // Достойно настоящего профессионала преобразуем JSON
//   } catch (error) {
//     console.error("Увы, возникли сложности при получении данных:", error);
//   }
// };

// // Применим получившееся мастерство ниндзя
// ninjaFetch('https://raw.githubusercontent.com/infgotoinf/School-Site/refs/heads/main/jason.json');


// const form = document.querySelector('.login-form');
// const loginInput = form.querySelector('.username');
// const passwordInput = form.querySelector('.password');

// form.addEventListener('submit', (evt) => {
//   // Отменяем действие по умолчанию
//   evt.preventDefault();
  
//   // Получаем значения полей формы
//   const login = loginInput.value;
//   const password = passwordInput.value;

//   window.location = 'https://infgotoinf.github.io/School-Site/app/Site/menu.html';

//   form.submit();
// });




async function loginFunction(event) {
  event.preventDefault();  // Предотвращаем стандартное действие формы

  // Получаем форму и собираем данные из неё
  const form = document.getElementById('login-form');
  const formData = new FormData(form);
  const data = Object.fromEntries(formData.entries());

  window.location.href = '/menu';
  
  try {
      // const response = await fetch('/auth/login', {
      //     method: 'POST',
      //     headers: {
      //         'Content-Type': 'application/json'
      //     },
      //     body: JSON.stringify(data)
      // });

      // // Проверяем успешность ответа
      // if (!response.ok) {
      //     // Получаем данные об ошибке
      //     const errorData = await response.json();
      //     displayErrors(errorData);  // Отображаем ошибки
      //     return;  // Прерываем выполнение функции
      // }

      // const result = await response.json();

      // if (result.message) {  // Проверяем наличие сообщения о успешной регистрации
      //     window.location.href = '/menu';  // Перенаправляем пользователя на страницу логина
      // } else {
      //     alert(result.message || 'Неизвестная ошибка');
      // }
      window.location.href = '/menu';
  } catch (error) {
      console.error('Ошибка:', error);
      alert('Произошла ошибка при входе. Пожалуйста, попробуйте снова.');
  }
}
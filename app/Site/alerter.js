const ninjaFetch = async (url) => {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP ошибка! Статус: ${response.status}`);
    }
    return await response.json(); // Достойно настоящего профессионала преобразуем JSON
  } catch (error) {
    console.error("Увы, возникли сложности при получении данных:", error);
  }
};

// Применим получившееся мастерство ниндзя
ninjaFetch('https://raw.githubusercontent.com/infgotoinf/School-Site/refs/heads/main/jason.json');


const form = document.querySelector('.login-form');
const loginInput = form.querySelector('.username');
const passwordInput = form.querySelector('.password');

form.addEventListener('submit', (evt) => {
  // Отменяем действие по умолчанию
  evt.preventDefault();
  
  // Получаем значения полей формы
  const login = loginInput.value;
  const password = passwordInput.value;

  window.location = 'https://www.example.com';

  form.submit();
});
// function callback() {
//   // const yo = document.querySelector('#login-form').value;
//   // alert(yo);
//   // alert( document.querySelector("#login-form").value);
//   window.location.href = '/menu';
//   };

// // const button = document.querySelector('#login-button');

// // button.addEventListener('click', callback);

function sendForm(e){
     
  // получаем значение поля key
  const log = document.form.login-form;
  const val = log.value;
  if(val.length<3){
      alert("Недопустимая длина строки");
      e.preventDefault();
  }   
  else
      alert("Отправка разрешена");
}

const sendButton = document.form.button;
sendButton.addEventListener("click", sendForm);
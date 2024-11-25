const API_USER='http://127.0.0.1:5000/users'
 
const formUser=document.querySelector("#form_user");

const corpoTabela = document.querySelector("#corpoTabela");

async function buscarUsuario(){

  // Essa é a nossa relação com a API
  const response = await fetch(API_USER);

  // Esse é o nosso json
  const users = await response.json();

 
corpoTabela.innerHTML = '';
users.array.forEach(element => {
  corpoTabela.innerHTML += `
  <th>
  <tr>
  <td>${element.id}</td>
  <td>${element.nome}</td>
  </tr>
  </th>
  `
});

} 
 
formUser.addEventListener("submit",async (e)=>{
 
    const user={
        nome:document.querySelector("#name").value
    };
 
    await fetch(API_USER,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(user)
        });
        buscarUsuario();
        formUser.reset();
} ) // esse é o final do evento de submit



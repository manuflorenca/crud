const API_USER='http://127.0.0.1:5000/users'
 
const formUser=document.querySelector("#form_user");
 
 
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
        fetchUsers();
        formUser.reset();
} ) // esse é o final do evento de submit
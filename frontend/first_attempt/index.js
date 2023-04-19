const loginForm = document.getElementById('login-form');
const logoutButton = document.getElementById('logout-btn');

let loginMessage = document.getElementById('login-message');
let loggedIn = localStorage.getItem('logged_in');
logoutButton.addEventListener('click', logout);
loginForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  
  const email = document.getElementById('email').value.toLowerCase();
  const password = document.getElementById('password').value;
  
  const response = await fetch('http://localhost:8000/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      email: email,
      password: password
    })
  });
  
  if (response.ok) {
    const data = await response.json();
    localStorage.setItem('access_token', data.access_token);
    localStorage.setItem('logged_in', true);
    const userResponse = await fetch('http://localhost:8000/user/', {
        headers: {
          'Authorization': `Bearer ${data.access_token}`
        }
      });
      const user = await userResponse.json();
      console.log(user)
      localStorage.setItem('current_user', JSON.stringify(user));
       window.location.href = 'index.html';
    // redirect the user to another page
  } else {
    const error = await response.json();
    console.log(response)
    loginMessage.textContent = error.detail[0].msg
  }

});

if (loggedIn) {
    loginForm.style.display = 'none';
    loginMessage.style.display = 'block';
    logoutButton.style.display = 'block';
    const userData = JSON.parse(localStorage.getItem('current_user'));
    loginMessage.textContent = `Login successful! ${userData.email}`;
  } else {
    loginForm.style.display = 'block';
    logoutButton.style.display = 'none';
  }

  function logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('logged_in');
    localStorage.removeItem('current_user');
    window.location.href = 'index.html';
  }
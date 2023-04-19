// Get the registration and login forms and current user div
const registerForm = document.getElementById("register-form");
const loginForm = document.getElementById("login-form");
const currentUserDiv = document.getElementById("current-user");
const loginButton = document.getElementById("login-btn");
const registerButton = document.getElementById("register-btn");

// Add event listeners for form submissions
registerForm.addEventListener("submit", registerUser);
loginForm.addEventListener("submit", loginUser);

// Function to register a new user
async function registerUser(event) {
  event.preventDefault();

  // Get the form data
  const formData = new FormData(registerForm);
  const email = formData.get("email").toLowerCase();
  const password = formData.get("password");

  // Make a POST request to the backend API endpoint
  const response = await fetch("http://localhost:8000/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  });

  // If the request was successful, display the new user's email
  if (response.ok) {
    const user = await response.json();
    currentUserDiv.textContent = `Current user: ${user.email}`;
    loginButton.style.display = "none";
    registerButton.style.display = "none";
  } else {
    alert("Error registering user");
  }
}

// Function to log in an existing user
async function loginUser(event) {
  event.preventDefault();

  // Get the form data
  const formData = new FormData(loginForm);
  const email = formData.get("email");
  const password = formData.get("password");

  // Make a POST request to the backend API endpoint
  const response = await fetch("http://localhost:8000/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  });

  // If the request was successful, display the logged in user's email
  if (response.ok) {
    const tokens = await response.json();
    localStorage.setItem("access_token", tokens.access_token);
    localStorage.setItem("refresh_token", tokens.refresh_token);
    currentUserDiv.textContent = `Current user: ${email}`;
    loginButton.style.display = "none";
    registerButton.style.display = "none";
  } else {
    alert("Error logging in user");
  }
}

// Function to get the current user's details
async function getCurrentUser() {
  // Get the access token from local storage
  const accessToken = localStorage.getItem("access_token");

  // If there is no access token, return
  if (!accessToken) {
    return;
  }

  // Make a GET request to the backend API endpoint
  const response = await fetch("http://localhost:8000/user", {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });

  // If the request was successful, display the current user's email
  if (response.ok) {
    const user = await response.json();
    currentUserDiv.textContent = `Current user: ${user.email}`;
    loginButton.style.display = "none";
    registerButton.style.display = "none";
  } else {
    // If the access token is invalid, try to refresh it
    const refreshToken = localStorage.getItem("refresh_token");
    if (refreshToken) {
      const refreshResponse = await fetch(
        "http://localhost:8000/auth/refresh",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ refresh_token: refreshToken }),
        }
      );

      if (refreshResponse.ok) {
        const tokens = await refreshResponse.json();
        localStorage.setItem("access_token", tokens.access_token);
        getCurrentUser();
      } else {
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");
      }
    } else {
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
    }
  }
}

// Function to log out the current user
function logoutUser() {
  // Remove the access and refresh tokens from local storage
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");

  // Clear the current user div
  currentUserDiv.textContent = "";

  // Show the login and register buttons again
  loginButton.style.display = "block";
  registerButton.style.display = "block";
}

// Add an event listener to the logout button
const logoutButton = document.getElementById("logout-button");
logoutButton.addEventListener("click", logoutUser);

// On page load, get the current user's details
getCurrentUser();

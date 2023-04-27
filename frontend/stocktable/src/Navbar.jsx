import { useNavigate } from "react-router-dom";
import { useAuth } from "./auth";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import { Link as MUILink } from "@mui/material";
import { Link as RouterLink } from "react-router-dom";

function Navbar() {
  const { email, isLoggedIn, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    // Remove tokens from localStorage or any other storage
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");

    // Update authentication state
    logout();

    // Redirect the user to the sign-in page
    navigate("/signin");
  };

  return (
    <AppBar position="static">
      <Toolbar>
        {isLoggedIn ? (
          <>
            <Typography variant="h6" sx={{ flexGrow: 1 }}>
              Welcome, {email}
            </Typography>
            <Button color="inherit" onClick={handleLogout}>
              Logout
            </Button>
          </>
        ) : (
          <>
            <MUILink
              component={RouterLink}
              to="/"
              color="inherit"
              sx={{ textDecoration: "none" }}
            >
              Home
            </MUILink>
            <MUILink
              component={RouterLink}
              to="/signin"
              color="inherit"
              sx={{ textDecoration: "none" }}
            >
              <Button color="inherit">Sign In</Button>
            </MUILink>
            <MUILink
              component={RouterLink}
              to="/signup"
              color="inherit"
              sx={{ textDecoration: "none" }}
            >
              <Button color="inherit">Sign Up</Button>
            </MUILink>
          </>
        )}
      </Toolbar>
    </AppBar>
  );
}

export default Navbar;

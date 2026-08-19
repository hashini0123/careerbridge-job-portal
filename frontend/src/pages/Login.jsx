import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../services/authService";
import api from "../api/api";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const data = await login(username, password);

      localStorage.setItem("accessToken", data.access);
      localStorage.setItem("refreshToken", data.refresh);

      const profileResponse = await api.get("/auth/profile/", {
        headers: {
          Authorization: `Bearer ${data.access}`,
        },
      });

      localStorage.setItem("role", profileResponse.data.role);

      alert("Login successful");

      navigate("/profile");
    } catch (error) {
      console.log("Login error:", error);
      alert("Login failed");
    }
  };

  return (
    <div>
      <h2>Login</h2>

      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(event) => setUsername(event.target.value)}
      />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(event) => setPassword(event.target.value)}
      />

      <button onClick={handleLogin}>
        Login
      </button>
    </div>
  );
}

export default Login;
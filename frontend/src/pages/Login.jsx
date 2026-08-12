import { useState } from "react";
import { login } from "../services/authService";

function Login() {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    try{
      const data = await login(username, password);

      localStorage.setItem("accesstoken", data.access);
      localStorage.setItem("refreshtoken", data.refresh);

      alert("login successful.");
    }catch(error){
      alert("login failed");
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

      <button onClick={handleLogin}>Login</button>
    </div>
  );
}

export default Login;
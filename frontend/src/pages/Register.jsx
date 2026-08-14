import { useState } from "react";
import { register } from "../services/authService";

function Register() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("JOB_SEEKER");

  const handleRegister = async () => {
    try {
      await register(username, email, password, role);
      alert("Registration successful");
    } catch (error) {
        console.log("Register error:", error.response?.data);
        alert("Registration failed");
    }
  };

  return (
    <div>
      <h2>Register</h2>

      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(event) => setUsername(event.target.value)}
      />

      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(event) => setEmail(event.target.value)}
      />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(event) => setPassword(event.target.value)}
      />

      <select
        value={role}
        onChange={(event) => setRole(event.target.value)}
      >
        <option value="JOB_SEEKER">Job Seeker</option>
        <option value="EMPLOYER">Employer</option>
      </select>

      <button onClick={handleRegister}>Register</button>
    </div>
  );
}

export default Register;
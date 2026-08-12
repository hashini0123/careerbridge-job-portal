import { useState } from "react";
import { register } from "../services/authService";

function register(){
    const [username, setUsername] = useState("");
    const [email, serEmail] = useState("");
    const [password, setPassword] = useState("");
    const [role, setRole] = useState("JOB_SEEKER");

    const handleRegister = async() => {
        try {
            await register(username, email, password, role);
            alert("Registration successful");
        }catch(error){
            alert("Registration failed");

        }
    };
}
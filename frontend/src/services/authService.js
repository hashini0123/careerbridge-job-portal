import api from "../api/api";

export const login = async (username, password) => {
  const response = await api.post("/auth/login/", {
    username,
    password,
  });

  return response.data;
};

export const register = async (username, email, password, role) => {
  const response = await api.post("/auth/register/", {
    username,
    email,
    password,
    role,
  });

  return response.data;
}
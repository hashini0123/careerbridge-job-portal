function Logout() {
  const handleLogout = () => {
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");

    alert("Logout successful");
  };

  return (
    <button onClick={handleLogout}>
      Logout
    </button>
  );
}

export default Logout;
import { useEffect, useState } from "react";
import api from "../api/api";

function Profile() {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    const getProfile = async () => {
      try {
        const token = localStorage.getItem("accessToken");

        const response = await api.get("/auth/profile/", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        setProfile(response.data);
      } catch (error) {
        console.log("Profile error:", error);
      }
    };

    getProfile();
  }, []);

  if (!profile) {
    return <p>Loading profile...</p>;
  }

  return (
    <div>
      <h2>Profile</h2>
      <p>Username: {profile.username}</p>
      <p>Email: {profile.email}</p>
      <p>Role: {profile.role}</p>
    </div>
  );
}

export default Profile;
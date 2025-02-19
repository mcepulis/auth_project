import { useEffect, useState } from "react";
import axios from "axios";

export default function Dashboard() {
  const [username, setUsername] = useState("");

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/user/", { withCredentials: true })
      .then((res) => setUsername(res.data.username))
      .catch(() => setUsername("Guest"));
  }, []);

  return <h2>Logged in as: {username}</h2>;
}

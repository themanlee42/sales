import React, { createContext, useState, useEffect, useContext } from "react";
import Cookies from "js-cookie";

export const UserContext = createContext();

const generateUniqueId = () => {
  return "uid_" + Math.random().toString(36).substr(2, 9);
};

export const UserProvider = ({ children }) => {
  const [userId, setUserId] = useState("");
  const [userEmail, setUserEmail] = useState("");
  const [loggedIn, setLoggedIn] = useState(false);

  const updateUserEmail = (email) => {
    localStorage.setItem("userEmail", email);
    setUserEmail(email);
  };

  useEffect(() => {
    let uniqueUser = Cookies.get("uniqueUser");
    if (!uniqueUser) {
      uniqueUser = generateUniqueId();
      Cookies.set("uniqueUser", uniqueUser, { expires: 7 }); // Expires in 7 days
    }
    setUserId(uniqueUser);
  }, []);

  useEffect(() => {
    // loggedIn is true if userEmail is not empty
    setLoggedIn(!!userEmail);
  }, [userEmail]);

  useEffect(() => {
    const storedEmail = localStorage.getItem("userEmail");
    if (storedEmail) {
      setUserEmail(storedEmail);
    }
  }, []);

  return (
    <UserContext.Provider
      value={{ userId, userEmail, updateUserEmail, loggedIn }}
    >
      {children}
    </UserContext.Provider>
  );
};

// custom hook
export const useUserContext = () => useContext(UserContext);

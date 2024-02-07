import React from "react";
import { Navigate } from "react-router-dom";
import { useUserContext } from "./UserContext";

const ProtectedRoute = ({ children }) => {
  const { loggedIn } = useUserContext();

  if (!loggedIn) {
    // user not logged in then redirect to login page
    // replace is needed here in the case login page is no longer needed
    return <Navigate to="/login" replace />;
  }

  return children;
};

export default ProtectedRoute;

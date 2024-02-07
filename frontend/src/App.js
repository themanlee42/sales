import React from "react";
import { Routes, Route } from "react-router-dom";
import { UserProvider } from "./UserContext"; // Import UserProvider

import Login from "./pages/Login";
import SignUp from "./pages/SignUp";
import NewProduct from "./pages/NewProduct";
import { NativeBaseProvider } from "native-base";
import "./assets/css/Common.css";
import { customTheme } from "./theme";
import ProtectedRoute from "./ProtectedRoute";
import { Helmet } from "react-helmet";

function App() {
  return (
    <>
      {" "}
      <Helmet>
        <title>Jason Lee - Sales Pitch AI</title>
        <meta
          name="description"
          content="Simple python, mongodb, react, openAI, assistants api, langchain demo project"
        />
        <meta name="keywords" content="test" />
        <meta
          name="viewport"
          content="width=device-width, initial-scale=1.0"
        ></meta>
        <meta name="author" content="Jason Lee" />
      </Helmet>
      <UserProvider>
        <NativeBaseProvider theme={customTheme}>
          <div className="App">
            <Routes>
              <Route path="/" element={<Login />} />
              <Route path="/login" element={<Login />} />
              <Route path="/signup" element={<SignUp />} />
              <Route
                path="/new-product"
                element={
                  <ProtectedRoute>
                    <NewProduct />
                  </ProtectedRoute>
                }
              />
            </Routes>
          </div>
        </NativeBaseProvider>
      </UserProvider>
    </>
  );
}

export default App;

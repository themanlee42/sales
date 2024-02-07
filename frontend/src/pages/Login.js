import React, { useState } from "react";
import { useUserContext } from "../UserContext";
import { useNavigate } from "react-router-dom";
import {
  Center,
  Box,
  Heading,
  VStack,
  FormControl,
  Input,
  Button,
  HStack,
  Text,
} from "native-base";
import { Link } from "react-router-dom";
import validator from "validator";
import { apiPost } from "../services/httpService";

const LOGIN_SUCCESS = "1";

const Login = () => {
  const { updateUserEmail } = useUserContext();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async () => {
    if (!validator.isEmail(email)) {
      alert("Please enter a valid email address.");
      return;
    }

    if (!email || !password) {
      alert("All fields are required.");
      return;
    }

    try {
      const response = await apiPost(`/login_user`, { email, password });
      if (response.success === LOGIN_SUCCESS) {
        alert("Login successful");
        // update email in context to track loggedin user
        updateUserEmail(email);
        navigate("/new-product");
      } else {
        alert("Login failed: " + response.message);
      }
    } catch (error) {
      alert("There was an error during the login process");
      console.error("There was an error during the login process", error);
    }
  };

  return (
    <Center w="100%">
      <Box safeArea p="2" py="8" w="90%" maxW="290">
        <Heading
          size="lg"
          fontWeight="600"
          color="coolGray.800"
          _dark={{ color: "warmGray.50" }}
        >
          Welcome
        </Heading>
        <Heading
          mt="1"
          _dark={{ color: "warmGray.200" }}
          color="coolGray.600"
          fontWeight="medium"
          size="xs"
        >
          Sign in to continue!
        </Heading>

        <VStack space={3} mt="5">
          <FormControl isRequired>
            <FormControl.Label>Email</FormControl.Label>
            <Input value={email} onChangeText={setEmail} />
          </FormControl>
          <FormControl isRequired>
            <FormControl.Label>Password</FormControl.Label>
            <Input
              type="password"
              value={password}
              onChangeText={setPassword}
            />
          </FormControl>
          <Button mt="2" colorScheme="indigo" onPress={handleSubmit}>
            Sign in
          </Button>
          <HStack mt="6" justifyContent="center">
            <Text
              fontSize="sm"
              color="coolGray.600"
              _dark={{ color: "warmGray.200" }}
            >
              I'm a new user.{" "}
            </Text>
            <Link
              to="/signup"
              style={{
                color: "#667EEA",
                fontWeight: "medium",
                fontSize: "16px",
              }}
            >
              Sign Up
            </Link>
          </HStack>
        </VStack>
      </Box>
    </Center>
  );
};

export default Login;

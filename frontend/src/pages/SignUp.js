import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  Center,
  Box,
  Heading,
  VStack,
  FormControl,
  Input,
  Button,
} from "native-base";
import { apiPost } from "../services/httpService";
import validator from "validator";

const SIGN_UP_SUCCESS = "1";

const SignUp = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async () => {
    if (!validator.isEmail(email)) {
      alert("Please enter a valid email address.");
      return;
    }

    if (!email || !password || !confirmPassword) {
      alert("All fields are required.");
      return;
    }

    if (password !== confirmPassword) {
      alert("Passwords do not match.");
      return;
    }

    if (password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }

    try {
      const response = await apiPost(`/create_user`, { email, password });
      console.log("-->" + response);
      if (response.success === SIGN_UP_SUCCESS) {
        alert("User Successfully Created ");
        // redirect user to the login page upon successful sign up
        navigate("/login");
      } else {
        alert("Sign up failed: " + response.message);
      }
    } catch (error) {
      alert("There was an error during the sign up process");
      console.error("There was an error during the sign up process", error);
    }
  };

  return (
    <Center w="100%">
      <Box safeArea p="2" w="90%" maxW="290" py="8">
        <Heading
          size="lg"
          color="coolGray.800"
          _dark={{
            color: "warmGray.50",
          }}
          fontWeight="semibold"
        >
          Welcome
        </Heading>
        <Heading
          mt="1"
          color="coolGray.600"
          _dark={{
            color: "warmGray.200",
          }}
          fontWeight="medium"
          size="xs"
        >
          Sign up to continue!
        </Heading>
        <VStack space={3} mt="5">
          <FormControl isRequired>
            <FormControl.Label>Email</FormControl.Label>
            <Input type="email" value={email} onChangeText={setEmail} />
          </FormControl>
          <FormControl isRequired>
            <FormControl.Label>Password</FormControl.Label>
            <Input
              type="password"
              value={password}
              onChangeText={setPassword}
            />
          </FormControl>
          <FormControl isRequired>
            <FormControl.Label>Confirm Password</FormControl.Label>
            <Input
              type="password"
              value={confirmPassword}
              onChangeText={setConfirmPassword}
            />
          </FormControl>
          <Button mt="2" colorScheme="indigo" onPress={handleSubmit}>
            Sign up
          </Button>
        </VStack>
      </Box>
    </Center>
  );
};

export default SignUp;

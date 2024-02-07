import React, { useState } from "react";
import {
  TextArea,
  Center,
  Heading,
  Container,
  Button,
  Stack,
} from "native-base";
import { apiPost } from "../services/httpService";

const NewProduct = () => {
  const [requestText, setRequestText] = useState("");
  const [responseText, setResponseText] = useState("");

  const handleSubmit = async () => {
    // clear the previous response text
    setResponseText("");
    // convert new lines to JSON readable format
    const input = requestText.replace(/\n/g, "\\n");

    // for now Work-around before JWT mechanism
    // in a real world programming - NEVER pass the email
    const userEmail = "mockUserId";

    try {
      const response = await apiPost(`/submit_question`, { input, userEmail });
      if (response && response.message) {
        setRequestText("");
        setResponseText(response.message);
        console.log("API Response:", response.output);
      }
    } catch (error) {
      console.error(
        "There was an error submitting the product description",
        error
      );
    }
  };

  const handleClearRequestText = () => {
    // clear the request textArea
    setRequestText("");
  };

  return (
    <Center flex={1}>
      <Container>
        <Heading color="emerald.400">AI SALES PITCH HELPER</Heading>
        <TextArea
          shadow={2}
          h={40}
          placeholder="Enter your product description here"
          value={requestText}
          onChangeText={setRequestText}
          w="400"
          _light={{
            placeholderTextColor: "trueGray.700",
            bg: "coolGray.100",
            _hover: {
              bg: "coolGray.200",
            },
            _focus: {
              bg: "coolGray.200:alpha.70",
            },
          }}
          _dark={{
            bg: "coolGray.800",
            _hover: {
              bg: "coolGray.900",
            },
            _focus: {
              bg: "coolGray.900:alpha.70",
            },
          }}
        />
        <Stack
          direction={{ base: "column", md: "row" }}
          space={2}
          mx={{ base: "auto", md: 0 }}
        >
          <Button size="sm" mt="2" onPress={handleSubmit}>
            SUBMIT
          </Button>
          <Button
            colorScheme="secondary"
            size="sm"
            mt="2"
            onPress={handleClearRequestText}
          >
            CLEAR
          </Button>
        </Stack>
        <TextArea
          shadow={2}
          h={80}
          mt="2"
          placeholder="Please wait for your response"
          value={responseText}
          isReadOnly
          w="400"
          _light={{
            placeholderTextColor: "trueGray.700",
            bg: "coolGray.100",
            _hover: {
              bg: "coolGray.200",
            },
            _focus: {
              bg: "coolGray.200:alpha.70",
            },
          }}
          _dark={{
            bg: "coolGray.800",
            _hover: {
              bg: "coolGray.900",
            },
            _focus: {
              bg: "coolGray.900:alpha.70",
            },
          }}
        />
      </Container>
    </Center>
  );
};

export default NewProduct;

import Constants from "./../Const";
import axios from "axios";

const axiosInstance = axios.create({
  baseURL: Constants.API_URL,
});

export const apiPost = async (url, data) => {
  try {
    const response = await axiosInstance.post(url, data);
    console.log("Server response:", response);
    return response.data;
  } catch (error) {
    console.error("There was an error sending the request", error);
    throw error;
  }
};

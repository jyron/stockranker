import axios from "axios";

export async function likeStock(stockId, action) {
  const accessToken = localStorage.getItem("access_token");
  try {
    const response = await axios.post(
      `http://localhost:8080/stocks/${stockId}/like/${action}`,
      {},
      {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      }
    );
    return response.data;
  } catch (error) {
    console.error("Error details:", error.response.data); // Log the error details
    throw new Error("Failed to like/dislike stock");
  }
}

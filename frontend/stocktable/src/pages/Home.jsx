import React from "react";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import StockPage from "../components/StockPage";

function Home() {
  return (
    <Box>
      <Typography variant="h1">StockRanker.co</Typography>
      <Typography variant="body1">Welcome to our homepage!</Typography>
      <StockPage />
    </Box>
  );
}

export default Home;

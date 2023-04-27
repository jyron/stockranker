import React, { useState, useEffect } from "react";
import axios from "axios";
import StockTable from "./StockTable";

const StockPage = () => {
  const [stocks, setStocks] = useState([]);

  useEffect(() => {
    const fetchStocks = async () => {
      try {
        const response = await axios.get("http://localhost:8080/stocks");
        setStocks(response.data.data);
      } catch (error) {
        console.error("Error fetching stocks:", error);
      }
    };

    fetchStocks();
  }, []);

  return (
    <div>
      <h1>Stocks</h1>
      {stocks.length > 0 ? (
        <StockTable stocks={stocks} />
      ) : (
        <p>Loading stocks...</p>
      )}
    </div>
  );
};

export default StockPage;

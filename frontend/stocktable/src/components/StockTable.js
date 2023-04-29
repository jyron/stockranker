import React, { useState, useMemo } from "react";
import { useTable } from "react-table";
import { likeStock } from "../utilities/like";

const StockTable = ({ stocks }) => {
  const [loading, setLoading] = useState(false);
  const columns = useMemo(
    () => [
      {
        Header: "Ticker",
        accessor: "ticker",
      },
      {
        Header: "Name",
        accessor: "name",
      },
      {
        Header: "Likes",
        accessor: "likes",
      },
      {
        Header: "Actions",
        id: "actions",
        Cell: ({ row }) => (
          <button
            disabled={loading}
            onClick={() => handleLike(row.original._id, "like")}
          >
            Like
          </button>
        ),
      },
      {
        Header: "Comments",
        accessor: "comments",
        Cell: ({ row }) => (
          <div>
            {row.original.comments.map((comment, index) => (
              <p key={index}>{comment}</p>
            ))}
            <form onSubmit={(e) => handleComment(e, row.original)}>
              <input
                type="text"
                placeholder="Add a comment"
                name={`comment-${row.original.ticker}`}
              />
              <button type="submit">Submit</button>
            </form>
          </div>
        ),
      },
    ],
    [loading]
  );

  const { getTableProps, getTableBodyProps, headerGroups, rows, prepareRow } =
    useTable({ columns, data: stocks });

  const handleLike = async (stockId, action) => {
    // Implement the like functionality here
    setLoading(true);
    try {
      await likeStock(stockId, action);
    } catch (error) {
      console.error("Error Liking stock:", error);
    } finally {
      setLoading(false);
    }
    console.log("Liked stock:", stockId);
  };

  const handleComment = (e, stock) => {
    e.preventDefault();
    const comment = e.target[`comment-${stock.ticker}`].value;
    // Implement the comment functionality here
    console.log(`Comment for stock ${stock.ticker}: ${comment}`);
  };

  return (
    <table {...getTableProps()} style={{ border: "solid 1px black" }}>
      <thead>
        {headerGroups.map((headerGroup) => (
          <tr {...headerGroup.getHeaderGroupProps()}>
            {headerGroup.headers.map((column) => (
              <th
                {...column.getHeaderProps()}
                style={{
                  borderBottom: "solid 3px black",
                  background: "aliceblue",
                  color: "black",
                  fontWeight: "bold",
                }}
              >
                {column.render("Header")}
              </th>
            ))}
          </tr>
        ))}
      </thead>
      <tbody {...getTableBodyProps()}>
        {rows.map((row) => {
          prepareRow(row);
          return (
            <tr {...row.getRowProps()}>
              {row.cells.map((cell) => {
                return (
                  <td
                    {...cell.getCellProps()}
                    style={{
                      padding: "10px",
                      border: "solid 1px gray",
                      background: "papayawhip",
                    }}
                  >
                    {cell.render("Cell")}
                  </td>
                );
              })}
            </tr>
          );
        })}
      </tbody>
    </table>
  );
};

export default StockTable;

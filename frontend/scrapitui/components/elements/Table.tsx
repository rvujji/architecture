import React, { useEffect, useState } from "react";

// Define the type for a table column
type TableColumn = {
  header: string; // Header text for the column
  field: string; // Field name in the data corresponding to the column
};

// Define the type for the props
type TableProps = {
  name: string; // Name or id of the table
  columns: TableColumn[]; // Array of column definitions
  data: string | object[]; // Data as an array of objects or a URL for fetching
};

const Table: React.FC<TableProps> = ({ name, columns, data }) => {
  const [tableData, setTableData] = useState<object[]>([]);

  // Fetch data if `data` is a URL; otherwise, assume it's passed as an array
  useEffect(() => {
    if (typeof data === "string") {
      fetch(data)
        .then((response) => response.json())
        .then((jsonData) => setTableData(jsonData))
        .catch((error) => console.error("Error fetching table data:", error));
    } else if (Array.isArray(data)) {
      setTableData(data);
    }
  }, [data]);

  return (
    <div className="table-container">
      <table
        id={name}
        className="table"
        style={{ borderCollapse: "collapse", width: "100%" }}
      >
        <thead>
          <tr>
            {columns.map((col, index) => (
              <th
                key={index}
                style={{ border: "1px solid #ddd", padding: "8px" }}
              >
                {col.header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {tableData.length > 0 ? (
            tableData.map((row, rowIndex) => (
              <tr key={rowIndex}>
                {columns.map((col, colIndex) => (
                  <td
                    key={colIndex}
                    style={{ border: "1px solid #ddd", padding: "8px" }}
                  >
                    {row[col.field as keyof typeof row] ?? "N/A"}
                  </td>
                ))}
              </tr>
            ))
          ) : (
            <tr>
              <td
                colSpan={columns.length}
                style={{ textAlign: "center", padding: "8px" }}
              >
                No data available
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default Table;

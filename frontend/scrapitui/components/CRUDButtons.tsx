import React from "react";

type CRUDButtonsProps = {
  onModeChange: (mode: "create" | "read" | "update" | "delete") => void;
};

const CRUDButtons: React.FC<CRUDButtonsProps> = ({ onModeChange }) => (
  <div className="crud-buttons">
    <button onClick={() => onModeChange("create")}>Create</button>
    <button onClick={() => onModeChange("read")}>Read</button>
    <button onClick={() => onModeChange("update")}>Update</button>
    <button onClick={() => onModeChange("delete")}>Delete</button>
  </div>
);

export default CRUDButtons;

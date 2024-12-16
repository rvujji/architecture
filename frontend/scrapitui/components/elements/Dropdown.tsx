import React from "react";

type Option = {
  label: string; // Display text for the dropdown option
  value: string; // Value associated with the option
};

// Define the type for the props
type DropdownProps = {
  label: string; // Label for the dropdown
  name: string; // Name and id for the dropdown
  options: Option[]; // Array of options for the dropdown
  value: string; // Currently selected value
  onChange: (event: React.ChangeEvent<HTMLSelectElement>) => void; // Change handler
};

const Dropdown: React.FC<DropdownProps> = ({
  label,
  name,
  options,
  value,
  onChange,
}) => {
  return (
    <div className="form-control">
      <label htmlFor={name}>{label}</label>
      <select
        id={name}
        name={name}
        value={value}
        onChange={onChange}
        style={{
          padding: "8px",
          borderRadius: "4px",
          border: "1px solid #ccc",
        }}
      >
        {options.map((option, index) => (
          <option key={index} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
    </div>
  );
};

export default Dropdown;

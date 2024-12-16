import React from "react";

// Define the type for validation rules
type ValidationRules = {
  required?: boolean; // Whether the field is required
  maxLength?: number; // Maximum length of the input
  errorMessage?: string; // Custom error message
};

type TextboxProps = {
  label: string;
  name: string;
  value: string; // Value of the input field
  placeholder: string;
  validation?: ValidationRules;
  onChange: (event: React.ChangeEvent<HTMLInputElement>) => void; // Change handler
};

const Textbox: React.FC<TextboxProps> = ({
  label,
  name,
  value,
  placeholder,
  validation = {},
  onChange,
}) => {
  const { required = false, maxLength, errorMessage } = validation;

  // State to manage validation error
  const [error, setError] = React.useState<string | null>(null);

  const validateInput = (value: string) => {
    if (required && value.trim() === "") {
      setError(errorMessage || "This field is required.");
    } else if (maxLength && value.length > maxLength) {
      setError(`Maximum length is ${maxLength} characters.`);
    } else {
      setError(null);
    }
  };

  const handleBlur = () => {
    validateInput(value);
  };

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setError(null); // Clear error on input change
    onChange(event);
  };

  return (
    <div className="form-control">
      <label htmlFor={name}>{label}</label>
      <input
        type="text"
        id={name}
        name={name}
        value={value}
        placeholder={placeholder}
        maxLength={maxLength}
        required={required}
        onChange={handleChange}
        onBlur={handleBlur}
        style={{
          padding: "8px",
          borderRadius: "4px",
          border: "1px solid #ccc",
        }}
      />
      {error && (
        <span style={{ color: "red", fontSize: "0.8rem" }}>{error}</span>
      )}
    </div>
  );
};
export default Textbox;

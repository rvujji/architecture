import { useState } from "react";

const useCRUD = () => {
  const [mode, setMode] = useState("read");
  return [mode, setMode];
};

export default useCRUD;

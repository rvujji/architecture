import { componentRegistry } from "@/components/registry/ComponentRegistry";
import config from "@/config/config.json";

const DynamicPage: React.FC = ({ config }) => {
  return (
    <div className={`layout-${config.layout}`}>
      <h1>{config.pageTitle}</h1>
      {config.components.map((component, index) => {
        const Component = componentRegistry[component.type];
        return Component ? <Component key={index} {...component} /> : null;
      })}
    </div>
  );
};

export default DynamicPage;

<Textbox
  label="Name"
  name="username"
  value={username}
  onChange={(e) => setUsername(e.target.value)}
/>;

<Dropdown
  label="Select Country"
  name="country"
  options={[
    { label: "India", value: "IN" },
    { label: "USA", value: "US" },
    { label: "Canada", value: "CA" },
  ]}
  value={country}
  onChange={(e) => setCountry(e.target.value)}
/>;

<Table
  name="userTable"
  columns={[
    { header: "ID", field: "id" },
    { header: "Name", field: "name" },
    { header: "Email", field: "email" },
  ]}
  data="https://jsonplaceholder.typicode.com/users"
/>;

import React from "react";
import Video from "./Video";

const App: React.FC = () => {
  return (
    <div>
      <h1>Video Example</h1>
      <Video src="https://www.w3schools.com/html/mov_bbb.mp4" controls={true} />
    </div>
  );
};

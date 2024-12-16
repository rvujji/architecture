import React from "react";
import { componentRegistry } from "@/components/registry/ComponentRegistry";
import { TextboxProps } from "@/components/elements/Textbox";
import { DropdownProps } from "@/components/elements/Dropdown";
import { VideoProps } from "@/components/elements/Video";
import { TableProps } from "@/components/elements/Table";

type ComponentConfig = {
  type: keyof typeof componentRegistry; // The type of the component (e.g., "Textbox", "Dropdown")
  props: TextboxProps | DropdownProps | VideoProps | TableProps; // The props to be passed to the component
};

export type Config = {
  pageTitle: string; // Title of the page
  layout: "vertical" | "horizontal"; // Layout type
  components: ComponentConfig[]; // List of components
};

const DynamicPage: React.FC<{ config: Config }> = ({ config }) => {
  return (
    <div className={`layout-${config.layout}`}>
      <h1>{config.pageTitle}</h1>
      {config.components.map((component, index) => {
        const Component = componentRegistry[component.type];
        return (
          //@ts-ignore
          <Component key={index} {...component.props} />
        );
      })}
    </div>
  );
};

export default DynamicPage;

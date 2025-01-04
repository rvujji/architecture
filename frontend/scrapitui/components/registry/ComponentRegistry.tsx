import Textbox, { TextboxProps } from "@/components/elements/Textbox";
import Dropdown, { DropdownProps } from "@/components/elements/Dropdown";
import Video, { VideoProps } from "@/components/elements/Video";
import Table, { TableProps } from "@/components/elements/Table";

export const componentRegistry: {
  Textbox: React.FC<TextboxProps>;
  Dropdown: React.FC<DropdownProps>;
  Video: React.FC<VideoProps>;
  Table: React.FC<TableProps>;
} = {
  Textbox,
  Dropdown,
  Video,
  Table,
};

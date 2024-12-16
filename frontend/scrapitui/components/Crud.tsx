
const data = {
  screen: {
    screen_id: 1,
    org_id: 1,
    project_id: 1,
    name: "List Seller Items",
    layout: {
      rows: 5,
      columns: 4,
      row_spans: [{ "2": 3 }, { "4": 5 }, { "3": 4 }],
      col_spans: [{ "1": 2 }],
    },
    fields: [
      {
        label_name: "seller name",
        row_no: 1,
        column_no: 1,
        content_type: "INPUT",
        content: {
          input_type: "TEXT",
          collection_field: "owner_details.name",
          collection: "items",
        },
      },
      {
        label_name: "seller graph",
        row_no: 1,
        column_no: 2,
        content_type: "GRAPH",
        content: {
          api_json: "selling_frequency",
        },
      },
    ],
  },
};

const Crud = () => {
  return (
    <div>
      <h1>Crud Component</h1>
    </div>
  );
};

export default Crud;

import { Text, View } from "react-native";
import Crud from "@/components/Crud";

export default function Index() {
  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Text>Edit app/index.tsx to edit this screen.</Text>
      <Crud />
    </View>
  );
}

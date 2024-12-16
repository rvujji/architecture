import { Text, View } from "react-native";
import Crud from "@/components/Crud";
import DynamicPage from "@/components/DynamicPage";
import configData from "@/config/pageConfig.json";
import { Config } from "@/components/DynamicPage";

export default function Index() {
  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <DynamicPage config={configData as Config} />;
    </View>
  );
}

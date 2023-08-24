import React from "react";
import { createRoot } from "react-dom/client";
import TestProvider from "tests/TestProvider";
import CodeEditor from "./CodeEditor";

it("renders without crashing", () => {
  const div = document.createElement("div");
  const root = createRoot(div);
  root.render(
    <TestProvider>
      <CodeEditor />
    </TestProvider>
  );
  root.unmount();
});
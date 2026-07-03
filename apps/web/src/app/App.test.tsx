import { expect, test } from "vitest";

import { App } from "@/app/App";

test("App is defined", () => {
  expect(App).toBeTypeOf("function");
});

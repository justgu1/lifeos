// Codegen: packages/shared/schema/*  ->  packages/shared/py/generated + ts/generated
//
// Scaffold only. The real pipeline (JSON Schema -> pydantic + zod/TS types) is
// implemented in SHARED-001. This placeholder documents the contract and exits 0
// so the CI wiring is exercised on the empty scaffold.

console.log("[codegen] scaffold: schema -> pydantic (py) + zod/types (ts)");
console.log("[codegen] implement in SHARED-001; no files generated yet.");
process.exit(0);

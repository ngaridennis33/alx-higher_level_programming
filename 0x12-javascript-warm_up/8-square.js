#!/usr/bin/node

let result = parseInt(process.argv[2]);
if (!isNaN(result)) {
  for (let i = 0; i < result; i++) {
    console.log("X".repeat(result));
  }
} else {
  console.log("Missing size");
}

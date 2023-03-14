#!/usr/bin/node

let txt = "C is fun";
let result = parseInt(process.argv[2]);
if (!isNaN(result)) {
  for (let i = 0; i < result; i++) {
    console.log(txt);
  }
} else {
  console.log("Input missing or NaN");
}

#!/usr/bin/node

function print(args, ...rest) {
  if (args === undefined) {
    console.log("No argument");
  } else if (rest.length === 0) {
    console.log("Argument found");
  } else if (rest.length > 0) {
    console.log("Arguments found");
  }
}

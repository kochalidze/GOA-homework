function count_area(...args) {
    const numArgs = args.length;
  
    if (numArgs === 2) {
      // Rectangle: requires 2 inputs (length, width)
      const [length, width] = args;
      return length * width;
    } else if (numArgs === 1) {
      // Circle: requires 1 input (radius)
      const radius = args[0];
      return Math.PI * radius ** 2;
    } else if (numArgs === 3) {
      // Triangle: requires 3 inputs (sides a, b, c)
      const [a, b, c] = args;
      const s = (a + b + c) / 2; // Semi-perimeter
      const area = Math.sqrt(s * (s - a) * (s - b) * (s - c)); // Heron's formula
      return area;
    } else {
      throw new Error("Invalid number of arguments. Provide 1, 2, or 3 arguments.");
    }
  }
  
  // მაგალითები:
  console.log(count_area(5, 10));  // Rectangle: 50
  console.log(count_area(7));      // Circle: 153.93804002589985
  console.log(count_area(3, 4, 5)); // Triangle: 6.0
  
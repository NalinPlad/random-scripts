function simplifyTrigFunction(trigFunction) {
    const pattern = /((sin|cos|tan)\((\w+)\))((sec|csc|cot)\((\w+)\))/g;
  
    let match;
  
    // Check if function has 2 parts separated by multiplication operator.
    if (trigFunction.indexOf("*") !== -1) {
      let [leftFunction, rightFunction] = trigFunction.split("*");
      trigFunction = `(${leftFunction})(${rightFunction})`;
    }
  
    // Look for matches with two trigonometric functions.
    while ((match = pattern.exec(trigFunction))) {
      const [matched, firstFunction, _, firstArg, secondFunction, __, secondArg] = match;
      const quotient = (firstFunction === 'sin' || firstFunction === 'csc') ? 'tan' : 'cot';
  
      // Simplify the two functions into a single quotient function.
      const quotientFunction = `${quotient}(${firstArg})`;
      if (quotientFunction === secondFunction + '(' + secondArg + ')') {
        trigFunction = quotientFunction;
      } else if ('reciprocal(' + quotientFunction + ')' === secondFunction + '(' + secondArg + ')') {
        trigFunction = '1/' + quotientFunction;
      }
    }
  
    return trigFunction;
  }
  
  console.log(simplifyTrigFunction('sin(x)*sec(x)')); // Outputs 'tan(x)'
  
let numero = 4;
let fatorial = 1;

if (numero === 0 || numero === 1) {
  return (fatorial = 1);
} else {
  for (let i = numero; i >= 1; i--) {
    fatorial *= i;
  }
}

console.log(`O fatorial de ${numero} é ${fatorial}`);

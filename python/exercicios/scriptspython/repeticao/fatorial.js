function fatorial(numeroDeEntrada) {
  let soma = 1;
  if (numeroDeEntrada <= 0 || numeroDeEntrada == 1) {
    return console.log("Insira um numero positivo ou maior que 1");
  } else {
    while (numeroDeEntrada >= 1) {
      soma *= numeroDeEntrada;
      numeroDeEntrada -= 1;
    }
  }
  return soma;
}

let numeroDeEntrada = 4;
let resultado = fatorial(numeroDeEntrada);

console.log(`O fatorial de ${numeroDeEntrada} é ${resultado}`);

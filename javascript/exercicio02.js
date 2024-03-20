//receber 10 numeros
//pecorrer cada numero
//somar o valor atual com o anterior
//acrescentar mais um no contador
//mostrar o menor valor dentro da lista
//mostrar o maior valor dentro da lista
//somar tudo e dividir por 10

let listaComDezNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let totalDeNumeros = 10;
let contador = 0;
let somaDosNumeros = 0;
let mediaDosNumeros = 0;
let maiorNumero = 0;
let menorNumero = Infinity8;
// while (listaComDezNumeros.length <= 10) {
//   if (listaComDezNumeros <= 10) {
//   }
//   console.log(listaComDezNumeros);
// }

for (let numero of listaComDezNumeros) {
  somaDosNumeros += numero;
  if (numero > maiorNumero) {
    maiorNumero = numero;
  }

  //   if (maiorNumero > numero) {
  //     console.log("true");
  //     menorNumero = 1;
  //   }
}
mediaDosNumeros = somaDosNumeros / listaComDezNumeros.length;

for (let i = 0; i < listaComDezNumeros.length; i++) {
  if (listaComDezNumeros[i] < menorNumero) {
    menorNumero = listaComDezNumeros[i];
  }
}

console.log("a media dos numeros é :", mediaDosNumeros);
console.log("maior numero:", maiorNumero);
console.log("menor numero:", menorNumero);

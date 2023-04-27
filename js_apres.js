// ECMAScript and JavaScript: a ECMA (acrônimo de European Computers Manufactors Association) foi fundada em 1961. É uma associação dedicada à padronização de sistemas 
// de informação. As padronizações envolvem o formato de encriptar dados (para que todo computador possa desincriptar), o método utilizado para isso; a forma como um 
// sistema operacional orquestra os componentes eletrônicos do computador. A razão para o Java (consequentemente o JS) fazer tanto sucesso é porque, naquela época,
// anterior ao ECMA, os códigos e programas tinham que ser adaptado para cada sistema operacional existente; porém, códigos em Java tinham uma adaptação automática.
// Conforme os apps web foram aumentando, bem como os browsers disponíveis (cada um com seu script), era necessário uma padronização. Em 1996 foi enviado ao ECMA
// o JavaScript para que ele fosse utilizado como programa padrão no desenvolvimento web. Seu nome alterou-se para ECMAScript, porém, devido ao sucesso que ele
// já tinha, continuou o nome usual.

// Hoisting e Use strict
function teste11(){
    console.log('oi');
}
function teste12(){
    mensagem = 'oi2';
    console.log(mensagem);
    console.log('----');
}
function teste13(){
    mensagem = 'oi3';
    console.log(mensagem);
    console.log('----');
    let mensagem;
}
function teste14(){
    'use strict';
    mensagem = 'oi4';
    console.log(mensagem);
    console.log('----');
}

// Default parameters
function teste21(x, y){
    if (typeof y == undefined){
        y = 0;
    }
    console.log(x + y);
}
function teste22(x, y){
    y = y || 0;
    console.log(x + y);
}
function teste23(x, y=0){
    console.log(x + y);
}

// Template strings
function teste3(text){
    console.log(text + ' foi o paramêtro recebido');
    console.log(`--- ${text} foi o paramêtro recebido`);
}


// Destructuring & for, forEach and for... of
function teste4(x){
    const [a, b, c] = x;
    console.log('first way:');
    for (let i = 0; i < x.length;i++){
        console.log(x[i]);
    }
    console.log('second way:');
    x.forEach((element, index) => console.log(element));
    console.log('third way:');
    for (const element of x){
        console.log(element);
    }
}
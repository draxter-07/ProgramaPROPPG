// ECMAScript and JavaScript: a ECMA (acrônimo de European Computers Manufactors Association) foi fundada em 1961. É uma associação dedicada à padronização de sistemas 
// de informação. As padronizações envolvem o formato de encriptar dados (para que todo computador possa desincriptar), o método utilizado para isso; a forma como um 
// sistema operacional orquestra os componentes eletrônicos do computador. A razão para o Java (consequentemente o JS) fazer tanto sucesso é porque, naquela época,
// anterior ao ECMA, os códigos e programas tinham que ser adaptado para cada sistema operacional existente; porém, códigos em Java tinham uma adaptação automática.
// Conforme os apps web foram aumentando, bem como os browsers disponíveis (cada um com seu script), era necessário uma padronização. Em 1996 foi enviado ao ECMA
// o JavaScript para que ele fosse utilizado como programa padrão no desenvolvimento web. Seu nome alterou-se para ECMAScript, porém, devido ao sucesso que ele
// já tinha, continuou o nome usual.

// como uma linguagem humana, o seu desenvolvimento se dá pelo aumento da praticidade

// Hoisting e Use strict (sujeito oculto & linguagem formal)
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

// Uma linguagem pode chegar ao fim?
// LiveScript VS JavaScript
function LS(){
//    table1 =
//  * id: 1
//    name: 'george'
//  * id: 2
//    name: 'mike'
//  * id: 3
//    name: 'donald'
//    table2 =
// * id: 2
//    age: 21
//  * id: 1
//    age: 20
//  * id: 3
//   age: 26
//    up-case-name = (.name .= to-upper-case!)
//    [{id:id1, name, age} for {id:id1, name} in table1
//                     for {id:id2, age} in table2
//                     when id1 is id2]
//    sort-by (.id)
//    map (.age), table2 |> fold1 (+)
}
function JS(){
    var table1, table2, upCaseName, id1, name, id2, age;
    table1 = [
        {
            id: 1,
            name: 'george'
        }, {
            id: 2,
            name: 'mike'
        }, {
            id: 3,
            name: 'donald'
        }
    ];
    table2 = [
        {
            id: 2,
            age: 21
        }, {
            id: 1,
            age: 20
        }, {
            id: 3,
            age: 26
        }
    ];
    upCaseName = function(it){
        return it.name = it.name.toUpperCase();
    };
    JSON.stringify(
        each(upCaseName)(
            sortBy(function(it){
                return it.id;
            })(
            (function(){
                var i$, ref$, len$, ref1$, j$, len1$, ref2$, results$ = [];
                for (i$ = 0, len$ = (ref$ = table1).length; i$ < len$; ++i$) {
                    ref1$ = ref$[i$], id1 = ref1$.id, name = ref1$.name;
                    for (j$ = 0, len1$ = (ref1$ = table2).length; j$ < len1$; ++j$) {
                        ref2$ = ref1$[j$], id2 = ref2$.id, age = ref2$.age;
                        if (id1 === id2) {
                            results$.push({
                                id: id1,        
                                name: name,    
                                age: age      
                            });
                        }   
                    }
                }
                return results$;
            }()))));
            fold1(curry$(function(x$, y$){
                return x$ + y$;
            }))(
                map(function(it){
                    return it.age;
                }, table2));
                function curry$(f, bound){
                    var context,
                    _curry = function(args) {
                        return f.length > 1 ? function(){
                            var params = args ? args.concat() : [];
                            context = bound ? context || this : this;
                            return params.push.apply(params, arguments) <
                            f.length && arguments.length ?
                            _curry.call(context, params) : f.apply(context, params);
                        } : f;
                    };
                    return _curry();
                }
}

// CoffeeScript VS JavaScript
function CS(){
//    number   = 42
//    opposite = true
//    number = -42 
//    if opposite
//   square = (x) -> x * x
//    list = [1, 2, 3, 4, 5]
//    math =
//    root:   Math.sqrt
//    square: square
//    cube:   (x) -> x * square x
//    race = (winner, runners...) ->
//    print winner, runners
//    alert "I knew it!" if elvis?
//    cubes = (math.cube num for num in list)
}
function JSCS(){
    var cubes, list, math, num, number, opposite, race, square;
    number = 42;
    opposite = true;
    if (opposite) {
        number = -42;
    }
    square = function(x) {
        return x * x;
    };
    list = [1, 2, 3, 4, 5];
    math = {
        root: Math.sqrt,
        square: square,
        cube: function(x) {
            return x * square(x);
        }
    };
    race = function(winner, ...runners) {
        return print(winner, runners);
    };
    if (typeof elvis !== "undefined" && elvis !== null) {
        alert("I knew it!");
    }
    cubes = (function() {
        var i, len, results;
        results = [];
        for (i = 0, len = list.length; i < len; i++) {
            num = list[i];
            results.push(math.cube(num));
        }
        return results;
    })();
}

// Python and JavaScript
// https://livingwithcode.com/can-python-replace-javascript/#:~:text=Your%20browser's%20rendering%20engine%20needs,other%20programming%20languages%20including%20Python.
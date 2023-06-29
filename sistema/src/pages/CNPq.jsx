import styled from 'styled-components'
import { useState } from 'react'
import Topo from './comps/Topo.jsx'

export default function PesqLaboratorio(){
    const yellowcolorUTFPR = 'rgb(250, 200, 0, 0.9)';
    const [pare, setPare] = useState([[null, null, null]]);
    const Screen = styled.div`
        box-sizing: border-box;
        width: 100vw;
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 50px 0px 0px;
    `
    const Pesquisa = styled.div`
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: auto;
        height: auto;
        input{
            box-sizing: border-box;
            margin: 0px 0px 5px;
            border-radius: 5px;
            border: 1px solid rgb(0, 0, 0);
            width: 200px;
            padding: 5px;
        }
    `
    const Resultados = styled.div`
        box-sizing: border-box;
        width: 50%;
        height: auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 20px 0px 0px;
        div{
            display: flex;
            flex-direction: row;
        }
    `
    function cnpqcar(e){
        let pares = [];
        let trLines = [];
        let trfLines = [];
        let conj = e.target.parentElement.children[0].value;
        // Divisão dos <tr e </tr
        for (let a = 0; a < conj.length - 2; a++){
            if (conj[a] + conj[a+1] + conj[a+2] == '<tr'){
                trLines.push(a);
            }
            else if (conj[a] + conj[a+1] + conj[a+2] + conj[a+3] == '</tr'){
                trfLines.push(a);
            }
        }
        // Trabalha no espaçõ entre o <tr e </tr
        for (let a = 0; a < trLines.length; a++){
            const comecoLine = trLines[a];
            const fimLine = trfLines[a];
            let dados = [];
            // Analisa o intervalo
            for (let b = comecoLine; b < fimLine + 1; b++){
                // Pega o nome se encontrar Title
                if (conj[b] + conj[b + 1] + conj[b + 2] + conj[b + 3] + conj[b + 4] == 'title'){
                    let comecoNome = 0;
                    let fimNome = 0;
                    let nome = "";
                    for (let c = b; c < fimLine; c++){
                        if (comecoNome == 0){
                            if (conj[c] == '"'){
                                comecoNome = c + 1;
                            }
                        }
                        else if (comecoNome != 0 && fimNome == 0){
                            if (conj[c] == '"'){
                                fimNome = c;
                                break;
                            }
                        }
                    }
                    for (let d = comecoNome; d < fimNome; d++){
                        nome = nome + conj[d];
                    }
                    nome = nome.replaceAll('Ã§', 'ç').replaceAll('Ã£', 'ã').replaceAll('Ã¡', 'á').replaceAll('Ã', 'í').replaceAll('í©', 'é').replaceAll('í¡', 'á').replaceAll('í£', 'ã').replaceAll('í´', 'ô').replaceAll('íª', 'ê').replaceAll('í³', 'ó').replaceAll('í¢', 'â').replaceAll('íº', 'ú')
                    nome = nome.replaceAll('ç', 'c').replaceAll('í', 'i').replaceAll('é', 'e').replaceAll('á', 'a').replaceAll('ã', 'a').replaceAll('ô', 'o').replaceAll('ê', 'e').replaceAll('ó', 'o').replaceAll('â', 'a').replaceAll('ú', 'u')
                    dados.push(nome);
                }
            }
            if (dados.length == 3){
                pares.push(dados);
            }
            else{
                // Pegar nome na segunda <td
                let found = 0;
                for (let e = comecoLine; e < fimLine + 1; e++){
                    if (conj[e] + conj[e + 1] + conj[e + 2] == '<td'){
                        found = found + 1;
                    }
                    if (found == 2){
                        let comecoLinetd = e;
                        let fimLinetd = 0;
                        for (let f = e; f < fimLine; f++){
                            if (conj[f] + conj[f + 1] + conj[f + 2] + conj[f + 3] == '</td'){
                                fimLinetd = f;
                                break;
                            }
                        }
                        let comecoNome = 0;
                        let fimNome = 0;
                        for (let g = comecoLinetd  +2; g < fimLinetd; g++){
                            if (conj[g] == '>' && comecoNome == 0){
                                comecoNome = g;
                            }
                            else if (conj[g] == '<' && fimNome == 0){
                                fimNome = g;
                                break;
                            }
                        }
                        let name = "";
                        for (let h = comecoNome + 1; h < fimNome; h++){
                            name = name + conj[h];
                        }
                        name = name.replaceAll('Ã§', 'ç').replaceAll('Ã£', 'ã').replaceAll('Ã¡', 'á').replaceAll('Ã', 'í').replaceAll('í©', 'é').replaceAll('í¡', 'á').replaceAll('í£', 'ã').replaceAll('í´', 'ô').replaceAll('íª', 'ê').replaceAll('í³', 'ó').replaceAll('í¢', 'â').replaceAll('íº', 'ú')
                        name = name.replaceAll('ç', 'c').replaceAll('í', 'i').replaceAll('é', 'e').replaceAll('á', 'a').replaceAll('ã', 'a').replaceAll('ô', 'o').replaceAll('ê', 'e').replaceAll('ó', 'o').replaceAll('â', 'a').replaceAll('ú', 'u')
                        dados.push(dados[1]);
                        dados[1] = name;
                        pares.push(dados);
                        break;
                    }
                }
            }
        }
        setPare(pares);
    }
    return(
        <Screen>
            <Topo/>
            <Pesquisa>
                <input placeholder=''></input>   
                <button onClick={(e) => cnpqcar(e)}>oii</button>
            </Pesquisa>
            <Resultados>
                {pare}
                {pare.map(item =>{
                    <button>item</button>
                })}
            </Resultados>
        </Screen>
    )
}
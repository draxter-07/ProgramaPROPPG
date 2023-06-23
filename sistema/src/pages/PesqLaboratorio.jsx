import styled from 'styled-components'
import { useNavigate } from 'react-router-dom'
import { useState } from 'react'
import Topo from './comps/Topo.jsx'
import teste from './assets/teste.jpg'

export default function PesqLaboratorio(){
    const yellowcolorUTFPR = 'rgb(250, 200, 0, 0.9)';
    const nav = useNavigate();
    const [butEquipColor, setButEquipColor] = useState(yellowcolorUTFPR);
    const [butLabColor, setButLabColor] = useState('white');
    const [busca, setBusca] = useState('');
    const itens = [['e.1', 'l.A', teste], ['e.2', 'l.A', teste], ['e.2', 'l.C', teste], ['e.3', 'l.D', teste], ['e.3', 'l.E', teste]];
    const [results, setResults] = useState(itens);
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
        flex-direction: row;
        jusitfy-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        margin: 20px 0px 0px;
    `
    const BotaoEquip = styled.button`
        background: ${butEquipColor};
        border: 1px solid rgb(0, 0, 0);
        border-radius: 5px;
        padding: 5px 7px;
        margin: 0px 10px 0px 0px;
        :hover{
            box-shadow: 0px 0px 3px rgb(0, 0, 0);
        }
    `
    const BotaoLab = styled.button`
        background: ${butLabColor};
        border: 1px solid rgb(0, 0, 0);
        border-radius: 5px;
        padding: 5px 7px;
        :hover{
            box-shadow: 0px 0px 3px rgb(0, 0, 0);
        }
    `
    const Botoes = styled.div`
        display: flex;
        flex-direction: row;
        margin: 0px 0px 20px;
    `
    const Result = styled.div`
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        border-radius: 5px;
        width: 180px;
        height: fit-content;
        margin: 0px 15px 15px 0px;
        img{
            width: 180px;
            height: 180px;
            border-top-left-radius: 5px;
            border-top-right-radius: 5px;
        }
        :hover{
            box-shadow: 0px 0px 5px rgb(0, 0, 0);
        }
    `
    const Nomes = styled.div`
        box-sizing: border-box;
        background: ${yellowcolorUTFPR};
        border-bottom-left-radius: 5px;
        border-bottom-right-radius: 5px;
        width: 100%;
        padding: 5px;
        margin: 0px;
        overflow: auto;
        div{
            border-top: 1px solid rgb(0, 0, 0);
            padding: 5px 0px 0px 0px;
            margin: 5px 0px 0px;
        }
        &::-webkit-scrollbar {
            width: 100%;
            height: 5px;
        }
        &::-webkit-scrollbar-track {
            background: rgb(0, 0, 0, 0.5);
            border-radius: 5px;

        }
        &::-webkit-scrollbar-thumb {
            background: rgb(55, 120, 191);
            border-radius: 5px;
            border: 1px solid rgb(0, 0, 0);
        }
    `
    function changeButEquip(){
        setButEquipColor(yellowcolorUTFPR);
        setButLabColor('white')
        
    }
    function changeButLab(){
        setButLabColor(yellowcolorUTFPR);
        setButEquipColor('white');
    }
    function changeResults(e){
        const search = e.target.value;
        let newResults = [];
        setBusca(search);
        if (search == ''){
            newResults = itens;
        }
        else{
            let i = 0;
            if (butEquipColor == 'white'){
                i = 1;
            }
            for (let a = 0; a < results.length; a++){
                const equip = results[a][i];
                for (let b = 0; b < equip.length - search.length + 1; b++){
                    let stringTest = '';
                    for (let c = 0; c < search.length; c++){
                        stringTest = stringTest + equip[b + c];
                    }
                    if (stringTest == search){
                        newResults.push(results[a]);
                        break;
                    }
                }
            }
        }
        setResults(newResults);
    }
    return(
        <Screen>
            <Topo/>
            <Pesquisa>
                <Botoes>
                    <BotaoEquip onClick={changeButEquip}>Equipamento</BotaoEquip>
                    <BotaoLab onClick={changeButLab}>Laboratório</BotaoLab>
                </Botoes>
                <input placeholder='' onChange={(e) => changeResults(e)} value={busca}></input>   
            </Pesquisa>
            <Resultados>
                {results.map(item =>
                    <Result>
                        <img src={item[2]}></img>
                        <Nomes>
                            {item[0]}
                            <div>
                                {item[1]}
                            </div>
                        </Nomes>
                    </Result>
                )}
            </Resultados>
        </Screen>
    )
}
import styled from 'styled-components'
import { useNavigate, Link } from 'react-router-dom'
import { useState } from 'react'
import Topo from './comps/Topo.jsx'


export default function PesqLaboratorio(){
    const yellowcolorUTFPR = 'rgb(250, 200, 0, 0.9)';
    const nav = useNavigate();
    const [butEquipColor, setButEquipColor] = useState('white');
    const [butLabColor, setButLabColor] = useState('white');
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
    function changeButEquip(){
        if (butEquipColor == 'white'){
            setButEquipColor(yellowcolorUTFPR);
        }
        else{
            setButEquipColor('white');
        }
    }
    function changeButLab(){
        if (butLabColor == 'white'){
            setButLabColor(yellowcolorUTFPR);
        }
        else{
            setButLabColor('white');
        }
    }
    return(
        <Screen>
            <Topo/>
            <Pesquisa>
                <Botoes>
                    <BotaoEquip onClick={changeButEquip}>Equipamento</BotaoEquip>
                    <BotaoLab onClick={changeButLab}>Laboratório</BotaoLab>
                </Botoes>
                <input placeholder='Pesquise aqui'></input>
            </Pesquisa>
        </Screen>
    )
}
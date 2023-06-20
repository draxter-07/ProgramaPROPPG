import styled from 'styled-components'
import Topo from './comps/Topo.jsx'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

export default function Menu(){
    const yellowcolorUTFPR = 'rgb(250, 200, 0, 0.9)';
    const nav = useNavigate();
    const [name, setName] = useState('https://jucisrs.rs.gov.br/upload/arquivos/201710/30150625-criacao-de-pdf-a.pdf')
    const Screen = styled.div`
        box-sizing: border-box;
        width: 100vw;
        height: auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 50px 0px 0px;
    `
    const Conteudo = styled.div`
        width: 70%;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    `
    const PesquisaRelatorio = styled.div`
        width: 50%;
        padding: 11px 0px 0px 0px;
        input{
            width: 100%;
        }
    `
    function Forms(){
        const FormGoogle = styled.iframe`
            width: 70%;
            height: 2600px;
            border: none;
            padding: none;
        `
        return(
            <FormGoogle src='https://docs.google.com/forms/d/e/1FAIpQLSdF2rGITAfx2S1Bc0Yi7Z5v1oQx1MNMBvSaxpez28j5gEVGsA/viewform?embedded=true'/>
        )
    }
    function Relatorio(atr){
        const Pdf = styled.embed`
            width: 100%;
            height: 85vh;
            border: none;
            padding: none;
        `
        return(
            <Pdf type='application/pdf' src={atr.src}/>
        )
    }
    function findName(e){
        const divPesquisa = e.target.parentElement;
        const inputValue = divPesquisa.children[0].value;
        setName(inputValue);
    }
    return(
        <Screen>
            <Topo/>
            <Conteudo>
                <PesquisaRelatorio>
                    <input placeholder="Pesquise aqui o relatório do aluno"></input>
                    <button onClick={(e) => findName(e)}>oi</button>
                    <Relatorio src={name + '.pdf'}/>
                </PesquisaRelatorio>
                <Forms/>
            </Conteudo>
        </Screen>
    )
}
import styled from 'styled-components'
import { useNavigate, Link } from 'react-router-dom'
import Topo from './comps/Topo.jsx'


export default function PesqLaboratorio(){
    const yellowcolorUTFPR = 'rgb(250, 200, 0, 0.9)';
    const nav = useNavigate();
    const Screen = styled.div`
        box-sizing: border-box;
        width: 100vw;
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 50px 0px 0px;
    `
    const Menu = styled.div`
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: auto;
        height: auto;
    `
    return(
        <Screen>
            <Topo/>
            lab
        </Screen>
    )
}
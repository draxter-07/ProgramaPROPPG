import styled from 'styled-components'
import Topo from './comps/Topo.jsx'
import Teste from './assets/teste.jpg'
import Formsimg from './assets/forms.jpg'
import lab from './assets/lab.jpg'
import { useNavigate } from 'react-router-dom'

export default function Menu(){
    const yellowcolorUTFPR = 'rgb(250, 200, 0, 0.9)';
    const nav = useNavigate();
    const MenuOption = styled.button`
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        background: none;
        border-radius: 5px;
        width: 180px;
        height: fit-content;
        margin: 0px 0px 15px;
        img{
            width: 180px;
            height: 180px;
            border-top-left-radius: 5px;
            border-top-right-radius: 5px;
        }
        div{
            box-sizing: border-box;
            background: ${yellowcolorUTFPR};
            border-bottom-left-radius: 5px;
            border-bottom-right-radius: 5px;
            width: 100%;
            padding: 5px;
            margin: 0px;
            
        }
        :hover{
            box-shadow: 0px 0px 5px rgb(0, 0, 0);
        }
    `
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
        width: 50%;
        height: auto;
        div{
            box-sizing: border-box;
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            height: auto;
        }
    `
    return(
        <Screen>
            <Topo/>
            <Menu>
                <div>
                    <MenuOption onClick={() => nav('/searchlab')}>
                        <img src={lab}></img>
                        <div>Laboratório</div>
                    </MenuOption>
                    <MenuOption onClick={() => nav('/forms')}>
                        <img src={Formsimg}></img>
                        <div>Formulário</div>
                    </MenuOption>
                    <MenuOption onClick={() => nav('/')}>
                        <img src={Teste}></img>
                        <div>Vazio</div>
                    </MenuOption>
                    <MenuOption onClick={() => nav('/')}>
                        <img src={Teste}></img>
                        <div>Vazio</div>
                    </MenuOption>
                </div>
                <div>
                    <MenuOption onClick={() => nav('/')}>
                        <img src={Teste}></img>
                        <div>Vazio</div>
                    </MenuOption>
                    <MenuOption onClick={() => nav('/')}>
                        <img src={Teste}></img>
                        <div>Vazio</div>
                    </MenuOption>
                    <MenuOption onClick={() => nav('/')}>
                        <img src={Teste}></img>
                        <div>Vazio</div>
                    </MenuOption>
                    <MenuOption onClick={() => nav('/')}>
                        <img src={Teste}></img>
                        <div>Vazio</div>
                    </MenuOption>
                </div>
            </Menu>
        </Screen>
    )
}
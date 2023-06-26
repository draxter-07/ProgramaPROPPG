import styled from 'styled-components'
import Topo from './comps/Topo.jsx'
import teste from './assets/teste.jpg'
import formsimg from './assets/forms.jpg'
import cnpq from './assets/cnpq.png'
import lab from './assets/lab.jpg'
import { useNavigate } from 'react-router-dom'

export default function Menu(){
    const yellowcolorUTFPR = 'rgb(250, 200, 0, 0.9)';
    const nav = useNavigate();
    const itens = [['Laboratório', lab], ['Formulário', formsimg], ['CNPq', cnpq], ['vazio', teste], ['vazio', teste], ['vazio', teste], ['vazio', teste]]
    const MenuOption = styled.button`
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        background: none;
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
        width: 50%;
        height: auto;
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;
        flex-wrap: wrap;
    `
    return(
        <Screen>
            <Topo/>
            <Menu>
                {itens.map(item => 
                    <MenuOption onClick={() => nav('/' + item[0])}>
                        <img src={item[1]}></img>
                        <div>{item[0]}</div>
                    </MenuOption>
                )}
            </Menu>
        </Screen>
    )
}
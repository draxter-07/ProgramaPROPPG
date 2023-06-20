import styled from 'styled-components'
import { onChange, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import LogoUTFPR from './assets/logoUtfpr.jpg'


export default function LoginPage(){
    const yellowcolorUTFPR = 'rgb(250, 200, 0, 0.9)';
    const nav = useNavigate();
    //let [user, setUser] = useState('');
    //let [passw, setPassw] = useState('');
    const [mensagem, setMensagem] = useState('');
    const [notFound, setNotFound] = useState('rgb(0, 0, 0)');
    const sleep = ms => new Promise(r => setTimeout(r, ms));
    const Screen = styled.div`
        width: 100vw;
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-around;
    `
    const LoginSection = styled.div`
        box-sizing: broder-box;
        display: flex;
        flex-direction: column;
        align-items: center;
        border-radius: 10px;
        width: auto;
        height: auto;
        padding: 50px 50px 0px;
        box-shadow: 0px 0px 20px ${notFound};
        div{
            height: 20px;
            margin: 0px 0px 10px;
        }
        img{
            width: 200px;
            height: auto;
            margin: 0px 0px 20px;
        }
        input{
            box-sizing: border-box;
            margin: 0px 0px 5px;
            border-radius: 5px;
            border: 1px solid rgb(0, 0, 0, 0);
            width: 200px;
            padding: 5px;
        }
        button{
            background: ${yellowcolorUTFPR};
            border: none;
            border-radius: 5px;
            margin: 45px 0px 10px;
            padding: 5px 10px;
            color: rgb(0, 0, 0);
            font-weight: bold;
            :hover{
                background: rgb(0, 0, 0);
                color: ${yellowcolorUTFPR};
            }
        }
        :hover{
            box-shadow: 0px 0px 25px ${notFound};
        }
    `
    async function verificarLogin(e){
        let loginSec = e.target.parentElement;
        let user = loginSec.children[1].value;
        let pass = loginSec.children[2].value;
        if (user == 'philippe'){
            setNotFound('rgb(0, 255, 0)');
            setMensagem('Seja bem-vindo!')
            await sleep(2000);
            nav('/menu');
        }
        else {
            setNotFound('rgb(255, 0, 0)');
            setMensagem('Usuário não encontrado')
            await sleep(2000);
            setNotFound('rgb(0, 0, 0)');
            setMensagem('')
        }
    }
    return(
        <Screen>
            <LoginSection>
                <img src={LogoUTFPR}></img>
                <input type='username' placeholder='Usuário'></input>
                <input type='password' placeholder='Senha'></input>
                <button onClick={(e) => verificarLogin(e)}>Login</button>
                <div>{mensagem}</div>
            </LoginSection>
        </Screen>
    )
}
import styled from 'styled-components'
import { onChange, useState } from 'react'
import LogoUTFPR from './assets/logoUtfpr.jpg'


export default function LoginPage(){
    const yellowcolorUTFPR = 'rgb(250, 200, 0, 0.9)';
    let [user, setUser] = useState('');
    let [passw, setPassw] = useState('');
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
        border: 1px solid rgb(0, 0, 0);
        border-radius: 10px;
        width: auto;
        height: auto;
        padding: 50px;
        img{
            width: 200px;
            height: auto;
            margin: 0px 0px 20px;
        }
        input{
            box-sizing: border-box;
            margin: 0px 0px 5px;
            border-radius: 5px;
            border: 1px solid rgb(0, 0, 0);
            width: 200px;
            padding: 5px;
        }
        button{
            background: ${yellowcolorUTFPR};
            border: 1px solid rgb(0, 0, 0);
            border-radius: 5px;
            margin: 0px;
            padding: 5px 10px;
            color: rgb(0, 0, 0);
            :hover{
                background: rgb(0, 0, 0);
                color: ${yellowcolorUTFPR};
            }
        }
    `
    function verificarLogin(){
        console.log(user);
    }
    return(
        <Screen>
            <LoginSection>
                <img src={LogoUTFPR}></img>
                <input type='username' placeholder='Usuário' onChange={(e) => setUser(e.target.value)} value={user}></input>
                <input type='password' placeholder='Senha' onChange={(e) => setPassw(e.target.value)} value={passw}></input>
                <button onClick={verificarLogin}>Login</button>
            </LoginSection>
        </Screen>
    )
}
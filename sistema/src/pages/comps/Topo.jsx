import styled from 'styled-components'
import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import LogoUTFPR from './assets/logoUtfpr.jpg'
import User from './assets/teste.jpg'

export default function Topo(){
    const yellowcolorUTFPR = 'rgb(250, 200, 0, 0.9)';
    const nav = useNavigate();
    const [profConfig, setProfConfig] = useState('none');
    const Logo = styled.div`
        box-sizing: border-box;
        position: fixed;
        top: 0px;
        left: 0px;
        margin: 20px 0px 0px 20px;
        padding: 15px;
        box-shadow: 0px 0px 10px rgb(0, 0, 0);
        border-radius: 5px;
        height: 60px;
        width: fit-content;
        button{
            width: 100%;
            height: 100%;
            background: none;
            border: none;
            img{
                height: 100%;
            }
        }
        :hover{
            box-shadow: 0px 0px 15px rgb(0, 0, 0);
        }
    `
    const Profile = styled.div`
        box-sizing: border-box;
        position: fixed;
        top: 0px;
        right: 0px;
        margin: 20px 20px 0px 0px;
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        box-shadow: 0px 0px 10px rgb(0, 0, 0);
        height: auto;
        width: auto;
        padding: 10px 10px 0px;
        border-radius: 5px;
        div{
            display: ${profConfig};
            flex-direction: column;
            *{
                box-sizing: border-box;
                padding: 3px 5px;
                margin: 0px 20px 10px 0px;
                border-radius: 5px;
                border: 1px solid rgb(0, 0, 0, 0);
                width: 100px;
                background: ${yellowcolorUTFPR};
                text-decoration: none;
                color: rgb(0, 0, 0);
                text-align: center;
                :hover{
                    background: rgb(0, 0, 0);
                    color: ${yellowcolorUTFPR};
                }
            }
        }
        button{
            background: none;
            height: 100%;
            width: 100%;
            border: none;
            padding: 0px;
            margin: 0px 0px 7px;
            img{
                height: 40px;
                width: 40px;
                border-radius: 20px;
            }
        }
        :hover{
            box-shadow: 0px 0px 15px rgb(0, 0, 0);
        }
    `
    function navMenu(){
        nav('/menu');
    }
    function openProfile(){
        if (profConfig == 'none'){
            setProfConfig('flex');
        }
        else{
            setProfConfig("none");
        }
    }
    return(
        <>
            <Logo>
                <button onClick={navMenu}><img src={LogoUTFPR}></img></button>
            </Logo>
            <Profile>
                <div>
                    <Link to='/'>Sair</Link>
                    <Link to='/'>Sair</Link>
                    <Link to='/'>Sair</Link>
                    <Link to='/'>Sair</Link>
                </div>
                <button onMouseOver={openProfile}><img src={User}></img></button>
            </Profile>
        </>
    )
}
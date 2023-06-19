import styled from 'styled-components'
import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import LogoUTFPR from './assets/logoUtfpr.jpg'
import User from './assets/user.jpg'

export default function Topo(){
    const yellowcolorUTFPR = 'rgb(250, 200, 0, 0.9)';
    const nav = useNavigate();
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
        img{
            height: 100%;
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
        align-items: center;
        box-shadow: 0px 0px 10px rgb(0, 0, 0);
        height: 60px;
        padding: 10px;
        border-radius: 5px;
        div{
            *{
                box-sizing: border-box;
                padding: 3px 5px;
                border-radius: 5px;
                border: 1px solid rgb(0, 0, 0, 0);
                background: ${yellowcolorUTFPR};
                text-decoration: none;
                color: rgb(0, 0, 0);
                :hover{
                    background: rgb(0, 0, 0);
                    color: ${yellowcolorUTFPR};
                }
            }
        }
        img{
            height: 100%;
            border-radius: 30px;
            margin: 0px 0px 0px 20px;
        }
    `
    return(
        <>
            <Logo>
                <img src={LogoUTFPR}></img>
            </Logo>
            <Profile>
                <div>
                    <Link to='/'>Sair</Link>
                </div>
                <img src={User}></img>
            </Profile>
        </>
    )
}
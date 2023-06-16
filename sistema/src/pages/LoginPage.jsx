import styled from 'styled-components'
import { Link } from 'react-router-dom'

export default function LoginPage(){
    const Screen = styled.div`
        width: 100vw;
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-around;
    `
    const LoginSection = styled.div`
        padding: 1%;
        border: 1px solid rgb(0, 0, 0);
        width: 50%;
        height: auto;
    `
    return(
        <Screen>
            <LoginSection>
                login
                <Link to='/menu'>Aqui</Link>
            </LoginSection>
        </Screen>
    )
}
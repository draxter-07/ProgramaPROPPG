import { Route, Routes, BrowserRouter} from 'react-router-dom'
import LoginPage from './pages/LoginPage'
import Menu from './pages/Menu'
import PesqLaboratorio from './pages/PesqLaboratorio'
import Forms from './pages/Forms'
import CNPq from './pages/CNPq'
import ResetStyle from "./styles/ResetStyle.js"

export default function App() {
  return (
    <>
      <ResetStyle/>
      <BrowserRouter>
        <Routes>
          <Route element={<LoginPage/>} path='/'/>
          <Route element={<Menu/>} path='/menu'/>
          <Route element={<PesqLaboratorio/>} path='/Laboratório'/>
          <Route element={<Forms/>} path='/Formulário'/>
          <Route element={<CNPq/>} path='/CNPq'/>
        </Routes>
      </BrowserRouter>
    </>
  )
}

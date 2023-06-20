import { Route, Routes, BrowserRouter} from 'react-router-dom'
import LoginPage from './pages/LoginPage'
import Menu from './pages/Menu'
import PesqLaboratorio from './pages/PesqLaboratorio'
import Forms from './pages/Forms'
import ResetStyle from "./styles/ResetStyle.js"

export default function App() {
  return (
    <>
      <ResetStyle/>
      <BrowserRouter>
        <Routes>
          <Route element={<LoginPage/>} path='/'/>
          <Route element={<Menu/>} path='/menu'/>
          <Route element={<PesqLaboratorio/>} path='/searchlab'/>
          <Route element={<Forms/>} path='/forms'/>
        </Routes>
      </BrowserRouter>
    </>
  )
}

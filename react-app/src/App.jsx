import './App.css'
import Login from './components/Login'
import Signup from './components/SignUp'

function App() {
  return (
    <div  className="items-center">
      <div className="flex items-center justify-center p-20">
        <Signup/>
      </div>
      <div className="flex items-center justify-center">
        <Login />
      </div> 
    </div>  
  )
}

export default App

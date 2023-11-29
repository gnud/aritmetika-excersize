import logo from './logo.svg';
import './App.css';
import './Form';
import MyForm from "./Form";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <MyForm></MyForm>
      </header>
    </div>
  );
}

export default App;

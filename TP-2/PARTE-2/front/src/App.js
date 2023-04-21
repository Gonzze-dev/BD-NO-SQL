import { Route, Routes } from "react-router-dom";

import './App.css';

import FormAddPersnaje from "./formAddPersnaje/FormAddPersnaje";
import FormDeleteCharacter from "./formDeleteCharacter/FormDeleteCharacter";
import FormGetChacaters from "./formGetChacaters/FormGetChacaters";

import Layout from './layout/Layout';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/' element={<Layout/>}>
          <Route path="/add" element={<FormAddPersnaje/>} />
          <Route path="/delete" element={<FormDeleteCharacter/>} />
          <Route path="/list" element={<FormGetChacaters/>} />
        </Route>
      </Routes>
    </div>
  );
}

export default App;

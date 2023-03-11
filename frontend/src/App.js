import { Routes, Route } from "react-router-dom";

import Home from "./pages/home"
import Profile from "./pages/profile"
import History from "./pages/history"
import Update from "./pages/updates"
import NavBar from "./pages/navbar";


function App() {
  return (
    <div id="app">
      <NavBar/>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/settings" element={<Profile/>}/>
        <Route path="/history" element={<History/>}/>
        <Route path="/updates" element={<Update/>}/>
      </Routes>
    </div>
  );
}

export default App;

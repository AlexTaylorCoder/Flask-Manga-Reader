import { Routes, Route } from "react-router-dom";

import Home from "./pages/home"
import Profile from "./pages/profile"
import History from "./pages/history"
import Update from "./pages/updates"

function App() {
  return (
    <div className="App">
      <nav>
      </nav>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/profile" element={<Profile/>}/>
        <Route path="/history" element={<History/>}/>
        <Route path="/update" element={<Update/>}/>
      </Routes>
    </div>
  );
}

export default App;

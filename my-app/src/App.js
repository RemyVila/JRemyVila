import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

// import all components that will be routed to in the app.

import Hangman from './views/hangman/Hangman';
import Toolbar from './views/Toolbar';
import LogIn from './views/LogInRegister/LogIn';
import Register from './views/LogInRegister/Register';

import Home from './views/Home';

function App() {
  return (
    <Router>
      <Toolbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/hangman" element={<Hangman />} />
        <Route path="/login" element={<LogIn />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </Router>
  );
}

export default App;

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import React, { useState } from 'react';

import Hangman from './views/hangman/Hangman';
import Toolbar from './views/Toolbar';
import LogIn from './views/LogInRegister/LogIn';
import Register from './views/LogInRegister/Register';
import Home from './views/Home';

function App() {
  const [userForLogOut, setUserForLogOut] = useState(null);

  const handleLogin = (user) => {
    setUserForLogOut(user);
  };

  return (
    <Router>
      <Toolbar userForLogOut={userForLogOut} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/hangman" element={<Hangman userForLogOut={userForLogOut} />} />
        <Route
          path="/login"
          element={<LogIn userForLogOut={userForLogOut} onLogin={handleLogin} />}
        />
        <Route path="/register" element={<Register />} />
      </Routes>
    </Router>
  );
}

export default App;
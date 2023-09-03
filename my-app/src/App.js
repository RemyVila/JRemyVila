import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import React, { useState } from 'react';

// Import all components that will be routed to in the app.
import Hangman from './views/hangman/Hangman';
import Toolbar from './views/Toolbar';
import LogIn from './views/LogInRegister/LogIn';
import Register from './views/LogInRegister/Register';
import Home from './views/Home';

function App() {
  // State to pass to LogIn's sibling
  const [userForLogOut, setUserForLogOut] = useState(null);

  // Function to handle login (replace this with your actual login logic)
  const handleLogin = (userForLogOut) => {
    // After a successful login, set the user in state
    setUserForLogOut(userForLogOut);
    console.log(userForLogOut)
  };

  return (
    <Router>
      <Toolbar userForLogOut={userForLogOut} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/hangman" element={<Hangman />} />
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

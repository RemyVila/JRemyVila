import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function Toolbar({ userForLogOut }) {
  // Initialize isLoggedIn state to false
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    // Check if userForLogOut is defined and update isLoggedIn accordingly
    if (userForLogOut) {
      setIsLoggedIn(true);
    } else {
      setIsLoggedIn(false);
    }
  }, [userForLogOut]);

  // Function to handle logout
  const handleLogout = async () => {
    try {
      // Send a POST request to the logout endpoint
      await axios.post('http://127.0.0.1:8000/api/logout/', userForLogOut);

      // Update the isLoggedIn state to false
      setIsLoggedIn(false);
    } catch (error) {
      // Handle any errors that may occur during the logout process
      console.error('Logout error:', error);
    }
  };

  return (
    <div className="toolbar">
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/hangman">Hangman</Link>
        </li>

        {isLoggedIn ? (
          <li>
            <button onClick={handleLogout}>Logout {userForLogOut.user}</button>
          </li>
        ) : (
          <li>
            <Link to="/login">Log In</Link>
          </li>
        )}
      </ul>
    </div>
  );
}

export default Toolbar;

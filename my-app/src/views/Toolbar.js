import React from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function Toolbar({ userForLogOut }) {
  // to determine if to render Log Out button
  let isLoggedIn = false
  if(userForLogOut){
    isLoggedIn = true
  }    
  console.log('User data:', userForLogOut);


  const handleLogout = async () => {
    try {
      // Send a POST request to the logout endpoint
      await axios.post('http://127.0.0.1:8000/api/logout/', userForLogOut);

      window.location.href = '/login';
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

        {isLoggedIn
          ? <li><button onClick={handleLogout}>Logout {userForLogOut.user}</button></li>
          :
        <li>
          <Link to="/login">Log In {isLoggedIn}</Link>
        </li>
        }
      </ul>
    </div>
  );
}

export default Toolbar;
import React from 'react';
import { Link } from 'react-router-dom';

function Toolbar() {
  return (
    <div className="toolbar">
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/hangman">Hangman</Link>
        </li>
        <li>
            <Link to="/login">Log In</Link>
        </li>
      </ul>
    </div>
  );
}

export default Toolbar;
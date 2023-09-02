import React from 'react';
import Hangman from './hangman/Hangman';

function SmallApps() {
  return (
    <div>
      <h1>Small Apps</h1>
      <p>There's a few nifty little programs I made here and wanted to
        put in my website.
      </p>
      <Hangman/>
    </div>
  );
}

export default SmallApps;
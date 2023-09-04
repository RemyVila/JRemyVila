import React, { useEffect, useState } from 'react';
import axios from 'axios';
import limbs4 from './assets/4 limbs.jpg';
import limbs3 from './assets/3 limbs.jpg';
import limbs2 from './assets/2 legs.jpg';
import limbs1 from './assets/1 leg.jpg';
import limbs0 from './assets/0 limbs.jpg';

function Hangman() {
  const testingAPI = 'http://127.0.0.1:8000/';

  const [wordBankData, setWordBankData] = useState([]);
  const [workingWord, setWorkingWord] = useState([]);
  const [limbs, setLimbs] = useState(4);
  const [leaderboard, setLeaderboard] = useState([
    {
      user: "empty leaderboard",
      wins: 0,
      losses: 0
    }
  ]);

  // on-mount
  useEffect(() => {
    // Make a GET request to the API endpoint
    axios.get(`${testingAPI}api/hangman-wordbank/`)
      .then((response) => {
        setWordBankData(response.data);
        
        // Generate a random word and split it into an array
        const randomIndex = Math.floor(Math.random() * response.data.length);
        const randomWord = response.data[randomIndex].name;
        const randomWordArray = randomWord.split('');
        setWorkingWord(randomWordArray);
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error fetching data:', error);
      });
    
    axios.get(`${testingAPI}api/leaderboard/`)
      .then((response) => {
        setLeaderboard(response.data.leaderboard);
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error fetching data:', error);
      });
  }, []);

  // Define the image file paths based on limbs count
  let limbImagePath;
  switch (limbs) {
    case 4:
      limbImagePath = limbs4;
      break;
    case 3:
      limbImagePath = limbs3;
      break;
    case 2:
      limbImagePath = limbs2;
      break;
    case 1:
      limbImagePath = limbs1;
      break;
    case 0:
      limbImagePath = limbs0;
      break;
    default:
      limbImagePath = limbs4; // Default to 4 limbs if limbs value is not recognized
  }

  return (
    <div>
      <div>
        <h3>Hangman</h3>
        <div>
          <img className="hangman_limbs" src={limbImagePath} alt={`Hangman with ${limbs} limbs`} />
        </div>
        
        <div>
          <h4>Leaderboard</h4>
            {leaderboard.map((item) => (
              <li key={item.id}>
                User: {item.user} <br />
                Wins: {item.wins} <br />
                Losses: {item.losses} <br />
                Win Rate: {(item.wins / (item.losses + item.wins || 1) * 100).toFixed(2)}%
              </li>
            ))}
        </div>
      </div>
    </div>
  );
}

export default Hangman;

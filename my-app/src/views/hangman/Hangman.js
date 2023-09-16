import React, { useEffect, useState } from 'react';
import axios from 'axios';

import limbs4 from './assets/4 limbs.jpg';
import limbs3 from './assets/3 limbs.jpg';
import limbs2 from './assets/2 legs.jpg';
import limbs1 from './assets/1 leg.jpg';
import limbs0 from './assets/0 limbs.jpg';

import config from '../../config';
axios.defaults.baseURL = config.baseURL;


function Hangman({ userForLogOut }) {
  // State for word bank data, working word, limbs count, known letters, and leaderboard
  const [wordBankData, setWordBankData] = useState([]);
  const [workingWord, setWorkingWord] = useState([]);
  const [wordHint, setWordHint] = useState('');
  const [limbs, setLimbs] = useState(4);
  const [knownLetters, setKnownLetters] = useState([]);
  const [guessedLetters, setGuessedLetters] = useState([]);
  const [gameStatus, setGameStatus] = useState('playing'); // 'playing', 'won', or 'lost'

  

  // Initialize leaderboard with a default entry
  const [leaderboard, setLeaderboard] = useState([
    {
      user: "empty leaderboard",
      wins: 0,
      losses: 0
    }
  ]);

  // Initialize a state variable to track whether the player has won
  const [hasWon, setHasWon] = useState(false);

  // useEffect to fetch data on component mount
  useEffect(() => {
    fetchWordBankData();
    fetchLeaderboardData();
  }, []);

  // Function to fetch word bank data
  const fetchWordBankData = () => {
    axios.get(`api/hangman-wordbank/`)
      .then((response) => {
        setWordBankData(response.data);
  
        // Generate a random word and split it into an array
        const randomIndex = Math.floor(Math.random() * response.data.length);
        const selectedWordData = response.data[randomIndex];
        const randomWord = selectedWordData.name;
        const randomWordArray = randomWord.split('');
        setWorkingWord(randomWordArray);
  
        // Set the hint for the selected word
        setWordHint(selectedWordData.hint);
  
        // Initialize knownLetters with 0 for each letter in the word
        const computedKnownLetters = randomWordArray.map((char) => (char === ' ' ? ' ' : 0));
        setKnownLetters(computedKnownLetters);
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error fetching word bank data:', error);
      });
  };
  

  // Function to fetch leaderboard data
  const fetchLeaderboardData = () => {
    axios.get(`api/leaderboard/`)
      .then((response) => {
        setLeaderboard(response.data.leaderboard);
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error fetching leaderboard data:', error);
      });
  };

  // Function to handle letter guesses
  const handleGuess = (letter) => {
    if (gameStatus === 'playing') {
      const normalizedLetter = letter.toLowerCase(); // Convert the guessed letter to lowercase

      if (!guessedLetters.includes(normalizedLetter)) {
        setGuessedLetters([...guessedLetters, normalizedLetter]);

        if (workingWord.some((char) => char.toLowerCase() === normalizedLetter)) {
          const updatedKnownLetters = knownLetters.map((char, index) =>
            workingWord[index].toLowerCase() === normalizedLetter ? workingWord[index] : char
          );
          setKnownLetters(updatedKnownLetters);

          if (!updatedKnownLetters.includes(0)) {
            setGameStatus('won');
            setHasWon(true); // Set the hasWon state to true

            // Conditional posting of user data
            let userData = null
            if(userForLogOut){
              userData = typeof userForLogOut === 'object' ? userForLogOut.user : userForLogOut;
              axios.post(`api/leaderboard/update/`, {
                user: userData,
                game_result: 1,
              })
                .then(() => {
                  // Fetch leaderboard data immediately after updating
                  fetchLeaderboardData();
                })
                .catch((error) => {
                  console.error('Error updating leaderboard:', error);
                });
            }
            else{
              axios.post(`api/leaderboard/update/`, {
                user: "Default",
                game_result: 1,
              })
                .then(() => {
                  // Fetch leaderboard data immediately after updating
                  fetchLeaderboardData();
                })
                .catch((error) => {
                  console.error('Error updating leaderboard:', error);
                });
            }
          }
        } else {
          setLimbs((prevLimbs) => prevLimbs - 1);

          if (limbs === 0) {
            setGameStatus('lost');

            // Conditional posting of user data
            let userData = null
            if(userForLogOut){
              userData = typeof userForLogOut === 'object' ? userForLogOut.user : userForLogOut;
              axios.post(`api/leaderboard/update/`, {
                user: userData,
                game_result: 0,
              })
                .then(() => {
                  // Fetch leaderboard data immediately after updating
                  fetchLeaderboardData();
                })
                .catch((error) => {
                  console.error('Error updating leaderboard:', error);
                });
            }
            else{
              axios.post(`api/leaderboard/update/`, {
                user: "Default",
                game_result: 0,
              })
                .then(() => {
                  // Fetch leaderboard data immediately after updating
                  fetchLeaderboardData();
                })
                .catch((error) => {
                  console.error('Error updating leaderboard:', error);
                });
            }
            }
        }
      }
    }
  };

// Function to restart the game
const restartGame = () => {
  setLimbs(4);
  setKnownLetters([]);
  setGuessedLetters([]);
  setGameStatus('playing');
  setHasWon(false); // Reset the hasWon state

  // Fetch a new word from the word bank using wordBankData
  if (wordBankData.length > 0) {
    const randomIndex = Math.floor(Math.random() * wordBankData.length);
    const selectedWordData = wordBankData[randomIndex];
    const randomWord = selectedWordData.name;
    const randomWordArray = randomWord.split('');
    setWorkingWord(randomWordArray);

    // Set the hint for the selected word
    setWordHint(selectedWordData.hint);

    // Initialize knownLetters with 0 for each letter in the word
    const computedKnownLetters = randomWordArray.map((char) => (char === ' ' ? ' ' : 0));
    setKnownLetters(computedKnownLetters);
  }
};

  // Determine the image file path based on limbs count
  let limbImagePath;
  switch (limbs) {
    case 0:
      limbImagePath = limbs4;
      break;
    case 1:
      limbImagePath = limbs3;
      break;
    case 2:
      limbImagePath = limbs2;
      break;
    case 3:
      limbImagePath = limbs1;
      break;
    case 4:
      limbImagePath = limbs0;
      break;
    default:
      limbImagePath = limbs4; // Default to 4 limbs if limbs value is not recognized
  }

  return (
    <div className='hangmanContainer'>
      <div>
        <h3>If you are not logged in, user on leaderboard update will default to "Default"</h3>
        <h1>Hangman</h1>
        <div>
          <img className="hangman_limbs" src={limbImagePath} alt={`Hangman with ${limbs} limbs`} />
        </div>
        <div>
          <h4>Guess the Word</h4>
          {gameStatus === 'playing' ? (
            <div>
              {knownLetters.map((char, index) => (
                <span key={index} className="letter">
                  {char === ' ' ? ' ' : char === 0 ? '_ ' : char}
                </span>
              ))}
                <div>
                  <h4>Hint</h4>
                  <p>{wordHint}</p>
                </div>
              <div>
                <div>
                  <h5>Guessed Letters</h5>
                  <div>
                    {guessedLetters.map((letter, index) => (
                      <span key={index}>{letter}</span>
                    ))}
                  </div>
                </div>
                <div>
                  <h5>Make a Guess</h5>
                  <div>
                    You have {limbs + 1} guesses left!
                  </div>
                  <div>
                    {Array.from({ length: 26 }, (_, i) => (
                      <button
                        key={i}
                        onClick={() => handleGuess(String.fromCharCode(65 + i))}
                        disabled={guessedLetters.includes(String.fromCharCode(65 + i))}
                      >
                        {String.fromCharCode(65 + i)}
                      </button>
                    ))}
                    <button
                      onClick={() => handleGuess('-')}
                      disabled={guessedLetters.includes('-')}
                    >
                      -
                    </button>
                  </div>
                </div>
              </div>
            </div>
          ) : (
            <div>
              {hasWon ? <h5>You won!</h5> : <h5>You lost!</h5>}
              <button onClick={restartGame}>Restart Game</button>
            </div>
          )}
        </div>
        <div>
          <h2>Leaderboard</h2>
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

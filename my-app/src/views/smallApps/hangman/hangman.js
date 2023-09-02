import { React, useEffect, useState } from 'react';
import axios from 'axios';

function Hangman() {
  const [wordBankData, setWordBankData] = useState([]);
  const testingAPI = 'http://127.0.0.1:8000/';

  useEffect(() => {
    // Make a GET request to the API endpoint
    axios.get(`${testingAPI}api/hangman-wordbank/`)
      .then((response) => {
        // Handle the response data
        setWordBankData(response.data);
        console.log(wordBankData)
      })
      .catch((error) => {
        // Handle any errors
        console.error('Error fetching data:', error);
      });
  }, []); // The empty dependency array ensures this effect runs once on component mount

  return (
    <div>
      <div>
        <h3>Hangman</h3>
        {/* Render the fetched data */}
        <div>
          {wordBankData.map((item) => (
            <li key={item.id}>
              Word: {item.name}
              Hint: {item.hint}
            </li>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Hangman;
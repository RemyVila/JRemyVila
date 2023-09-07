import React from 'react';
import '../App.css';
import ai_remy from './AI_Remy.jpg'

function Home() {
    return (
      <div className='container'>
        <div className='miniContainer'>
          <h1 className='head'>Remy Vila</h1>
          <img className='imgSize' src={ai_remy} alt="Cool AI generated Remy" />
          <p>
            Hi, I'm Remy. I'm an aspiring programmer and this is my first fullstack built website. I made this
            using React for the GUI and frontend handling, then Django for the database / server.
          </p>
          <p>
            As you can see, you are able to register, log in and log out. The register function is working as intended,
            including with Django.
          </p>
          <p>
            There is no ACTUAL auth implemented in this site yet. I am just holding the username in state,
            so if a component has to remount e.g. by refreshing the page.
          </p>
          <p>
            The logged in username will be lost, and
            you will encounter an error if you try to submit a win or loss to the Hangman leaderboard.
          </p>
          <p>
            The pseudo auth implentation I used is also the reason you probably had your browser notify you that
            your password was leaked.
          </p>
          <p>
            Because I imagine this may happen often, I feel the need to say I did not follow a tutorial or guide
            for any of this.
            Only documentation and a little chatGPT as resources.
          </p>
        </div>
      </div>
    );
  }
  
  export default Home;
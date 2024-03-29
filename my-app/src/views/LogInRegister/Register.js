import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import config from '../../config';
axios.defaults.baseURL = config.baseURL;


function Register() {
  const [registered, setRegistered] = useState(false);
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    confirmPassword: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    let submittedData = {
      user: formData.username,
      password: formData.password
    }
    // Make an API request to register the user with the form data
    try {
      await axios.post(`api/register/`, submittedData)
      .then(res => {
        console.log(res.data)
        setRegistered(true)
      })
    } catch (error) {
      console.log(formData)
      console.log(submittedData)
    }
  };

  return (
    <div className='logInContainer'>
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            name="username"
            value={formData.username}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="confirmPassword">Confirm Password:</label>
          <input
            type="password"
            id="confirmPassword"
            name="confirmPassword"
            value={formData.confirmPassword}
            onChange={handleInputChange}
          />
        </div>
        <button type="submit">Register</button>
      </form>
      {registered ? (
        <div> User "{formData.username}" registered successfully </div>
      ) : <Link to="/login">Already have an account? Login</Link>}
    </div>
  );
}

export default Register;

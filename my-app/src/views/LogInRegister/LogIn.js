import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function LogIn({ onLogin }) {
  const [formData, setFormData] = useState({
    user: '',
    password: '',
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
    console.log(formData);
    try {
      await axios.post('http://127.0.0.1:8000/api/login/', formData)
      .then(res => {
        console.log(res.data.message)
        const user = { user: formData.user }; // Replace this with your login logic
        onLogin(user); // Pass the user data to the parent component
      })

      // window.location.href = '/';
    } catch (error) {

    }
    // console.log('Submitted data:', formData);
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="user">user:</label>
          <input
            type="text"
            id="user"
            name="user"
            value={formData.user}
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
        <button type="submit">Login</button>
      </form>
      <Link to="/register">Register</Link>
    </div>
  );
}

export default LogIn;
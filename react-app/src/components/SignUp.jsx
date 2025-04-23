import React, { useState } from 'react';

const Signup = () => {
    const [formData, setFormData] = useState({ username: '', password: '' });
    
    const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
    };

  const handleSubmit = async e => {
    e.preventDefault();
    const response = await fetch('http://localhost:5000/signup', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    });

    const data = await response.json();
    console.log(data);
  };

  return (
    <div>
        <div className="bg-slate-800 border border-slate-600 rounded-md p-8 shadow-lg backdrop-filter backdrop-blur-lg bg-opacity-30 relative">
            <h1 className="font-bold text-center text-4xl">Sign Up</h1>
            <form onSubmit={handleSubmit}>
                <div className="my-4 relative">
                    <input type="text" 
                    name="username"
                    value={formData.username}
                    onChange={handleChange}
                    className="block w-72 py-2.5 px-0 text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 
                    appearance-none dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:text-white focus:border-blue-600 peer" placeholder="Username"></input>
                    <label htmlFor=""  className="absolute text-sm duration-300 transform -translate scale-75 top-3 -z-10 origin-[0]"></label>
                </div>
                <div className="relative my-4">
                    <input type="password" 
                    name="password"
                    value={formData.password}
                    onChange={handleChange}
                    className="block w-72 py-2.5 px-0 text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 
                    appearance-none dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:text-white focus:border-blue-600 peer" placeholder="Password"></input>
                    <label htmlFor="" className="absolute text-sm duration-300 transform -translate scale-75 top-3 -z-10 origin-[0]"></label>
                </div>
                <button type="submit" className="w-full mb-4 text-[18px] roundedbg-blue-500 py-2 hover:bg-blue-800 transition-colors duration-300">Sign Up</button>
            </form>
        </div>
    </div>
  )
}

export default Signup
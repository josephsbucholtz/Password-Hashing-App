
const Login = () => {
  return (
    <div>
        <div className="bg-slate-800 border border-slate-600 rounded-md p-8 shadow-lg backdrop-filter backdrop-blur-lg bg-opacity-30 relative">
            <h1 className="font-bold text-center text-4xl">Login</h1>
            <form action="">
                <div className="my-4 relative">
                    <input type="text" className="block w-72 py-2.5 px-0 text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 
                    appearance-none dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:text-white focus:border-blue-600 peer" placeholder="Username"></input>
                    <label htmlFor=""  className="absolute text-sm duration-300 transform -translate scale-75 top-3 -z-10 origin-[0]"></label>
                </div>
                <div className="relative my-4">
                    <input type="password" className="block w-72 py-2.5 px-0 text-sm text-white bg-transparent border-0 border-b-2 border-gray-300 
                    appearance-none dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:text-white focus:border-blue-600 peer" placeholder="Password"></input>
                    <label htmlFor="" className="absolute text-sm duration-300 transform -translate scale-75 top-3 -z-10 origin-[0]"></label>
                </div>
                <button type="submit" className="w-full mb-4 text-[18px] roundedbg-blue-500 py-2 hover:bg-blue-800 transition-colors duration-300">Login</button>
            </form>
        </div>
    </div>
  )
}

export default Login
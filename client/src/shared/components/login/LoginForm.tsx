// import { useState, useEffect } from "react";
// import type { FormEvent } from "react";
// import useManualFetch from "../../hooks/useManualFetch";

// import { useDispatch } from "react-redux";
// import { updateAuth } from "../../../features/auth/authSlice";
// import LoginImg from "../../../assets/LoginImg.jpg"
// import { Link, useNavigate } from "react-router-dom";

// interface LoginFormProps {
//   role: string;
//   url: string;
// }

// const LoginForm = ({ role, url }: LoginFormProps) => {
//   const dispatch = useDispatch();
//   const navigate = useNavigate();

//   const [email, setEmail] = useState<string | null>(null);
//   const [password, setPassword] = useState<string | null>(null);

//   const { execute, data, status } = useManualFetch<any>();

//   const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
//     e.preventDefault();
//     await execute(url, "POST", { email, password });
//   };

//   useEffect(() => {
//     if (status === "success" && data) {
//       dispatch(
//         updateAuth({
//           authenticated: true,
//           user: `${data.first_name} ${data.last_name}`,
//         })
//       );
//       console.log("navigating to role", role);
//       navigate(`/${role}`);
//     }
//   }, [status, data, dispatch, navigate, role]);

//   return (
//     <div className="flex items-center justify-center">
//       <div className="flex w-[850px] shadow-lg rounded-lg overflow-hidden bg-white">
//         {/* Left column (form) */}
//         <div className="w-1/2 p-10">
//           <h2 className="text-2xl font-bold text-center mb-2">Welcome back</h2>
//           <p className="text-gray-500 text-center mb-6">
//             Login to your {role} account
//           </p>

//           <form onSubmit={handleSubmit} className="flex flex-col gap-4">
//             {/* Email */}
//             <label htmlFor="email" className="text-sm font-medium text-gray-600">
//               Email
//             </label>
//             <input
//               type="email"
//               name="email"
//               onChange={(e) => setEmail(e.target.value)}
//               className="border border-gray-300 rounded-3xl px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
//               required
//             />

//             {/* Password */}
//             <div className="flex justify-between items-center">
//               <label
//                 htmlFor="password"
//                 className="text-sm font-medium text-gray-600"
//               >
//                 Password
//               </label>
//               {/* <a href="#" className="text-sm text-blue-500 hover:underline">
//                 Forgot password?
//               </a> */}
//             </div>
//             <input
//               type="password"
//               name="password"
//               onChange={(e) => setPassword(e.target.value)}
//               className="border border-gray-300 rounded-3xl px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
//               required
//             />

//             {/* Error */}
//             {status === "error" && (
//               <p className="text-red-600">Incorrect Password or Email</p>
//             )}

//             {/* Login Button */}
//             <button
//               type="submit"
//               className="bg-blue-600 text-white py-2 rounded-3xl hover:bg-blue-700 transition-colors"
//             >
//               {status === "loading" ? (
//                 <span className="animate-spin inline-block w-4 h-4 border-2 border-current border-t-transparent rounded-full"></span>
//               ) : (
//                 "Login"
//               )}
//             </button>

//             {/* Sign Up */}
//             <p className="text-center text-sm text-gray-600 mt-2">
//               Don’t have an account?{" "}
//               <Link
//                 className="text-blue-600 hover:underline"
//                 to={"/auth/signup"}
//               >
//                 Sign up
//               </Link>
//             </p>
//           </form>
//         </div>

//         {/* Right column (image) */}
//         <div className="w-1/2 flex rounded-lg items-center justify-center">
//           <img
//             src={LoginImg}
//             alt="Login Illustration"
//             className="w-full h-full object-cover rounded-r-lg"
//           />
//         </div>
//       </div>
//     </div>
//   );
// };

// export default LoginForm;

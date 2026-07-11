import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY || "AIzaSyBEQTUcIlyeKasEDLVPWXEgx7KSJqBFd70",
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN || "loki-x-prime-8b088.firebaseapp.com",
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID || "loki-x-prime-8b088",
  storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET || "loki-x-prime-8b088.firebasestorage.app",
  messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID || "470871430064",
  appId: import.meta.env.VITE_FIREBASE_APP_ID || "1:470871430064:web:9dcad83b72f3c35e567c75",
  measurementId: import.meta.env.VITE_FIREBASE_MEASUREMENT_ID || "G-NWTVPF2MJP"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const analytics = typeof window !== 'undefined' ? getAnalytics(app) : null;

// Initialize Firebase Auth
import { getAuth } from "firebase/auth";
export const auth = getAuth(app);

export default app;

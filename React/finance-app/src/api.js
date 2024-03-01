
import axios from "axios";
// import './App.css';
// import React,{useState,useEffect} from 'react';
// import api from './api';

const api = axios.create({
    baseURL:'http://127.0.0.1:8000'
    
});

export default api;

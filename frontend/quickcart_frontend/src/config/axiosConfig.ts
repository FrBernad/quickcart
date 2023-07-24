import axios from 'axios';

export const apiAxios = axios.create({
  baseURL: '/api'
});

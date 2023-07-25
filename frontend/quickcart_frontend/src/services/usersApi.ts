import { apiAxios } from '@/config/axiosConfig';
import { User } from '@/models/User';

export const usersApi = {
  getUserById: async (userId: number, signal: AbortSignal): Promise<User> => {
    const response = await apiAxios.get<User>(`/users/${userId}`, {
      signal
    });
    return response.data;
  },

  login: async (email: string, password: string): Promise<User> => {
    const response = await apiAxios.post<User>(`/users/login`, {
      email,
      password
    });
    return response.data;
  },

  register: async (
    email: string,
    username: string,
    password: string
  ): Promise<User> => {
    const response = await apiAxios.post<User>(`/users`, {
      email,
      username,
      password
    });
    return response.data;
  }
};

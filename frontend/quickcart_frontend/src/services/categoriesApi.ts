import { apiAxios } from '@/config/axiosConfig';
import { Category } from '@/models/Product';

export const categoriesApi = {
  getCategories: async (signal: AbortSignal): Promise<Category[]> => {
    const response = await apiAxios.get<Category[]>(`/categories`, {
      signal
    });
    return response.data;
  },

  createCategory: async (name: string): Promise<void> => {
    await apiAxios.post<void>(`/categories`, {
      name
    });
  }
};

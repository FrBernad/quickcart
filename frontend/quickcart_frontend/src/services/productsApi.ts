import { apiAxios } from '@/config/axiosConfig';
import { Product } from '@/models/Product';

export const productsApi = {
  getProducts: async (signal: AbortSignal): Promise<Product[]> => {
    const response = await apiAxios.get<Product[]>('/products', {
      signal
    });
    return response.data;
  },

  getProductById: async (
    product_id: string,
    signal: AbortSignal
  ): Promise<Product> => {
    const response = await apiAxios.get<Product>(`/products/${product_id}`, {
      signal
    });
    return response.data;
  }
};

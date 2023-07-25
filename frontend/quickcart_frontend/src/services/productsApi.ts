import { apiAxios } from '@/config/axiosConfig';
import { Product } from '@/models/Product';
import { CreateProductFormInput } from '@/pages/create-product/CreateProductPage';

export const productsApi = {
  getProducts: async (signal: AbortSignal): Promise<Product[]> => {
    const response = await apiAxios.get<Product[]>('/products', {
      signal
    });
    return response.data;
  },

  createProduct: async (
    productData: CreateProductFormInput
  ): Promise<Product> => {
    const response = await apiAxios.post<Product>('/products', productData);
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

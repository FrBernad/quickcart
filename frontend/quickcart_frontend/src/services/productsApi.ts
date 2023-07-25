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
    userId: number,
    productData: CreateProductFormInput
  ): Promise<Product> => {
    const tags = productData.tags.split(',').map((tag) => tag.trim());

    const response = await apiAxios.post<Product>('/products', {
      ...productData,
      price: Number(productData.price),
      stock: Number(productData.stock),
      category_id: Number(productData.category.value),
      user_id: userId,
      tags
    });
    return response.data;
  },

  getProductById: async (
    product_id: number,
    signal: AbortSignal
  ): Promise<Product> => {
    const response = await apiAxios.get<Product>(`/products/${product_id}`, {
      signal
    });
    return response.data;
  }
};

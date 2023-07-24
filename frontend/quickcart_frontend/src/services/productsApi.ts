import { apiAxios } from '@/config/axiosConfig';
import { Product } from '@/models/Product';
import { wait } from '@/utils';

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

export const products: Array<Product> = [
  {
    id: 1,
    name: 'Product 1',
    price: 100,
    seller: 'Seller 1',
    stock: 10,
    score: 5
  },
  {
    id: 2,
    name: 'Product 2',
    price: 200,
    seller: 'Seller 2',
    stock: 10,
    score: 5
  },
  {
    id: 3,
    name: 'Product 3',
    price: 300,
    seller: 'Seller 3',
    stock: 10,
    score: 5
  },
  {
    id: 4,
    name: 'Product 4',
    price: 400,
    seller: 'Seller 4',
    stock: 10,
    score: 5
  },
  {
    id: 5,
    name: 'Product 5',
    price: 500,
    seller: 'Seller 5',
    stock: 10,
    score: 5
  },
  {
    id: 6,
    name: 'Product 6',
    price: 600,
    seller: 'Seller 6',
    stock: 10,
    score: 5
  }
];

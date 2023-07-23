import { apiAxios } from '@/config/api';
import { Product } from '@/models/Product';
import { wait } from '@/utils';

export const shoppingCartApi = {
  getShoppingCart: async (
    userId: string = '',
    signal: AbortSignal
  ): Promise<Product[]> => {
    // const response = await apiAxios.get<Product[]>(
    //   'http://localhost:80/products',
    //   {
    //     params: {
    //       product
    //     },
    //     signal
    //   }
    // );
    // return response.data;
    await wait(1000);
    return [];
  },

  addProduct: async (
    product: string = '',
    signal: AbortSignal
  ): Promise<void> => {
    // const response = await apiAxios.get<Product[]>(
    //   'http://localhost:80/products',
    //   {
    //     params: {
    //       product
    //     },
    //     signal
    //   }
    // );
    // return response.data;
    await wait(1000);
  },

  removeProduct: async (
    product_id: string,
    signal: AbortSignal
  ): Promise<void> => {
    // const response = await apiAxios.get<Product[]>(
    //   `http://localhost:80/products/${product_id}`,
    //   {
    //     signal
    //   }
    // );
    await wait(1000);
  }
};

import { apiAxios } from '@/config/api';
import { Product } from '@/models/Product';
import { wait } from '@/utils';
import { Order } from '@/models/Order';
import { products } from '@/services/productsApi';

export const ordersApi = {
  getUserOrders: async (
    userId: string = '',
    signal: AbortSignal
  ): Promise<Order[]> => {
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
    return [
      {
        id: 1,
        total: 100,
        products: products
      }
    ];
  }
};

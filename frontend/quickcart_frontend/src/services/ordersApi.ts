import { apiAxios } from '@/config/axiosConfig';
import { Product } from '@/models/Product';
import { wait } from '@/utils';
import { Order } from '@/models/Order';
import { products } from '@/services/productsApi';

export const ordersApi = {
  getUserOrders: async (
    userId: string = '',
    signal: AbortSignal
  ): Promise<Order[]> => {
    const response = await apiAxios.get<Order[]>('/purchase-orders', {
      signal
    });
    return response.data;
    // await wait(1000);
    // return [
    //   {
    //     id: 1,
    //     total: 100,
    //     products: products
    //   }
    // ];
  }
};

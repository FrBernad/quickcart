import { apiAxios } from '@/config/axiosConfig';
import { wait } from '@/utils';
import { Order } from '@/models/Order';

export const ordersApi = {
  getUserOrders: async (
    userId: string = '',
    signal: AbortSignal
  ): Promise<Order[]> => {
    const response = await apiAxios.get<Order[]>('/purchase-orders', {
      signal
    });
    return response.data;
  }
};

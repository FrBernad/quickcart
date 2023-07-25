import { apiAxios } from '@/config/axiosConfig';
import { Order } from '@/models/Order';

export const ordersApi = {
  getUserOrders: async (
    userId: number,
    signal: AbortSignal
  ): Promise<Order[]> => {
    const response = await apiAxios.get<Order[]>(`/purchase-orders/${userId}`, {
      signal
    });

    if (response.status === 204) return [];

    return response.data;
  }
};
